package com.mythicrealms.creatures.entity;

import com.mythicrealms.creatures.entity.ai.CreatureCombatGoal;
import com.mythicrealms.creatures.entity.combat.AttackTimeline;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.sounds.SoundEvent;
import net.minecraft.sounds.SoundEvents;
import net.minecraft.world.damagesource.DamageSource;
import net.minecraft.world.entity.*;
import net.minecraft.world.entity.ai.goal.*;
import net.minecraft.world.entity.ai.goal.target.*;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.entity.monster.Monster;
import net.minecraft.world.level.Level;
import software.bernie.geckolib.animatable.GeoEntity;
import software.bernie.geckolib.animatable.instance.AnimatableInstanceCache;
import software.bernie.geckolib.animatable.manager.AnimatableManager;
import software.bernie.geckolib.animatable.processing.AnimationController;
import software.bernie.geckolib.animation.*;
import software.bernie.geckolib.util.GeckoLibUtil;

public abstract class MythicHostileEntity extends Monster implements GeoEntity {
    private static final RawAnimation IDLE = RawAnimation.begin().thenLoop("idle");
    private static final RawAnimation WALK = RawAnimation.begin().thenLoop("walk");
    private static final RawAnimation DEATH = RawAnimation.begin().thenPlayAndHold("death");
    private final AnimatableInstanceCache animationCache = GeckoLibUtil.createInstanceCache(this);
    public final AttackTimeline attack;
    private LivingEntity committedTarget;

    protected MythicHostileEntity(EntityType<? extends MythicHostileEntity> type, Level level) {
        super(type, level);
        attack = new AttackTimeline(kind().windup, kind().recovery);
        xpReward = kind().width >= 1.3 ? 12 : 5;
    }
    public abstract CreatureKind kind();
    public abstract void performAttack(ServerLevel level, LivingEntity target);
    public boolean reposition(LivingEntity target) { return false; }
    public boolean ranged() { return false; }
    public boolean busy() { return false; }
    public boolean tryAttack(LivingEntity target) {
        if (!attack.tryStart()) return false;
        committedTarget = target;
        getNavigation().stop();
        triggerAnim("action", "attack");
        playSound(kind() == CreatureKind.STONE_TROLL ? SoundEvents.STONE_BREAK : SoundEvents.PLAYER_ATTACK_SWEEP, .7f, .6f);
        return true;
    }
    @Override protected void registerGoals() {
        goalSelector.addGoal(0, new FloatGoal(this));
        goalSelector.addGoal(2, new CreatureCombatGoal(this));
        goalSelector.addGoal(6, new WaterAvoidingRandomStrollGoal(this, .8));
        goalSelector.addGoal(7, new LookAtPlayerGoal(this, Player.class, 8));
        goalSelector.addGoal(8, new RandomLookAroundGoal(this));
        targetSelector.addGoal(1, new HurtByTargetGoal(this));
        targetSelector.addGoal(2, new NearestAttackableTargetGoal<>(this, Player.class, true));
    }
    @Override protected void customServerAiStep(ServerLevel level) {
        super.customServerAiStep(level);
        if (committedTarget != null && (!committedTarget.isAlive() || !isAlive())) {
            attack.cancel(); committedTarget = null;
        }
        if (attack.tick()) {
            LivingEntity target = committedTarget;
            committedTarget = null;
            if (target != null && target.isAlive() && getSensing().hasLineOfSight(target)) performAttack(level, target);
        }
    }
    public void interruptAttack() { attack.cancel(); committedTarget = null; }
    public boolean areaVictim(LivingEntity candidate, LivingEntity primaryTarget) {
        if (!candidate.isAlive() || candidate == this || isAlliedTo(candidate)) return false;
        if (candidate instanceof Player player && (player.isCreative() || player.isSpectator())) return false;
        return candidate == primaryTarget || candidate instanceof Player;
    }
    public void melee(ServerLevel level, LivingEntity target, double reach, double multiplier) {
        if (target.isAlive() && distanceToSqr(target) <= reach * reach && getSensing().hasLineOfSight(target)) {
            target.hurtServer(level, damageSources().mobAttack(this),
                (float)(getAttributeValue(net.minecraft.world.entity.ai.attributes.Attributes.ATTACK_DAMAGE) * multiplier));
        }
    }
    @Override protected SoundEvent getAmbientSound() { return SoundEvents.PILLAGER_AMBIENT; }
    @Override protected SoundEvent getHurtSound(DamageSource source) { return SoundEvents.RAVAGER_HURT; }
    @Override protected SoundEvent getDeathSound() { return SoundEvents.RAVAGER_DEATH; }
    @Override public void registerControllers(AnimatableManager.ControllerRegistrar controllers) {
        controllers.add(new AnimationController<MythicHostileEntity>("locomotion", 5, test ->
            test.setAndContinue(test.animatable().isDeadOrDying() ? DEATH : test.isMoving() ? WALK : IDLE)));
        controllers.add(new AnimationController<MythicHostileEntity>("action", 2, test -> PlayState.STOP)
            .triggerableAnim("attack", RawAnimation.begin().thenPlay("attack"))
            .triggerableAnim("cast", RawAnimation.begin().thenPlay("cast")));
    }
    @Override public AnimatableInstanceCache getAnimatableInstanceCache() { return animationCache; }
}
