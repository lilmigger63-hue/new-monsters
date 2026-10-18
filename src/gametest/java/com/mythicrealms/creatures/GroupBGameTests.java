package com.mythicrealms.creatures;

import com.mythicrealms.creatures.config.CreatureConfig;
import com.mythicrealms.creatures.entity.*;
import com.mythicrealms.creatures.entity.mount.*;
import com.mythicrealms.creatures.registry.ModEntities;
import net.fabricmc.fabric.api.gametest.v1.GameTest;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.gametest.framework.GameTestHelper;
import net.minecraft.network.chat.Component;
import net.minecraft.util.ProblemReporter;
import net.minecraft.world.*;
import net.minecraft.world.entity.*;
import net.minecraft.world.entity.player.Input;
import net.minecraft.world.item.*;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.level.storage.*;
import net.minecraft.world.phys.Vec3;

public final class GroupBGameTests {
    private void floor(GameTestHelper h) {
        for (int x=0;x<8;x++) for (int z=0;z<8;z++) h.setBlock(x,1,z,Blocks.GRASS_BLOCK);
    }
    private void check(GameTestHelper h, boolean condition, String message) { h.assertTrue(condition, Component.literal(message)); }
    @GameTest
    public void groupBRegistersAttributesEggsAndLoot(GameTestHelper h) {
        floor(h);
        var types=java.util.List.of(ModEntities.ANCIENT_TREANT,ModEntities.FOREST_DRYAD,ModEntities.GRIFFIN,ModEntities.DIRE_WOLF,ModEntities.WILD_WYVERN);
        for (var type:types) {
            var mob=h.spawn(type,3,2,3);mob.setNoAi(true);
            var kind=((MythicCreature)mob).kind();
            check(h,mob.getMaxHealth()==kind.health,"species health");
            check(h,BuiltInRegistries.ITEM.getValue(ModEntities.id(kind.id+"_spawn_egg")) instanceof SpawnEggItem,"egg registered");
            check(h,h.getLevel().getServer().reloadableRegistries().getLootTable(type.getDefaultLootTable().orElseThrow())
                != net.minecraft.world.level.storage.loot.LootTable.EMPTY,"loot loaded");
            mob.discard();
        }
        h.succeed();
    }
    @GameTest(maxTicks=50)
    public void treantRootDamagesAndSlowsHostile(GameTestHelper h) {
        floor(h);
        var treant=h.spawn(ModEntities.ANCIENT_TREANT,2,2,2);treant.setNoAi(true);
        var hostile=h.spawn(ModEntities.ORC_WARRIOR,5,2,2);hostile.setNoAi(true);
        float health=hostile.getHealth();
        treant.performAttack(h.getLevel(),hostile);
        h.runAfterDelay(16,()->{
            check(h,hostile.getHealth()<health,"root hits hostile");
            check(h,hostile.hasEffect(net.minecraft.world.effect.MobEffects.SLOWNESS),"roots apply slow");
            h.succeed();
        });
    }
    @GameTest(maxTicks=40)
    public void dryadHealsFriendlyTargetAfterCast(GameTestHelper h) {
        floor(h);
        var dryad=h.spawn(ModEntities.FOREST_DRYAD,2,2,2);
        var treant=h.spawn(ModEntities.ANCIENT_TREANT,4,2,2);treant.setNoAi(true);treant.setHealth(20);
        check(h,dryad.beginHealing(treant),"healing begins for wounded ally");
        h.runAfterDelay(3,()->check(h,treant.getHealth()==20,"no healing before windup"));
        h.runAfterDelay(20,()->{
            check(h,treant.getHealth()>20,"heals after cast");h.succeed();
        });
    }
    @GameTest
    public void ownerSaddleStayAndRareVariantSurviveReload(GameTestHelper h) {
        floor(h);
        var owner=h.makeMockServerPlayerInLevel();owner.setGameMode(net.minecraft.world.level.GameType.SURVIVAL);
        var wyvern=h.spawn(ModEntities.WILD_WYVERN,3,2,3);wyvern.setNoAi(true);
        wyvern.setOwner(owner);wyvern.setTame(true,false);wyvern.setSaddled(true);wyvern.setRareVariant(true);
        wyvern.setOrderedToSit(true);wyvern.setInSittingPose(true);
        var output=TagValueOutput.createWithContext(ProblemReporter.DISCARDING,h.getLevel().registryAccess());
        wyvern.saveWithoutId(output);
        var clone=ModEntities.WILD_WYVERN.create(h.getLevel(),EntitySpawnReason.LOAD);
        clone.load(TagValueInput.create(ProblemReporter.DISCARDING,h.getLevel().registryAccess(),output.buildResult()));
        check(h,clone.isTame() && clone.getOwnerReference().getUUID().equals(owner.getUUID()),"owner persists");
        check(h,clone.isSaddled() && clone.isOrderedToSit() && clone.isRareVariant(),"mount state persists");
        check(h,!clone.canAttack(owner),"owner cannot be attacked");
        h.succeed();
    }
    @GameTest
    public void onlyRareWyvernsCanBeTamed(GameTestHelper h) {
        floor(h);
        var player=h.makeMockPlayer(net.minecraft.world.level.GameType.SURVIVAL);
        var wyvern=h.spawn(ModEntities.WILD_WYVERN,3,2,3);wyvern.setNoAi(true);wyvern.setRareVariant(false);
        player.setItemInHand(InteractionHand.MAIN_HAND,new ItemStack(Items.FERMENTED_SPIDER_EYE,3));
        int previous=CreatureConfig.INSTANCE.tamingDifficulty;CreatureConfig.INSTANCE.tamingDifficulty=1;
        try {
            wyvern.mobInteract(player,InteractionHand.MAIN_HAND);
            check(h,!wyvern.isTame(),"ordinary wyvern remains wild");
            wyvern.setRareVariant(true);
            wyvern.mobInteract(player,InteractionHand.MAIN_HAND);
            check(h,wyvern.isTame() && wyvern.getOwnerReference().getUUID().equals(player.getUUID()),"rare wyvern tames");
            check(h,player.getMainHandItem().getCount()==2,"only the valid taming attempt consumes food");
        } finally { CreatureConfig.INSTANCE.tamingDifficulty=previous; }
        h.succeed();
    }
    @GameTest
    public void ownedFlyingMountUsesServerInputs(GameTestHelper h) {
        floor(h);
        var rider=h.makeMockServerPlayerInLevel();
        var griffin=h.spawn(ModEntities.GRIFFIN,3,3,3);
        griffin.setOwner(rider);griffin.setTame(true,false);griffin.setSaddled(true);
        check(h,rider.startRiding(griffin,true,true),"owner can ride");
        rider.setLastClientInput(new Input(true,false,false,false,true,false,false));
        griffin.travel(Vec3.ZERO);
        check(h,griffin.isFlying() && griffin.getDeltaMovement().y>0,"space initiates bounded ascent");
        check(h,!griffin.isClientAuthoritative(),"server owns mount movement");
        check(h,griffin.getDeltaMovement().length()<1,"bounded velocity");
        rider.stopRiding();h.succeed();
    }
    @GameTest
    public void nonOwnerCannotControlOrFeedOwnersMount(GameTestHelper h) {
        floor(h);
        var owner=h.makeMockServerPlayerInLevel();owner.setGameMode(net.minecraft.world.level.GameType.SURVIVAL);
        var stranger=h.makeMockServerPlayerInLevel();
        var wolf=h.spawn(ModEntities.DIRE_WOLF,3,2,3);wolf.setNoAi(true);
        wolf.setOwner(owner);wolf.setTame(true,false);wolf.setSaddled(true);
        stranger.startRiding(wolf,true,true);
        check(h,wolf.getControllingPassenger()==null,"forced non-owner passenger gets no controls");
        stranger.stopRiding();
        stranger.setItemInHand(InteractionHand.MAIN_HAND,new ItemStack(Items.SADDLE));
        wolf.mobInteract(stranger,InteractionHand.MAIN_HAND);
        check(h,wolf.getOwnerReference().getUUID().equals(owner.getUUID()),"ownership unchanged");
        h.succeed();
    }
    @GameTest(maxTicks=35)
    public void flightRespondsDuringNormalServerTicks(GameTestHelper h) {
        floor(h);
        var rider=h.makeMockServerPlayerInLevel();
        var griffin=h.spawn(ModEntities.GRIFFIN,3,3,3);
        griffin.setOwner(rider);griffin.setTame(true,false);griffin.setSaddled(true);
        rider.startRiding(griffin,true,true);
        double initialY=griffin.getY();
        rider.setLastClientInput(new Input(false,false,false,false,true,false,false));
        h.runAfterDelay(6,()->{
            check(h,griffin.getY()>initialY+.2,"server ticks apply ascent input");
            rider.setLastClientInput(new Input(false,false,false,false,false,false,true));
        });
        h.runAfterDelay(19,()->{
            check(h,griffin.getDeltaMovement().y<0,"sprint input descends after acceleration");
            rider.stopRiding();h.succeed();
        });
    }

    @GameTest
    public void wildWyvernBecomesPassiveInPeaceful(GameTestHelper h) {
        floor(h);
        var player=h.makeMockPlayer(net.minecraft.world.level.GameType.SURVIVAL);
        var wyvern=h.spawn(ModEntities.WILD_WYVERN,3,2,3);wyvern.setNoAi(true);
        var server=h.getLevel().getServer();var previous=h.getLevel().getDifficulty();
        try {
            server.setDifficulty(Difficulty.NORMAL,true);
            check(h,wyvern.canAttack(player),"wild wyvern targets survival players before switching difficulty");
            server.setDifficulty(Difficulty.PEACEFUL,true);
            check(h,!wyvern.canAttack(player),"untamed wyvern cannot attack in Peaceful");
        } finally {server.setDifficulty(previous,true);}
        h.succeed();
    }

    @GameTest(maxTicks=25)
    public void direWolfMovesFromServerRiderInput(GameTestHelper h) {
        floor(h);
        var rider=h.makeMockServerPlayerInLevel();
        var wolf=h.spawn(ModEntities.DIRE_WOLF,3,2,3);
        wolf.setOwner(rider);wolf.setTame(true,false);wolf.setSaddled(true);
        rider.startRiding(wolf,true,true);rider.setYRot(0);
        double initialZ=wolf.getZ();
        rider.setLastClientInput(new Input(true,false,false,false,false,false,false));
        h.runAfterDelay(8,()->{
            check(h,wolf.getZ()>initialZ+.1,"ground mount follows server input");
            rider.stopRiding();h.succeed();
        });
    }
    @GameTest
    public void companionsNeverAttackSameOwnersPets(GameTestHelper h) {
        floor(h);
        var owner=h.makeMockServerPlayerInLevel();owner.setGameMode(net.minecraft.world.level.GameType.SURVIVAL);
        var wolf=h.spawn(ModEntities.DIRE_WOLF,2,2,2);wolf.setNoAi(true);
        var griffin=h.spawn(ModEntities.GRIFFIN,4,2,2);griffin.setNoAi(true);
        wolf.setOwner(owner);wolf.setTame(true,false);griffin.setOwner(owner);griffin.setTame(true,false);
        check(h,!wolf.canAttack(owner) && !wolf.canAttack(griffin) && !griffin.canAttack(wolf),"owner and companion safety");
        h.succeed();
    }

}
