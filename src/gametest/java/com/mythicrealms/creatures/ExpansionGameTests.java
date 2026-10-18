package com.mythicrealms.creatures;

import com.mythicrealms.creatures.entity.CreatureKind;
import com.mythicrealms.creatures.registry.ModEntities;
import net.fabricmc.fabric.api.gametest.v1.GameTest;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.core.registries.Registries;
import net.minecraft.gametest.framework.GameTestHelper;
import net.minecraft.network.chat.Component;
import net.minecraft.world.entity.EntitySpawnReason;
import net.minecraft.world.entity.Mob;
import net.minecraft.world.entity.MobCategory;
import net.minecraft.world.item.SpawnEggItem;
import java.util.Set;
import java.util.HashSet;

public final class ExpansionGameTests {
    private static final Set<String> NEW_IDS=Set.of("ender_dragon_girl","vampire","holstaurus","centaur",
            "sahuagin","valkyrie","fox_spirit_girl","anubis","kobold","cyclops","dhampir","succubus","werecat");
    private void check(GameTestHelper h,boolean condition,String message){h.assertTrue(condition,Component.literal(message));}

    @GameTest public void onlyTwoOriginalSpeciesRemainInNaturalBiomeTables(GameTestHelper h){
        Set<String> found=new HashSet<>();
        Set<String> added=new HashSet<>();
        var biomes=h.getLevel().registryAccess().lookupOrThrow(Registries.BIOME);
        for(var biome:biomes)for(var category:MobCategory.values())
            for(var weighted:biome.getMobSettings().getMobs(category).unwrap()){
                var id=BuiltInRegistries.ENTITY_TYPE.getKey(weighted.value().type());
                if(id.getNamespace().equals(MythicRealmsCreatures.MOD_ID)){
                    if(NEW_IDS.contains(id.getPath()))added.add(id.getPath());
                    else found.add(id.getPath());
                }
            }
        check(h,found.equals(Set.of("forest_dryad","slime_maiden")),"original natural spawns must be exactly Dryad+Slime, got "+found);
        check(h,added.equals(NEW_IDS),"all thirteen new species appear in natural biome tables: "+added);
        h.succeed();
    }

    @GameTest public void thirteenNewSpeciesHaveIndependentTypesAndSpawnEggs(GameTestHelper h){
        for(String id:NEW_IDS){
            var key=ModEntities.id(id);var type=BuiltInRegistries.ENTITY_TYPE.getValue(key);
            check(h,key.equals(BuiltInRegistries.ENTITY_TYPE.getKey(type)),"new species registered: "+id);
            var entity=type.create(h.getLevel(),EntitySpawnReason.COMMAND);
            check(h,entity instanceof Mob,"new species creates a mob: "+id);
            check(h,BuiltInRegistries.ITEM.getValue(ModEntities.id(id+"_spawn_egg")) instanceof SpawnEggItem,"new species egg: "+id);
            var item=BuiltInRegistries.ITEM.getValue(ModEntities.id(id+"_spawn_egg"));
            check(h,((SpawnEggItem)item).getType(item.getDefaultInstance())==type,"egg resolves correct species: "+id);
            entity.discard();
        }
        h.succeed();
    }

    @GameTest public void allOriginalSpeciesStillAllowManualCreation(GameTestHelper h){
        int original=0;
        for(var kind:CreatureKind.values()){
            if(NEW_IDS.contains(kind.id))continue;
            original++;
            var entity=BuiltInRegistries.ENTITY_TYPE.getValue(ModEntities.id(kind.id)).create(h.getLevel(),EntitySpawnReason.COMMAND);
            check(h,entity instanceof Mob,"manual original mob: "+kind.id);
            check(h,BuiltInRegistries.ITEM.getValue(ModEntities.id(kind.id+"_spawn_egg")) instanceof SpawnEggItem,"original egg: "+kind.id);
            var egg=(SpawnEggItem)BuiltInRegistries.ITEM.getValue(ModEntities.id(kind.id+"_spawn_egg"));
            check(h,egg.getType(egg.getDefaultInstance())==entity.getType(),"original egg type preserved: "+kind.id);
            entity.discard();
        }
        check(h,original==20,"twenty original entity IDs preserved");h.succeed();
    }
}
