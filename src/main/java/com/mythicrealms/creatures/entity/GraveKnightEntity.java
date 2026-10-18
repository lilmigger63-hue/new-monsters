package com.mythicrealms.creatures.entity;

import net.minecraft.server.level.ServerLevel;
import net.minecraft.tags.DamageTypeTags;
import net.minecraft.world.damagesource.DamageSource;
import net.minecraft.world.entity.*;
import net.minecraft.world.level.Level;

public final class GraveKnightEntity extends MythicHostileEntity {
    private int combo;
    public GraveKnightEntity(EntityType<? extends GraveKnightEntity> type,Level level){super(type,level);}
    @Override public CreatureKind kind(){return CreatureKind.GRAVE_KNIGHT;}
    @Override protected String attackAnimation(){return (combo+1)%3==0?"heavy":"attack";}
    @Override public void performAttack(ServerLevel level,LivingEntity target){
        boolean heavy=++combo%3==0;
        melee(level,target,2.8,heavy?1.5:1);
        if(heavy && distanceToSqr(target)<8)target.knockback(.7,getX()-target.getX(),getZ()-target.getZ());
    }
    @Override public boolean hurtServer(ServerLevel level,DamageSource source,float damage){
        var from=source.getSourcePosition();
        if(attack!=null && !attack.isWindingUp() && getTarget()!=null && from!=null
            && !source.is(DamageTypeTags.BYPASSES_SHIELD) && from.subtract(position()).normalize().dot(getLookAngle())>.5)damage*=.6f;
        return super.hurtServer(level,source,damage);
    }
}
