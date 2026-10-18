package com.mythicrealms.creatures.entity;

import net.minecraft.core.BlockPos;
import net.minecraft.world.entity.*;
import net.minecraft.world.entity.ai.control.FlyingMoveControl;
import net.minecraft.world.entity.ai.goal.Goal;
import net.minecraft.world.entity.ai.navigation.*;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.levelgen.Heightmap;
import net.minecraft.world.phys.Vec3;
import java.util.EnumSet;

/** Loaded-chunk-bounded flying navigation shared by spectral and winged enemies. */
public abstract class AerialHostileEntity extends MythicHostileEntity {
    protected AerialHostileEntity(EntityType<? extends AerialHostileEntity> type,Level level){super(type,level);moveControl=new FlyingMoveControl(this,14,true);}
    @Override protected PathNavigation createNavigation(Level level){var nav=new FlyingPathNavigation(this,level);nav.setCanFloat(true);return nav;}
    @Override protected void registerGoals(){
        super.registerGoals();
        goalSelector.addGoal(5,new Goal(){
            private int ticks;
            {setFlags(EnumSet.of(Flag.MOVE));}
            @Override public boolean canUse(){return getTarget()==null && getRandom().nextInt(80)==0;}
            @Override public void start(){
                ticks=0;var pos=blockPosition().offset(getRandom().nextInt(13)-6,0,getRandom().nextInt(13)-6);
                if(!level().hasChunkAt(pos))return;
                int ground=level().getHeight(Heightmap.Types.MOTION_BLOCKING_NO_LEAVES,pos.getX(),pos.getZ());
                double y=Math.min(Math.max(getY()-3,ground+2),Math.min(getY()+4,level().getMaxY()-3));
                getNavigation().moveTo(pos.getX()+.5,y,pos.getZ()+.5,.8);
            }
            @Override public boolean canContinueToUse(){return ++ticks<100 && getTarget()==null && !getNavigation().isDone();}
            @Override public void stop(){getNavigation().stop();}
        });
    }
    @Override public void travel(Vec3 input){
        if(isLocalInstanceAuthoritative()){
            setNoGravity(true);fallDistance=0;moveRelative(.06f,input);
            Vec3 velocity=getDeltaMovement();
            if(getNavigation().isDone() && getTarget()==null)velocity=new Vec3(velocity.x*.8,-.05,velocity.z*.8);
            if(velocity.length()>.55)velocity=velocity.normalize().scale(.55);
            if(getY()>level().getMaxY()-3)velocity=new Vec3(velocity.x,Math.min(0,velocity.y),velocity.z);
            if(!level().hasChunkAt(BlockPos.containing(position().add(velocity))))velocity=Vec3.ZERO;
            setDeltaMovement(velocity);move(MoverType.SELF,velocity);setDeltaMovement(velocity.scale(.85));calculateEntityAnimation(false);
        }else super.travel(input);
    }
    @Override public boolean causeFallDamage(double distance,float multiplier,net.minecraft.world.damagesource.DamageSource source){return false;}
}
