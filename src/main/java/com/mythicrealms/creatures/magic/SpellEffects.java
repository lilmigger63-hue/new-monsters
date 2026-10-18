package com.mythicrealms.creatures.magic;

import com.mythicrealms.creatures.config.CreatureConfig;
import com.mythicrealms.creatures.entity.CreatureKind;
import net.minecraft.core.particles.*;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.entity.*;
import net.minecraft.world.effect.*;
import net.minecraft.world.level.block.Blocks;

/** Bounded, nearby-player-only presentation. No damage, targeting or movement authority. */
public final class SpellEffects {
    private SpellEffects() { }
    private static boolean visible(ServerLevel level,double x,double y,double z){
        for(var player:level.players())if(player.distanceToSqr(x,y,z)<=32*32)return true;
        return false;
    }
    public static void particles(ServerLevel level,ParticleOptions particle,double x,double y,double z,int count,double spread){
        int amount=Math.clamp((int)Math.round(count*CreatureConfig.INSTANCE.magicParticleIntensity),0,64);
        if(amount>0 && visible(level,x,y,z))level.sendParticles(particle,x,y,z,amount,spread,spread,spread,.02);
    }
    public static void ring(ServerLevel level,ParticleOptions particle,double x,double y,double z,double radius,int requested){
        int amount=Math.clamp((int)Math.round(requested*CreatureConfig.INSTANCE.magicParticleIntensity),0,24);
        if(amount==0 || !visible(level,x,y,z))return;
        for(int i=0;i<amount;i++){
            double angle=Math.PI*2*i/amount;
            level.sendParticles(particle,x+Math.cos(angle)*radius,y,z+Math.sin(angle)*radius,1,0,0,0,0);
        }
    }
    public static void telegraph(ServerLevel level,Mob caster,CreatureKind kind,LivingEntity target){
        ParticleOptions particle=switch(kind){
            case GOBLIN_SHAMAN,FOREST_DRYAD,ANCIENT_TREANT -> ParticleTypes.HAPPY_VILLAGER;
            case SHADOW_WRAITH,DEMON_SORCERESS -> ParticleTypes.WITCH;
            case CRYSTAL_SPIDER,MOON_STAG -> ParticleTypes.END_ROD;
            case FLAME_IMP -> ParticleTypes.FLAME;
            case FROST_ELEMENTAL -> ParticleTypes.SNOWFLAKE;
            case CAVE_BASILISK -> ParticleTypes.ASH;
            case WILD_WYVERN,SLIME_MAIDEN -> ParticleTypes.SNEEZE;
            case HARPY,GRIFFIN -> ParticleTypes.WHITE_ASH;
            case MINOTAUR,STONE_TROLL -> new BlockParticleOption(ParticleTypes.BLOCK,Blocks.STONE.defaultBlockState());
            default -> null;
        };
        if(particle==null)return;
        double y=caster.getY()+Math.min(.8,caster.getBbHeight()*.45);
        ring(level,particle,caster.getX(),y,caster.getZ(),Math.max(.35,caster.getBbWidth()*.65),12);
        if(kind==CreatureKind.GOBLIN_SHAMAN || kind==CreatureKind.DEMON_SORCERESS)
            ring(level,particle,caster.getX(),y+.15,caster.getZ(),.3,8);
    }
    public static void gaze(ServerLevel level,LivingEntity caster,LivingEntity target){
        if(CreatureConfig.INSTANCE.magicParticleIntensity==0 || !visible(level,caster.getX(),caster.getY(),caster.getZ()))return;
        int points=Math.clamp((int)Math.round(10*CreatureConfig.INSTANCE.magicParticleIntensity),1,16);
        var from=caster.getEyePosition();var delta=target.getEyePosition().subtract(from);
        for(int i=1;i<=points;i++){
            double f=(double)i/points;
            level.sendParticles(ParticleTypes.ASH,from.x+delta.x*f,from.y+delta.y*f,from.z+delta.z*f,1,0,0,0,0);
        }
    }
    public static void slow(LivingEntity target,int ticks,int strength){target.addEffect(new MobEffectInstance(MobEffects.SLOWNESS,ticks,strength));}
}
