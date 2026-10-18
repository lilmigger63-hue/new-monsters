package com.mythicrealms.creatures.entity;

import com.mythicrealms.creatures.registry.ModEntities;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.sounds.*;
import net.minecraft.world.entity.*;
import net.minecraft.world.level.Level;

public class SlimeMaidenEntity extends ForestGuardianEntity {
    public SlimeMaidenEntity(EntityType<? extends SlimeMaidenEntity> type,Level level){super(type,level);}
    @Override public CreatureKind kind(){return CreatureKind.SLIME_MAIDEN;}
    @Override public void performAttack(ServerLevel level,LivingEntity target){if(distanceToSqr(target)<100)CreatureProjectile.launch(ModEntities.SLIME_BUBBLE,this,target,1.1f);}
    @Override protected void customServerAiStep(ServerLevel level){
        super.customServerAiStep(level);
        if(onGround() && tickCount%35==0 && !combatTimeline().isWindingUp()){
            setDeltaMovement(getDeltaMovement().x,.3,getDeltaMovement().z);playSound(SoundEvents.SLIME_JUMP,.4f,1.3f);
        }
    }
    @Override protected SoundEvent getAmbientSound(){return SoundEvents.SLIME_SQUISH;}
    @Override protected SoundEvent getDeathSound(){return SoundEvents.SLIME_DEATH;}
}
