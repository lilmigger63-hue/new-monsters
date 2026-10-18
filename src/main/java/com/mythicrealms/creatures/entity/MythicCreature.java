package com.mythicrealms.creatures.entity;

import com.mythicrealms.creatures.entity.mount.MythicMountEntity;
import net.minecraft.world.entity.LivingEntity;
import software.bernie.geckolib.animatable.GeoEntity;
import software.bernie.geckolib.animatable.manager.AnimatableManager;
import software.bernie.geckolib.animatable.processing.AnimationController;
import software.bernie.geckolib.animation.*;

public interface MythicCreature extends GeoEntity {
    CreatureKind kind();
    @Override default void registerControllers(AnimatableManager.ControllerRegistrar controllers) {
        controllers.add(new AnimationController<MythicCreature>("locomotion",5,test -> {
            var entity=(LivingEntity)test.animatable();
            String state="idle";
            if (entity.isDeadOrDying()) return test.setAndContinue(RawAnimation.begin().thenPlayAndHold("death"));
            if (entity instanceof MythicMountEntity mount) {
                if (mount.isInSittingPose()) state="sit";
                else if (mount.isFlying()) state=test.isMoving()?"fly":"hover";
                else if (test.isMoving()) state=mount.isVehicle()?"ride":"walk";
            } else if (test.isMoving()) state=entity.isSprinting()?"run":"walk";
            return test.setAndContinue(RawAnimation.begin().thenLoop(state));
        }));
        var action=new AnimationController<MythicCreature>("action",2,test -> PlayState.STOP)
            .triggerableAnim("attack",RawAnimation.begin().thenPlay("attack"))
            .triggerableAnim("cast",RawAnimation.begin().thenPlay("cast"))
            .triggerableAnim("hurt",RawAnimation.begin().thenPlay("hurt"));
        if(this instanceof MythicMountEntity)action.triggerableAnim("tame",RawAnimation.begin().thenPlay("tame"));
        controllers.add(action);
    }
}
