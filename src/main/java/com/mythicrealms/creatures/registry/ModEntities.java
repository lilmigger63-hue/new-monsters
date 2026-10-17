package com.mythicrealms.creatures.registry;

import com.mythicrealms.creatures.MythicRealmsCreatures;
import com.mythicrealms.creatures.config.CreatureConfig;
import com.mythicrealms.creatures.entity.*;
import net.fabricmc.fabric.api.biome.v1.*;
import net.fabricmc.fabric.api.itemgroup.v1.ItemGroupEvents;
import net.fabricmc.fabric.api.object.builder.v1.entity.FabricEntityType;
import net.minecraft.core.Registry;
import net.minecraft.core.registries.*;
import net.minecraft.resources.*;
import net.minecraft.tags.TagKey;
import net.minecraft.world.entity.*;
import net.minecraft.world.entity.monster.Monster;
import net.minecraft.world.item.*;
import net.minecraft.world.level.biome.Biome;
import net.minecraft.world.level.levelgen.Heightmap;

public final class ModEntities {
    public static final EntityType<GoblinScoutEntity> GOBLIN_SCOUT = creature(CreatureKind.GOBLIN_SCOUT, GoblinScoutEntity::new);
    public static final EntityType<GoblinShamanEntity> GOBLIN_SHAMAN = creature(CreatureKind.GOBLIN_SHAMAN, GoblinShamanEntity::new);
    public static final EntityType<OrcWarriorEntity> ORC_WARRIOR = creature(CreatureKind.ORC_WARRIOR, OrcWarriorEntity::new);
    public static final EntityType<MinotaurEntity> MINOTAUR = creature(CreatureKind.MINOTAUR, MinotaurEntity::new);
    public static final EntityType<StoneTrollEntity> STONE_TROLL = creature(CreatureKind.STONE_TROLL, StoneTrollEntity::new);
    public static final EntityType<CreatureProjectile> SHAMAN_BOLT = projectile("shaman_bolt", .25f);
    public static final EntityType<CreatureProjectile> TROLL_BOULDER = projectile("troll_boulder", .55f);

    public static ResourceLocation id(String path) { return ResourceLocation.fromNamespaceAndPath(MythicRealmsCreatures.MOD_ID, path); }
    private static <T extends MythicHostileEntity> EntityType<T> creature(CreatureKind kind, EntityType.EntityFactory<T> factory) {
        var key = ResourceKey.create(Registries.ENTITY_TYPE, id(kind.id));
        var rule = CreatureConfig.INSTANCE.spawning.get(kind.id);
        var builder = FabricEntityType.Builder.createMob(factory, MobCategory.MONSTER, extra -> extra
            .defaultAttributes(() -> kind.attributes(CreatureConfig.INSTANCE.difficultyMultiplier))
            .spawnRestriction(SpawnPlacementTypes.ON_GROUND, Heightmap.Types.MOTION_BLOCKING_NO_LEAVES,
                (type, level, reason, pos, random) -> rule.enabled && random.nextInt(rule.frequency) == 0
                    && (kind != CreatureKind.STONE_TROLL || pos.getY() < level.getLevel().getSeaLevel() - 8)
                    && Monster.checkMonsterSpawnRules(type, level, reason, pos, random)));
        var type = Registry.register(BuiltInRegistries.ENTITY_TYPE, key,
            builder.sized(kind.width, kind.height).clientTrackingRange(8).build(key));
        var itemKey = ResourceKey.create(Registries.ITEM, id(kind.id + "_spawn_egg"));
        Item egg = Registry.register(BuiltInRegistries.ITEM, itemKey,
            new SpawnEggItem(new Item.Properties().setId(itemKey).spawnEgg(type)));
        ItemGroupEvents.modifyEntriesEvent(CreativeModeTabs.SPAWN_EGGS).register(entries -> entries.accept(egg));
        if (rule.enabled && rule.weight > 0) {
            TagKey<Biome> tag = TagKey.create(Registries.BIOME, id("spawns/" + kind.id));
            BiomeModifications.addSpawn(BiomeSelectors.tag(tag), MobCategory.MONSTER, type,
                rule.weight, rule.minGroup, rule.maxGroup);
        }
        return type;
    }
    private static EntityType<CreatureProjectile> projectile(String name, float size) {
        var key = ResourceKey.create(Registries.ENTITY_TYPE, id(name));
        return Registry.register(BuiltInRegistries.ENTITY_TYPE, key,
            EntityType.Builder.<CreatureProjectile>of(CreatureProjectile::new, MobCategory.MISC)
                .sized(size, size).clientTrackingRange(6).updateInterval(2).build(key));
    }
    public static void initialize() { }
}
