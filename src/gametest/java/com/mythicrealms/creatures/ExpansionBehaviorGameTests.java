package com.mythicrealms.creatures;

import com.mythicrealms.creatures.entity.*;
import com.mythicrealms.creatures.entity.expansion.*;
import com.mythicrealms.creatures.registry.ModEntities;
import java.util.List;
import net.fabricmc.fabric.api.gametest.v1.GameTest;
import net.minecraft.core.BlockPos;
import net.minecraft.gametest.framework.GameTestHelper;
import net.minecraft.network.chat.Component;
import net.minecraft.world.effect.MobEffects;
import net.minecraft.world.entity.*;
import net.minecraft.world.entity.ai.navigation.AmphibiousPathNavigation;
import net.minecraft.world.level.block.Blocks;

/** Server effects exercise inherited behavior; no reflection or mocked combat. */
public final class ExpansionBehaviorGameTests {
    private void check(GameTestHelper h, boolean value, String message) {
        h.assertTrue(value, Component.literal(message));
    }
    private void floor(GameTestHelper h) {
        for (int x=0;x<8;x++) for (int z=0;z<8;z++) h.setBlock(x,1,z,Blocks.STONE);
    }
    private net.minecraft.world.entity.animal.IronGolem victim(GameTestHelper h) {
        var target=h.spawn(EntityType.IRON_GOLEM,5,2,3);
        target.setNoAi(true);
        return target;
    }

    @GameTest public void allThirteenSpeciesUseTheirRequestedInheritedProfiles(GameTestHelper h) {
        var groups=List.of(
            List.<EntityType<?>>of(ModEntities.VAMPIRE,ModEntities.CENTAUR,ModEntities.SAHUAGIN,ModEntities.VALKYRIE,
                ModEntities.ANUBIS,ModEntities.KOBOLD,ModEntities.CYCLOPS,ModEntities.DHAMPIR),
            List.<EntityType<?>>of(ModEntities.FOX_SPIRIT_GIRL,ModEntities.WERECAT),
            List.<EntityType<?>>of(ModEntities.HOLSTAURUS),
            List.<EntityType<?>>of(ModEntities.ENDER_DRAGON_GIRL,ModEntities.SUCCUBUS));
        var profiles=List.of(AiProfile.SCOUT,AiProfile.SHAMAN,AiProfile.SLIME,AiProfile.DEMON);
        int count=0;
        for (int i=0;i<groups.size();i++) for (var type:groups.get(i)) {
            var entity=type.create(h.getLevel(),EntitySpawnReason.COMMAND);
            check(h,entity instanceof ProfiledCreature,"species is profile-backed: "+type);
            var creature=(ProfiledCreature)entity;
            check(h,creature.aiProfile()==profiles.get(i),"requested profile: "+type);
            check(h,switch (profiles.get(i)) {
                case SCOUT -> entity instanceof GoblinScoutEntity;
                case SHAMAN -> entity instanceof GoblinShamanEntity;
                case SLIME -> entity instanceof SlimeMaidenEntity;
                case DEMON -> entity instanceof DemonSorceressEntity;
            },"inherits original behavior implementation: "+type);
            check(h,creature.attackRange()==creature.kind().range,"species range is live configuration: "+type);
            entity.discard();
            count++;
        }
        check(h,count==13,"all thirteen mappings checked");
        h.succeed();
    }

    @GameTest(maxTicks=30) public void vampireMeleeWaitsForWindupAndLocksRecovery(GameTestHelper h) {
        floor(h);
        var vampire=h.spawn(ModEntities.VAMPIRE,3,2,3);
        vampire.removeAllGoals(goal -> true);
        var target=victim(h);
        target.setPos(vampire.getX()+1.2,vampire.getY(),vampire.getZ());
        float health=target.getHealth();
        check(h,vampire.tryAttack(target),"vampire starts inherited timeline");
        h.runAfterDelay(2,()->check(h,target.getHealth()==health,"windup cannot deal early melee damage"));
        h.runAfterDelay(12,()->{
            check(h,target.getHealth()<health,"server releases vampire melee after windup");
            check(h,!vampire.tryAttack(target),"inherited recovery prevents immediate second attack");
            h.succeed();
        });
    }

    @GameTest(maxTicks=35) public void foxSpiritShamanBoltDamagesAndIgnites(GameTestHelper h) {
        floor(h);
        var fox=h.spawn(ModEntities.FOX_SPIRIT_GIRL,1,2,3);fox.setNoAi(true);
        var target=victim(h);
        fox.performAttack(h.getLevel(),target);
        h.runAfterDelay(18,()->{
            check(h,target.getHealth()<target.getMaxHealth(),"fox shaman projectile hits");
            check(h,target.isOnFire(),"fox retains original shaman fire effect");
            h.succeed();
        });
    }

    @GameTest(maxTicks=35) public void succubusDemonBoltAppliesBothCurses(GameTestHelper h) {
        floor(h);
        var succubus=h.spawn(ModEntities.SUCCUBUS,1,2,3);succubus.setNoAi(true);
        var target=victim(h);
        // Exactly four blocks avoids the close-range teleport branch.
        target.setPos(succubus.getX()+4,succubus.getY(),succubus.getZ());
        succubus.performAttack(h.getLevel(),target);
        h.runAfterDelay(18,()->{
            check(h,target.getHealth()<target.getMaxHealth(),"succubus dark bolt hits");
            check(h,target.hasEffect(MobEffects.WEAKNESS) && target.hasEffect(MobEffects.DARKNESS),
                "succubus retains original demon weakness and darkness");
            h.succeed();
        });
    }

    @GameTest(maxTicks=35) public void holstaurusBubbleSlowsAndDamagesHostileTarget(GameTestHelper h) {
        floor(h);
        var holstaurus=h.spawn(ModEntities.HOLSTAURUS,1,2,3);holstaurus.setNoAi(true);
        var target=h.spawn(EntityType.HUSK,5,2,3);target.setNoAi(true);
        holstaurus.performAttack(h.getLevel(),target);
        h.runAfterDelay(18,()->{
            check(h,target.getHealth()<target.getMaxHealth(),"holstaurus slime bubble damages hostile");
            check(h,target.hasEffect(MobEffects.SLOWNESS),"holstaurus retains slime slow");
            check(h,!holstaurus.canAttack(h.spawn(ModEntities.SLIME_MAIDEN,6,2,5)),"guardian profile protects fellow guardians");
            h.succeed();
        });
    }

    @GameTest(maxTicks=55) public void holstaurusRetainsPeriodicSlimeHop(GameTestHelper h) {
        floor(h);
        var holstaurus=h.spawn(ModEntities.HOLSTAURUS,3,2,3);
        holstaurus.removeAllGoals(goal -> true);
        double groundY=holstaurus.getY();
        boolean[] hopped={false};
        h.onEachTick(()->{
            if (holstaurus.tickCount>=35 && holstaurus.getY()>groundY+.15) hopped[0]=true;
        });
        h.runAfterDelay(46,()->{
            check(h,hopped[0],"original 35-tick server hop lifts holstaurus off the ground without a target");
            h.succeed();
        });
    }

    @GameTest(maxTicks=100) public void sahuaginNavigatesUnderwaterAndKeepsAirAndHealth(GameTestHelper h) {
        floor(h);
        // Bounded four-block-deep source-water tank, with a fully submerged route.
        for (int y=2;y<=6;y++) for (int x=0;x<8;x++) for (int z=0;z<8;z++)
            h.setBlock(x,y,z,(x==0 || x==7 || z==0 || z==7 || y==6)?Blocks.GLASS:Blocks.WATER);
        var sahuagin=h.spawn(ModEntities.SAHUAGIN,2,2,3);
        sahuagin.removeAllGoals(goal -> true);
        sahuagin.setAirSupply(0);
        float health=sahuagin.getHealth();
        var destination=net.minecraft.world.phys.Vec3.atBottomCenterOf(h.absolutePos(new BlockPos(5,3,3)));
        double initialDistance=sahuagin.position().distanceTo(destination);
        h.runAfterDelay(2,()->{
            check(h,sahuagin.isInWater(),"test creature is submerged in real water");
            check(h,sahuagin.getNavigation() instanceof AmphibiousPathNavigation,"amphibious navigation is installed");
            var path=sahuagin.getNavigation().createPath(h.absolutePos(new BlockPos(5,3,3)),0);
            check(h,path!=null && path.canReach(),"underwater destination has a reachable real path");
            check(h,sahuagin.getNavigation().moveTo(path,1),"underwater navigation starts");
        });
        h.runAfterDelay(40,()->check(h,sahuagin.position().distanceTo(destination)<initialDistance-.15,
            "server swimming approaches underwater destination without overshooting; position="+sahuagin.position()));
        h.runAfterDelay(82,()->{
            check(h,sahuagin.isInWater(),"creature remains in tank throughout breathing check");
            check(h,sahuagin.getAirSupply()>0,"air recovers from zero underwater");
            check(h,sahuagin.getHealth()==health,"submerged sahuagin takes no drowning damage over eighty ticks");
            h.succeed();
        });
    }

    @GameTest(maxTicks=45) public void sahuaginAlsoNavigatesOnDryLand(GameTestHelper h) {
        floor(h);
        var sahuagin=h.spawn(ModEntities.SAHUAGIN,2,2,3);
        sahuagin.removeAllGoals(goal -> true);
        double initialX=sahuagin.getX();
        h.runAfterDelay(2,()->{
            var destination=h.absolutePos(new BlockPos(5,2,3));
            var path=sahuagin.getNavigation().createPath(destination,0);
            check(h,path!=null && path.canReach(),"amphibious navigator finds dry land path");
            check(h,sahuagin.getNavigation().moveTo(path,1),"dry land navigation starts");
        });
        h.runAfterDelay(32,()->{
            check(h,!sahuagin.isInWater(),"land movement test is dry");
            check(h,sahuagin.getX()>initialX+.15,"server land travel advances along path");
            h.succeed();
        });
    }
}
