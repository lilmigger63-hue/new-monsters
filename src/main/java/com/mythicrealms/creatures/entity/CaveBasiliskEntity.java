package com.mythicrealms.creatures.entity;

import com.mythicrealms.creatures.magic.SpellEffects;
import net.minecraft.core.particles.ParticleTypes;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.entity.*;
import net.minecraft.world.effect.*;
import net.minecraft.world.level.Level;

public final class CaveBasiliskEntity extends MythicHostileEntity {
    public CaveBasiliskEntity(EntityType<? extends CaveBasiliskEntity> type,Level level){super(type,level);}
    @Override public CreatureKind kind(){return CreatureKind.CAVE_BASILISK;}
    @Override public boolean ranged(){return true;}
    @Override public void performAttack(ServerLevel level,LivingEntity target){
        if(distanceToSqr(target)>81 || !getSensing().hasLineOfSight(target))return;
        boolean hurt=target.hurtServer(level,damageSources().mobAttack(this),(float)getAttributeValue(net.minecraft.world.entity.ai.attributes.Attributes.ATTACK_DAMAGE));
        if(hurt){SpellEffects.slow(target,65,3);target.addEffect(new MobEffectInstance(MobEffects.MINING_FATIGUE,65,1));}
        SpellEffects.particles(level,ParticleTypes.ASH,target.getX(),target.getEyeY(),target.getZ(),10,.3);
    }
}
