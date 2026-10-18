package com.mythicrealms.creatures.entity.expansion;

import com.mythicrealms.creatures.entity.CreatureKind;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.MoverType;
import net.minecraft.world.entity.ai.control.SmoothSwimmingLookControl;
import net.minecraft.world.entity.ai.control.SmoothSwimmingMoveControl;
import net.minecraft.world.entity.ai.goal.FloatGoal;
import net.minecraft.world.entity.ai.goal.RandomStrollGoal;
import net.minecraft.world.entity.ai.goal.RandomSwimmingGoal;
import net.minecraft.world.entity.ai.goal.WaterAvoidingRandomStrollGoal;
import net.minecraft.world.entity.ai.navigation.AmphibiousPathNavigation;
import net.minecraft.world.entity.ai.navigation.PathNavigation;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.pathfinder.PathType;
import net.minecraft.world.phys.Vec3;

/** Scout combat with amphibious paths and real vertical swimming, without forced surfacing. */
public final class SahuaginEntity extends ScoutProfileEntity {
    public SahuaginEntity(EntityType<? extends SahuaginEntity> type, Level level) {
        super(type, level);
        moveControl = new SmoothSwimmingMoveControl(this, 85, 10, 1, 1, false);
        lookControl = new SmoothSwimmingLookControl(this, 10);
        setPathfindingMalus(PathType.WATER, 0);
        setPathfindingMalus(PathType.WATER_BORDER, 0);
    }
    @Override public CreatureKind kind() { return CreatureKind.SAHUAGIN; }
    @Override protected PathNavigation createNavigation(Level level) {
        return new AmphibiousPathNavigation(this, level);
    }
    @Override protected void registerGoals() {
        super.registerGoals();
        goalSelector.removeAllGoals(goal -> goal instanceof FloatGoal || goal instanceof WaterAvoidingRandomStrollGoal);
        goalSelector.addGoal(6, new RandomSwimmingGoal(this, .8, 40) {
            @Override public boolean canUse() { return isInWater() && super.canUse(); }
            @Override public boolean canContinueToUse() { return isInWater() && super.canContinueToUse(); }
        });
        goalSelector.addGoal(6, new RandomStrollGoal(this, .8) {
            @Override public boolean canUse() { return !isInWater() && super.canUse(); }
            @Override public boolean canContinueToUse() { return !isInWater() && super.canContinueToUse(); }
        });
    }
    @Override public boolean canBreatheUnderwater() { return true; }
    @Override public boolean isPushedByFluid() { return false; }
    @Override public void updateSwimming() {
        if (!level().isClientSide()) setSwimming(isInWater() && !getNavigation().isDone());
    }
    @Override public void travel(Vec3 input) {
        if (isEffectiveAi() && isInWater()) {
            // SmoothSwimmingMoveControl already scales input by MOVEMENT_SPEED.
            // A fixed aquatic acceleration avoids applying that speed twice and
            // building enough momentum to orbit/overshoot path nodes.
            moveRelative(.02f, input);
            move(MoverType.SELF, getDeltaMovement());
            setDeltaMovement(getDeltaMovement().scale(.9));
        } else {
            super.travel(input);
        }
    }
}
