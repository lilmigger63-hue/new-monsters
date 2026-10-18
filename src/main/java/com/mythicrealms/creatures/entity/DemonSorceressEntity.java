package com.mythicrealms.creatures.entity;

import com.mythicrealms.creatures.magic.SpellEffects;
import com.mythicrealms.creatures.registry.ModEntities;
import net.minecraft.core.BlockPos;
import net.minecraft.core.particles.ParticleTypes;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.entity.*;
import net.minecraft.world.level.Level;

public final class DemonSorceressEntity extends MythicHostileEntity {
    private int teleportCooldown;
    public DemonSorceressEntity(EntityType<? extends DemonSorceressEntity> type,Level level){super(type,level);}
    @Override public CreatureKind kind(){return CreatureKind.DEMON_SORCERESS;}
    @Override public boolean ranged(){return true;}
    public boolean teleportAway(ServerLevel level,LivingEntity target){
        if(teleportCooldown>0)return false;
        for(int attempt=0;attempt<4;attempt++){
            double x=getX()+getRandom().nextInt(9)-4,z=getZ()+getRandom().nextInt(9)-4;
            if(!level.hasChunkAt(BlockPos.containing(x,getY(),z)))continue;
            if(target.distanceToSqr(x,getY(),z)<16)continue;
            if(randomTeleport(x,getY()+2,z,true)){
                triggerAnim("action","teleport");teleportCooldown=100;SpellEffects.particles(level,ParticleTypes.PORTAL,getX(),getY()+1,getZ(),16,.6);return true;
            }
        }
        teleportCooldown=30;return false;
    }
    @Override public void performAttack(ServerLevel level,LivingEntity target){
        if(distanceToSqr(target)<16)teleportAway(level,target);
        if(distanceToSqr(target)<225)CreatureProjectile.launch(ModEntities.DARK_BOLT,this,target,1.2f);
    }
    @Override protected void customServerAiStep(ServerLevel level){super.customServerAiStep(level);if(teleportCooldown>0)--teleportCooldown;}
}
