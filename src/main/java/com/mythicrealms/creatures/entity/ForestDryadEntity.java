package com.mythicrealms.creatures.entity;

import com.mythicrealms.creatures.entity.mount.MythicMountEntity;
import com.mythicrealms.creatures.registry.ModEntities;
import net.minecraft.core.particles.ParticleTypes;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.sounds.SoundEvents;
import net.minecraft.world.entity.*;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.level.Level;

public final class ForestDryadEntity extends ForestGuardianEntity {
    private LivingEntity healingTarget;
    private int healWindup,healCooldown;
    public ForestDryadEntity(EntityType<? extends ForestDryadEntity> type,Level level){super(type,level);}
    @Override public CreatureKind kind(){return CreatureKind.FOREST_DRYAD;}
    @Override public boolean busyCasting(){return healWindup>0;}
    @Override public void performAttack(ServerLevel level,LivingEntity target){CreatureProjectile.launch(ModEntities.VINE_SEED,this,target,1.15f);}
    public boolean beginHealing(LivingEntity target){
        if(healCooldown>0 || healWindup>0 || combatTimeline().isWindingUp() || !friendly(target)
            || target.getHealth()>=target.getMaxHealth() || distanceToSqr(target)>64 || !getSensing().hasLineOfSight(target))return false;
        healingTarget=target;healWindup=15;healCooldown=120;getNavigation().stop();
        triggerAnim("action","cast");playSound(SoundEvents.ENCHANTMENT_TABLE_USE,.5f,1.3f);return true;
    }
    private boolean friendly(LivingEntity target){
        return target.isAlive() && target!=getTarget() && (target instanceof ForestGuardianEntity
            || target instanceof Player || target instanceof MythicMountEntity mount && mount.isTame());
    }
    @Override protected void customServerAiStep(ServerLevel level){
        super.customServerAiStep(level);
        if(healCooldown>0)--healCooldown;
        if(healWindup>0 && --healWindup==0){
            var target=healingTarget;healingTarget=null;
            if(target!=null && friendly(target) && distanceToSqr(target)<64 && getSensing().hasLineOfSight(target)){
                target.heal(4);
                com.mythicrealms.creatures.magic.SpellEffects.particles(level,ParticleTypes.HAPPY_VILLAGER,target.getX(),target.getY()+1,target.getZ(),8,.4);
            }
        }
        if(tickCount%40==0 && healCooldown==0){
            for(var target:level.getEntitiesOfClass(LivingEntity.class,getBoundingBox().inflate(7),this::friendly)){
                if(beginHealing(target))break;
            }
        }
    }
}
