package com.mythicrealms.creatures.entity;

import com.mythicrealms.creatures.entity.ai.CreatureCombatGoal;
import com.mythicrealms.creatures.entity.combat.AttackTimeline;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.sounds.SoundEvent;
import net.minecraft.sounds.SoundEvents;
import net.minecraft.world.damagesource.DamageSource;
import net.minecraft.world.entity.*;
import net.minecraft.network.syncher.*;
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
    private static final RawAnimation FLY=RawAnimation.begin().thenLoop("fly");
    private static final RawAnimation HOVER=RawAnimation.begin().thenLoop("hover");
    private static final RawAnimation WALK = RawAnimation.begin().thenLoop("walk");
    private static final RawAnimation DEATH = RawAnimation.begin().thenPlayAndHold("death");
    private final AnimatableInstanceCache animationCache = GeckoLibUtil.createInstanceCache(this);
    public final AttackTimeline attack;
    private LivingEntity committedTarget;
    private static final EntityDataAccessor<Byte> VISUAL_POSE=SynchedEntityData.defineId(MythicHostileEntity.class,EntityDataSerializers.BYTE);
    @Override protected void defineSynchedData(SynchedEntityData.Builder data){super.defineSynchedData(data);data.define(VISUAL_POSE,(byte)0);}
    public byte visualPose(){return entityData.get(VISUAL_POSE);}
    private void updateVisualPose(){
        byte pose=0;
        if(!attack.isWindingUp() && isAlive()){
            if(kind()==CreatureKind.MINOTAUR && busy())pose=2;
            else if(getTarget()!=null && (kind()==CreatureKind.GRAVE_KNIGHT || kind()==CreatureKind.ORC_WARRIOR) && distanceToSqr(getTarget())<20)pose=1;
            else if(kind()==CreatureKind.GOBLIN_SCOUT && getTarget()!=null && tickCount%60<14 && distanceToSqr(getTarget())>=9 && distanceToSqr(getTarget())<=49)pose=3;
        }
        entityData.set(VISUAL_POSE,pose);
    }

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
    protected String attackAnimation() { return ranged() ? "cast" : "attack"; }
    public boolean tryAttack(LivingEntity target) {
        if (!attack.tryStart()) return false;
        committedTarget = target;
        getNavigation().stop();
        triggerAnim("action", attackAnimation());
        if(level() instanceof ServerLevel server)com.mythicrealms.creatures.magic.SpellEffects.telegraph(server,this,kind(),target);
        playSound(switch(kind()) {
            case STONE_TROLL, FROST_ELEMENTAL -> SoundEvents.STONE_BREAK;
            case GOBLIN_SHAMAN, SHADOW_WRAITH, DEMON_SORCERESS -> SoundEvents.EVOKER_PREPARE_ATTACK;
            case FLAME_IMP -> SoundEvents.BLAZE_SHOOT;
            case CAVE_BASILISK, CRYSTAL_SPIDER -> SoundEvents.SPIDER_AMBIENT;
            case HARPY -> SoundEvents.PHANTOM_FLAP;
            default -> SoundEvents.PLAYER_ATTACK_SWEEP;
        }, .7f, .6f);
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
        updateVisualPose();
        if(tickCount%12==0) {
            net.minecraft.core.particles.ParticleOptions particle=switch(kind()) {
                case GOBLIN_SHAMAN -> net.minecraft.core.particles.ParticleTypes.HAPPY_VILLAGER;
                case CRYSTAL_SPIDER -> net.minecraft.core.particles.ParticleTypes.END_ROD;
                case SHADOW_WRAITH -> net.minecraft.core.particles.ParticleTypes.SMOKE;
                case FLAME_IMP -> net.minecraft.core.particles.ParticleTypes.FLAME;
                case FROST_ELEMENTAL -> net.minecraft.core.particles.ParticleTypes.SNOWFLAKE;
                case DEMON_SORCERESS -> net.minecraft.core.particles.ParticleTypes.WITCH;
                default -> null;
            };
            if(particle!=null)com.mythicrealms.creatures.magic.SpellEffects.particles(level,particle,getX(),getY()+getBbHeight()*.5,getZ(),2,.25);
        }
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
    @Override protected SoundEvent getAmbientSound() {
        return switch(kind()) {
            case CAVE_BASILISK, CRYSTAL_SPIDER -> SoundEvents.SPIDER_AMBIENT;
            case GRAVE_KNIGHT -> SoundEvents.SKELETON_AMBIENT;
            case FROST_ELEMENTAL -> SoundEvents.SNOW_GOLEM_AMBIENT;
            case HARPY -> SoundEvents.PHANTOM_AMBIENT;
            case DEMON_SORCERESS -> SoundEvents.WITCH_AMBIENT;
            default -> SoundEvents.PILLAGER_AMBIENT;
        };
    }
    @Override public boolean hurtServer(ServerLevel level,DamageSource source,float damage) {
        boolean hit=super.hurtServer(level,source,damage);
        if(hit && isAlive() && !attack.isWindingUp())triggerAnim("action","hurt");
        return hit;
    }
    @Override protected SoundEvent getHurtSound(DamageSource source) { return SoundEvents.RAVAGER_HURT; }
    @Override protected SoundEvent getDeathSound() { return SoundEvents.RAVAGER_DEATH; }
    @Override public void registerControllers(AnimatableManager.ControllerRegistrar controllers) {
        controllers.add(new AnimationController<MythicHostileEntity>("locomotion",5,test -> {
            var mob=test.animatable();
            if(mob.isDeadOrDying())return test.setAndContinue(DEATH);
            String state=mob instanceof com.mythicrealms.creatures.entity.expansion.SahuaginEntity && mob.isInWater()
                ?(test.isMoving()?"swim":"idle_swim"):
                mob instanceof AerialHostileEntity && !mob.onGround()?(test.isMoving()?"fly":"hover"):
                test.isMoving()?(mob.getDeltaMovement().horizontalDistanceSqr()>.01?"run":"walk"):
                mob instanceof DemonSorceressEntity?"levitate":"idle";
            return test.setAndContinue(MythicCreature.loop(state));
        }));
        controllers.add(new AnimationController<MythicHostileEntity>("posture",4,test -> {
            byte pose=test.animatable().visualPose();
            return pose==0 || test.animatable().isDeadOrDying()?PlayState.STOP:
                test.setAndContinue(MythicCreature.loop(pose==1?"guard":pose==2?"charge":"sneak"));
        }));
        var action=new AnimationController<MythicHostileEntity>("action", 2, test -> PlayState.STOP)
            .triggerableAnim("attack", RawAnimation.begin().thenPlay("attack"))
            .triggerableAnim("cast", RawAnimation.begin().thenPlay("cast"))
            .triggerableAnim("hurt", RawAnimation.begin().thenPlay("hurt"));
        if(kind()==CreatureKind.GRAVE_KNIGHT)action.triggerableAnim("attack_two",RawAnimation.begin().thenPlay("attack_two"));
        if(kind()==CreatureKind.GRAVE_KNIGHT || kind()==CreatureKind.STONE_TROLL)action.triggerableAnim("heavy",RawAnimation.begin().thenPlay("heavy"));
        if(kind()==CreatureKind.STONE_TROLL)action.triggerableAnim("throw",RawAnimation.begin().thenPlay("throw"));
        if(kind()==CreatureKind.HARPY)action.triggerableAnim("swoop",RawAnimation.begin().thenPlay("swoop"));
        if(this instanceof DemonSorceressEntity)action.triggerableAnim("teleport",RawAnimation.begin().thenPlay("teleport"));
        controllers.add(action);
    }
    @Override public AnimatableInstanceCache getAnimatableInstanceCache() { return animationCache; }
}
