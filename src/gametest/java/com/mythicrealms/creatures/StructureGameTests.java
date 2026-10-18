package com.mythicrealms.creatures;

import com.google.gson.JsonParser;
import com.mojang.serialization.JsonOps;
import com.mythicrealms.creatures.config.CreatureConfig;
import com.mythicrealms.creatures.world.StructureContent;
import net.fabricmc.fabric.api.gametest.v1.GameTest;
import net.fabricmc.fabric.api.resource.conditions.v1.ResourceCondition;
import net.minecraft.core.BlockPos;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.core.registries.Registries;
import net.minecraft.gametest.framework.GameTestHelper;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.ResourceKey;
import net.minecraft.resources.RegistryOps;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.entity.Mob;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.EntitySpawnReason;
import net.minecraft.nbt.CompoundTag;
import net.minecraft.util.ProblemReporter;
import net.minecraft.world.level.storage.TagValueInput;
import net.minecraft.world.level.block.entity.RandomizableContainerBlockEntity;
import net.minecraft.world.level.levelgen.structure.pools.JigsawPlacement;
import net.minecraft.world.level.levelgen.structure.structures.JigsawStructure;
import net.minecraft.world.level.storage.loot.LootTable;
import net.minecraft.world.phys.AABB;

import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

public final class StructureGameTests {
    private static ResourceLocation id(String path) {
        return ResourceLocation.fromNamespaceAndPath(MythicRealmsCreatures.MOD_ID, path);
    }
    private static void check(GameTestHelper helper, boolean condition, String message) {
        helper.assertTrue(condition, Component.literal(message));
    }

    @GameTest(structure="mythic_realms_creatures_test:structures_arena", maxTicks=100, skyAccess=true)
    public void registeredJigsawsPlaceInhabitantsAndUsableLoot(GameTestHelper helper) {
        var level = helper.getLevel();
        var expected = List.of(Set.of("goblin_scout", "goblin_shaman"),
            Set.of("forest_dryad", "ancient_treant"), Set.of("grave_knight", "shadow_wraith"), Set.of("wild_wyvern"));
        for (int index=0; index<StructureContent.STRUCTURES.size(); index++) {
            String name = StructureContent.STRUCTURES.get(index);
            var registry = level.registryAccess();
            var definition = registry.lookupOrThrow(Registries.STRUCTURE)
                .getOrThrow(ResourceKey.create(Registries.STRUCTURE, id(name))).value();
            check(helper, definition instanceof JigsawStructure, name+" is a real registered jigsaw structure");
            var set = registry.lookupOrThrow(Registries.STRUCTURE_SET)
                .getOrThrow(ResourceKey.create(Registries.STRUCTURE_SET, id(name))).value();
            check(helper, set.structures().stream().anyMatch(entry -> entry.structure().value()==definition), name+" structure set resolves");
            var template = level.getStructureManager().getOrCreate(id(name));
            check(helper, template.getSize().getY()>5 && template.getSize().getX()>8, name+" nonempty template loads");
            var pool = registry.lookupOrThrow(Registries.TEMPLATE_POOL)
                .getOrThrow(ResourceKey.create(Registries.TEMPLATE_POOL, id(name+"/start")));
            BlockPos anchor = helper.absolutePos(new BlockPos(11+index*20, 2, 11));
            var encoded=JigsawStructure.CODEC.codec().encodeStart(RegistryOps.create(JsonOps.INSTANCE,registry),
                (JigsawStructure)definition).getOrThrow().getAsJsonObject();
            int depth=encoded.get("size").getAsInt();
            check(helper,depth>0,name+" configured jigsaw depth places at least one piece");
            check(helper, JigsawPlacement.generateJigsaw(level, pool, id("entry"), depth, anchor, false), name+" jigsaw actually places");
            var sourceEntities=template.save(new CompoundTag()).getListOrEmpty("entities").compoundStream().toList();
            check(helper, !sourceEntities.isEmpty(), name+" template contains entity NBT");
            for(var source : sourceEntities) {
                var loaded=EntityType.create(TagValueInput.create(ProblemReporter.DISCARDING, registry,
                    source.getCompoundOrEmpty("nbt")),level,EntitySpawnReason.STRUCTURE).orElseThrow();
                check(helper, loaded instanceof Mob mob && mob.isPersistenceRequired(), name+" entity NBT decodes to a persistent mob");
                loaded.discard();
            }
        }
        // Newly generated chunk entity sections become queryable after the server advances.
        helper.runAfterDelay(2, () -> {
            for(int index=0;index<StructureContent.STRUCTURES.size();index++) {
                String name=StructureContent.STRUCTURES.get(index);
                BlockPos anchor=helper.absolutePos(new BlockPos(11+index*20,2,11));
                var inhabitants = level.getEntitiesOfClass(Mob.class,
                    AABB.encapsulatingFullBlocks(anchor.offset(-9,-1,-9), anchor.offset(9,18,9)));
                check(helper, inhabitants.stream().allMatch(Mob::isPersistenceRequired), name+" inhabitants persist between visits");
                Set<String> actual = inhabitants.stream()
                    .map(mob -> BuiltInRegistries.ENTITY_TYPE.getKey(mob.getType()))
                    .filter(key -> key.getNamespace().equals(MythicRealmsCreatures.MOD_ID))
                    .map(ResourceLocation::getPath).collect(Collectors.toSet());
                check(helper, actual.containsAll(expected.get(index)), name+" persistent inhabitants spawn: "+actual);
                int containers=0;
                for (BlockPos pos : BlockPos.betweenClosed(anchor.offset(-9,-1,-9), anchor.offset(9,18,9))) {
                    if (level.getBlockEntity(pos) instanceof RandomizableContainerBlockEntity chest) {
                        containers++;
                        var key=chest.getLootTable();
                        check(helper, key!=null && key.location().equals(id("chests/"+name)), name+" chest retains its loot reference");
                        check(helper, level.getServer().reloadableRegistries().getLootTable(key)!=LootTable.EMPTY, name+" loot table loaded");
                        chest.unpackLootTable(null);
                        check(helper, !chest.isEmpty(), name+" chest generates usable items");
                    }
                }
                check(helper, containers>0, name+" contains an accessible loot container");
                level.getEntitiesOfClass(Mob.class, AABB.encapsulatingFullBlocks(anchor.offset(-9,-1,-9), anchor.offset(9,18,9)))
                    .forEach(Mob::discard);
            }
            helper.succeed();
        });
    }

    @GameTest
    public void structureResourceConditionHonorsGlobalAndIndividualSettings(GameTestHelper helper) {
        var config = CreatureConfig.INSTANCE;
        boolean previousGlobal=config.structuresEnabled;
        Boolean previousIndividual=config.structures.get("goblin_watchtower");
        try {
            var condition=ResourceCondition.CODEC.parse(JsonOps.INSTANCE, JsonParser.parseString(
                "{\"condition\":\"mythic_realms_creatures:structure_enabled\",\"structure\":\"goblin_watchtower\"}")).getOrThrow();
            config.structuresEnabled=true;
            config.structures.put("goblin_watchtower",true);
            check(helper, condition.test(null), "enabled structure set loads");
            config.structures.put("goblin_watchtower",false);
            check(helper, !condition.test(null), "individual disable excludes structure set");
            config.structures.put("goblin_watchtower",true);
            config.structuresEnabled=false;
            check(helper, !condition.test(null), "global disable excludes structure set");
            check(helper, !new StructureContent.Enabled("unknown").test(null), "unknown IDs fail closed");
        } finally {
            config.structuresEnabled=previousGlobal;
            if(previousIndividual==null) config.structures.remove("goblin_watchtower");
            else config.structures.put("goblin_watchtower",previousIndividual);
        }
        helper.succeed();
    }
}
