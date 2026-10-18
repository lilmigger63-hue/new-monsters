package com.mythicrealms.creatures.entity;

import com.mythicrealms.creatures.entity.mount.MythicMountEntity;
import net.minecraft.world.entity.LivingEntity;
import software.bernie.geckolib.animatable.GeoEntity;
import software.bernie.geckolib.animatable.manager.AnimatableManager;
import software.bernie.geckolib.animatable.processing.AnimationController;
import software.bernie.geckolib.animation.*;

public interface MythicCreature extends GeoEntity {
    CreatureKind kind();
    RawAnimation DEATH_ANIMATION=RawAnimation.begin().thenPlayAndHold("death");
    java.util.Map<String,RawAnimation> LOOPS=java.util.stream.Stream.of("idle","walk","run","fly","hover","sit","ride","jump","guard","charge","sneak","levitate","swim","idle_swim","hop")
        .collect(java.util.stream.Collectors.toUnmodifiableMap(name->name,name->RawAnimation.begin().thenLoop(name)));
    static RawAnimation loop(String name){return LOOPS.get(name);}
    @Override default void registerControllers(AnimatableManager.ControllerRegistrar controllers) {
        controllers.add(new AnimationController<MythicCreature>("locomotion",5,test -> {
            var entity=(LivingEntity)test.animatable();
            String state="idle";
            if (entity.isDeadOrDying()) return test.setAndContinue(DEATH_ANIMATION);
            if (entity instanceof MythicMountEntity mount) {
                if (mount.isInSittingPose()) state="sit";
                else if (mount.isFlying()) state=test.isMoving()?"fly":"hover";
                else if (!mount.onGround() && !mount.canFly() && Math.abs(mount.getDeltaMovement().y)>.08) state="jump";
                else if (test.isMoving()) state=mount.isVehicle()?"ride":mount.getDeltaMovement().horizontalDistanceSqr()>.01?"run":"walk";
            } else if (test.isMoving()) state=entity.getDeltaMovement().horizontalDistanceSqr()>.01?"run":"walk";
            return test.setAndContinue(loop(state));
        }));
        var action=new AnimationController<MythicCreature>("action",2,test -> PlayState.STOP)
            .triggerableAnim("attack",RawAnimation.begin().thenPlay("attack"))
            .triggerableAnim("cast",RawAnimation.begin().thenPlay("cast"))
            .triggerableAnim("hurt",RawAnimation.begin().thenPlay("hurt"));
        if(this instanceof MythicMountEntity)action.triggerableAnim("tame",RawAnimation.begin().thenPlay("tame"));
        if(this instanceof MythicMountEntity mount && mount.canFly()) {
            action.triggerableAnim("takeoff",RawAnimation.begin().thenPlay("takeoff"));
            action.triggerableAnim("landing",RawAnimation.begin().thenPlay("landing"));
        }
        controllers.add(action);
    }
}
