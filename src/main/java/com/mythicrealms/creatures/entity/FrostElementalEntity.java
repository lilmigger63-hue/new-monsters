package com.mythicrealms.creatures.entity;

import com.mythicrealms.creatures.magic.SpellEffects;
import com.mythicrealms.creatures.registry.ModEntities;
import net.minecraft.core.particles.ParticleTypes;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.entity.*;
import net.minecraft.world.level.Level;

public final class FrostElementalEntity extends MythicHostileEntity {
    public FrostElementalEntity(EntityType<? extends FrostElementalEntity> type,Level level){super(type,level);}
    @Override public CreatureKind kind(){return CreatureKind.FROST_ELEMENTAL;}
    @Override public boolean ranged(){return true;}
    @Override public void performAttack(ServerLevel level,LivingEntity target){
        if(distanceToSqr(target)<16){
            for(var victim:level.getEntitiesOfClass(LivingEntity.class,getBoundingBox().inflate(4),candidate -> areaVictim(candidate,target))){
                if(getSensing().hasLineOfSight(victim) && victim.hurtServer(level,damageSources().mobAttack(this),(float)getAttributeValue(net.minecraft.world.entity.ai.attributes.Attributes.ATTACK_DAMAGE)))SpellEffects.slow(victim,80,2);
            }
            SpellEffects.particles(level,ParticleTypes.SNOWFLAKE,getX(),getY()+.6,getZ(),18,2);
        }else if(distanceToSqr(target)<169)CreatureProjectile.launch(ModEntities.ICE_SPIKE,this,target,1.2f);
    }
}
