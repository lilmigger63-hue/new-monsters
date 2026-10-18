package com.mythicrealms.creatures.entity;

import com.mythicrealms.creatures.entity.ai.GuardianCombatGoal;
import com.mythicrealms.creatures.entity.combat.AttackTimeline;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.sounds.*;
import net.minecraft.world.damagesource.DamageSource;
import net.minecraft.world.entity.*;
import net.minecraft.world.entity.ai.goal.*;
import net.minecraft.world.entity.ai.goal.target.*;
import net.minecraft.world.entity.monster.Monster;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.level.Level;
import software.bernie.geckolib.animatable.instance.AnimatableInstanceCache;
import software.bernie.geckolib.util.GeckoLibUtil;

public abstract class ForestGuardianEntity extends PathfinderMob implements CreatureCombatant {
    private final AnimatableInstanceCache cache=GeckoLibUtil.createInstanceCache(this);
    private final AttackTimeline attack;
    private LivingEntity pending;
    protected ForestGuardianEntity(EntityType<? extends ForestGuardianEntity> type,Level level) {
        super(type,level);attack=new AttackTimeline(kind().windup,kind().recovery);xpReward=6;
    }
    @Override protected void registerGoals() {
        goalSelector.addGoal(0,new FloatGoal(this));
        goalSelector.addGoal(2,new GuardianCombatGoal(this));
        goalSelector.addGoal(6,new WaterAvoidingRandomStrollGoal(this,.7));
        goalSelector.addGoal(7,new LookAtPlayerGoal(this,Player.class,8));
        goalSelector.addGoal(8,new RandomLookAroundGoal(this));
        targetSelector.addGoal(1,new HurtByTargetGoal(this));
        targetSelector.addGoal(2,new NearestAttackableTargetGoal<>(this,Monster.class,true));
    }
    @Override public boolean canAttack(LivingEntity target) { return !(target instanceof ForestGuardianEntity) && super.canAttack(target); }
    @Override public AttackTimeline combatTimeline() { return attack; }
    @Override public boolean beginAttack(LivingEntity target) {
        if (!canAttack(target) || !attack.tryStart())return false;
        pending=target;triggerAnim("action","cast");
        if(level() instanceof ServerLevel server)com.mythicrealms.creatures.magic.SpellEffects.telegraph(server,this,kind(),target);playSound(SoundEvents.EVOKER_PREPARE_ATTACK,.5f,.7f);return true;
    }
    @Override public void interruptAttack() { attack.cancel();pending=null; }
    @Override protected void customServerAiStep(ServerLevel level) {
        super.customServerAiStep(level);
        if(kind()==CreatureKind.ANCIENT_TREANT && tickCount%20==0)
            com.mythicrealms.creatures.magic.SpellEffects.particles(level,net.minecraft.core.particles.ParticleTypes.HAPPY_VILLAGER,getX(),getY()+getBbHeight()*.7,getZ(),2,.6);
        if(pending!=null && (!pending.isAlive() || !canAttack(pending)))interruptAttack();
        if(attack.tick()) {
            var target=pending;pending=null;
            if(target!=null && distanceToSqr(target)<kind().range*kind().range && getSensing().hasLineOfSight(target))performAttack(level,target);
        }
    }
    public abstract void performAttack(ServerLevel level,LivingEntity target);
    @Override protected SoundEvent getAmbientSound(){return SoundEvents.AZALEA_LEAVES_STEP;}
    @Override protected SoundEvent getHurtSound(DamageSource source){return SoundEvents.WOOD_BREAK;}
    @Override protected SoundEvent getDeathSound(){return SoundEvents.WOOD_BREAK;}
    @Override public AnimatableInstanceCache getAnimatableInstanceCache(){return cache;}
    @Override public boolean hurtServer(ServerLevel level,net.minecraft.world.damagesource.DamageSource source,float damage){
        boolean hit=super.hurtServer(level,source,damage);
        if(hit && isAlive() && !combatTimeline().isWindingUp())triggerAnim("action","hurt");
        return hit;
    }

}
