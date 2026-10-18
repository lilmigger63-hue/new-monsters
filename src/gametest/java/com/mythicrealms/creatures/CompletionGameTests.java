package com.mythicrealms.creatures;

import com.mythicrealms.creatures.entity.*;
import com.mythicrealms.creatures.registry.ModEntities;
import net.fabricmc.fabric.api.gametest.v1.GameTest;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.gametest.framework.GameTestHelper;
import net.minecraft.network.chat.Component;
import net.minecraft.world.entity.*;
import net.minecraft.world.effect.MobEffects;
import net.minecraft.world.item.SpawnEggItem;
import net.minecraft.world.level.block.Blocks;

public final class CompletionGameTests {
    private void floor(GameTestHelper h){for(int x=0;x<8;x++)for(int z=0;z<8;z++)h.setBlock(x,1,z,Blocks.STONE);}
    private void check(GameTestHelper h,boolean value,String text){h.assertTrue(value,Component.literal(text));}
    @GameTest public void allTwentySpeciesHaveEggsAttributesAndLoadedLoot(GameTestHelper h){
        floor(h);check(h,CreatureKind.values().length==20,"exactly twenty species");
        for(var kind:CreatureKind.values()){
            var type=BuiltInRegistries.ENTITY_TYPE.getValue(ModEntities.id(kind.id));
            var entity=type.create(h.getLevel(),EntitySpawnReason.COMMAND);
            check(h,entity instanceof Mob,"registered mob: "+kind.id);
            var mob=(Mob)entity;
            check(h,mob.getMaxHealth()>0,"attributes: "+kind.id);
            check(h,BuiltInRegistries.ITEM.getValue(ModEntities.id(kind.id+"_spawn_egg")) instanceof SpawnEggItem,"egg: "+kind.id);
            check(h,h.getLevel().getServer().reloadableRegistries().getLootTable(type.getDefaultLootTable().orElseThrow())
                !=net.minecraft.world.level.storage.loot.LootTable.EMPTY,"loaded loot: "+kind.id);
            mob.discard();
        }h.succeed();
    }
    @GameTest public void basiliskGazeSlowsTarget(GameTestHelper h){
        floor(h);var mob=h.spawn(ModEntities.CAVE_BASILISK,2,2,2);mob.setNoAi(true);
        var target=h.spawn(EntityType.COW,4,2,2);target.setNoAi(true);
        mob.performAttack(h.getLevel(),target);
        check(h,target.hasEffect(MobEffects.SLOWNESS),"petrifying gaze applies slow");h.succeed();
    }
    @GameTest(maxTicks=40) public void crystalProjectileCreatesTimedWeb(GameTestHelper h){
        floor(h);var mob=h.spawn(ModEntities.CRYSTAL_SPIDER,2,2,2);mob.setNoAi(true);
        var target=h.spawn(EntityType.IRON_GOLEM,5,2,2);target.setNoAi(true);
        mob.performAttack(h.getLevel(),target);
        h.runAfterDelay(18,()->{
            check(h,target.getHealth()<target.getMaxHealth(),"crystal hit damages");
            check(h,!h.getLevel().getEntitiesOfClass(com.mythicrealms.creatures.magic.WebTrapEntity.class,target.getBoundingBox().inflate(3)).isEmpty(),"web trap exists");h.succeed();
        });
    }
    @GameTest public void graveKnightComboHasHeavyFinisher(GameTestHelper h){
        floor(h);var knight=h.spawn(ModEntities.GRAVE_KNIGHT,2,2,2);knight.setNoAi(true);
        var target=h.spawn(EntityType.IRON_GOLEM,3,2,2);target.setNoAi(true);
        float health=target.getHealth();knight.performAttack(h.getLevel(),target);float first=health-target.getHealth();
        target.invulnerableTime=0;knight.performAttack(h.getLevel(),target);
        target.invulnerableTime=0;health=target.getHealth();knight.performAttack(h.getLevel(),target);
        check(h,health-target.getHealth()>first,"third strike is stronger");h.succeed();
    }
    @GameTest public void frostWaveSlowsEnemies(GameTestHelper h){
        floor(h);var elemental=h.spawn(ModEntities.FROST_ELEMENTAL,2,2,2);elemental.setNoAi(true);
        var target=h.spawn(EntityType.COW,4,2,2);target.setNoAi(true);
        elemental.performAttack(h.getLevel(),target);check(h,target.hasEffect(MobEffects.SLOWNESS),"frost wave slows");h.succeed();
    }
    @GameTest public void moonStagIsGroundMountAndCanOwnPlayer(GameTestHelper h){
        floor(h);var player=h.makeMockServerPlayerInLevel();var stag=h.spawn(ModEntities.MOON_STAG,3,2,3);stag.setNoAi(true);
        stag.setOwner(player);stag.setTame(true,false);stag.setSaddled(true);
        check(h,!stag.canFly(),"stag is ground mount");check(h,player.startRiding(stag,true,true),"stag can carry owner");
        check(h,!stag.canAttack(player),"owner safe");player.stopRiding();h.succeed();
    }
    @GameTest(maxTicks=30) public void allNewSpeciesTickWithoutAiAttributeFailures(GameTestHelper h){
        floor(h);
        for(var type:java.util.List.of(ModEntities.CAVE_BASILISK,ModEntities.CRYSTAL_SPIDER,ModEntities.SHADOW_WRAITH,
            ModEntities.GRAVE_KNIGHT,ModEntities.FLAME_IMP,ModEntities.FROST_ELEMENTAL,ModEntities.MOON_STAG,
            ModEntities.SLIME_MAIDEN,ModEntities.HARPY,ModEntities.DEMON_SORCERESS))h.spawn(type,3,2,3);
        h.runAfterDelay(22,h::succeed);
    }
    @GameTest(maxTicks=35) public void frostUsesIceProjectileBeyondNovaReach(GameTestHelper h){
        floor(h);var elemental=h.spawn(ModEntities.FROST_ELEMENTAL,1,2,2);elemental.setNoAi(true);
        var target=h.spawn(EntityType.IRON_GOLEM,7,2,2);target.setNoAi(true);
        elemental.performAttack(h.getLevel(),target);
        h.runAfterDelay(18,()->{check(h,target.hasEffect(MobEffects.SLOWNESS),"midrange ice spike hits instead of unreachable nova");h.succeed();});
    }
    @GameTest public void webTrapCanBeTargetedAndBroken(GameTestHelper h){
        var web=h.spawn(ModEntities.WEB_TRAP,3,2,3);
        check(h,web.isPickable(),"players can aim attacks at web");
        web.hurtServer(h.getLevel(),web.damageSources().generic(),1);
        check(h,web.isRemoved(),"damage clears temporary web");h.succeed();
    }

    @GameTest public void naturalSpawnEntriesResolveInEachConfiguredHabitat(GameTestHelper h){
        var biomes=h.getLevel().registryAccess().lookupOrThrow(net.minecraft.core.registries.Registries.BIOME);
        for(var kind:CreatureKind.values()) {
            var type=BuiltInRegistries.ENTITY_TYPE.getValue(ModEntities.id(kind.id));
            var tag=net.minecraft.tags.TagKey.create(net.minecraft.core.registries.Registries.BIOME,ModEntities.id("spawns/"+kind.id));
            var tagged=biomes.get(tag).orElseThrow();
            check(h,tagged.size()>0,"habitat tag resolves: "+kind.id);
            var rule=com.mythicrealms.creatures.config.CreatureConfig.INSTANCE.spawning.get(kind.id);
            boolean entry=tagged.stream().anyMatch(holder -> holder.value().getMobSettings().getMobs(type.getCategory()).unwrap().stream()
                .anyMatch(weighted -> weighted.value().type()==type && weighted.weight()==rule.weight
                    && weighted.value().minCount()==rule.minGroup && weighted.value().maxCount()==rule.maxGroup));
            check(h,entry,"natural biome spawn entry: "+kind.id);
            var position=h.absolutePos(new net.minecraft.core.BlockPos(3,2,3));
            var blocked=(kind==CreatureKind.FLAME_IMP || kind==CreatureKind.DEMON_SORCERESS)?h.getLevel():
                h.getLevel().getServer().getLevel(net.minecraft.world.level.Level.NETHER);
            check(h,!net.minecraft.world.entity.SpawnPlacements.checkSpawnRules(type,blocked,EntitySpawnReason.NATURAL,position,blocked.random),
                "dimension restriction rejects wrong dimension: "+kind.id);
        }
        h.succeed();
    }

    @GameTest(maxTicks=40) public void darkFireAndSlimeMagicApplyTheirDistinctEffects(GameTestHelper h){
        floor(h);
        var wraith=h.spawn(ModEntities.SHADOW_WRAITH,1,2,1);wraith.setNoAi(true);
        var imp=h.spawn(ModEntities.FLAME_IMP,1,2,4);imp.setNoAi(true);
        var slime=h.spawn(ModEntities.SLIME_MAIDEN,1,2,7);slime.setNoAi(true);
        var cursed=h.spawn(EntityType.IRON_GOLEM,6,2,1);cursed.setNoAi(true);
        var burning=h.spawn(EntityType.IRON_GOLEM,6,2,4);burning.setNoAi(true);
        var slowed=h.spawn(EntityType.IRON_GOLEM,6,2,7);slowed.setNoAi(true);
        wraith.performAttack(h.getLevel(),cursed);imp.performAttack(h.getLevel(),burning);slime.performAttack(h.getLevel(),slowed);
        h.runAfterDelay(20,()->{
            check(h,cursed.hasEffect(MobEffects.WEAKNESS) && cursed.hasEffect(MobEffects.DARKNESS),"dark magic applies curse");
            check(h,burning.isOnFire(),"imp projectile ignites target");
            check(h,slowed.hasEffect(MobEffects.SLOWNESS),"slime bubble slows target");h.succeed();
        });
    }

}
