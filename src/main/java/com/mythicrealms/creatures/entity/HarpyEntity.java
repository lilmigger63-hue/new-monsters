package com.mythicrealms.creatures.entity;

import com.mythicrealms.creatures.registry.ModEntities;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.entity.*;
import net.minecraft.world.level.Level;

public final class HarpyEntity extends AerialHostileEntity {
    public HarpyEntity(EntityType<? extends HarpyEntity> type,Level level){super(type,level);}
    @Override public CreatureKind kind(){return CreatureKind.HARPY;}
    @Override protected String attackAnimation(){return getTarget()!=null && distanceToSqr(getTarget())<9?"swoop":"cast";}
    @Override public boolean ranged(){return true;}
    @Override public boolean reposition(LivingEntity target){
        if(tickCount%100<28 && distanceToSqr(target)>7){
            if(tickCount%7==0)getNavigation().moveTo(target.getX(),target.getY()+.5,target.getZ(),1.3);return true;
        }
        if(tickCount%100>80 && distanceToSqr(target)<36){
            if(tickCount%7==0)getNavigation().moveTo(getX(),target.getY()+4,getZ(),1.1);return true;
        }
        return false;
    }
    @Override public void performAttack(ServerLevel level,LivingEntity target){
        if(distanceToSqr(target)<9)melee(level,target,3,1.25);
        else if(distanceToSqr(target)<121)CreatureProjectile.launch(ModEntities.FEATHER_BOLT,this,target,1.6f);
    }
}
