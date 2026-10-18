package com.mythicrealms.creatures.magic;

import com.mythicrealms.creatures.config.CreatureConfig;
import net.minecraft.core.particles.ParticleOptions;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.effect.*;

public final class SpellEffects {
    private SpellEffects() { }
    public static void particles(ServerLevel level,ParticleOptions particle,double x,double y,double z,int count,double spread){
        int amount=Math.clamp((int)Math.round(count*CreatureConfig.INSTANCE.magicParticleIntensity),0,64);
        if(amount>0)level.sendParticles(particle,x,y,z,amount,spread,spread,spread,.02);
    }
    public static void slow(LivingEntity target,int ticks,int strength){target.addEffect(new MobEffectInstance(MobEffects.SLOWNESS,ticks,strength));}
}
