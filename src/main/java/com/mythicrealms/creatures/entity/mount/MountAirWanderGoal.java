package com.mythicrealms.creatures.entity.mount;

import net.minecraft.core.BlockPos;
import net.minecraft.world.entity.ai.goal.Goal;
import net.minecraft.world.level.levelgen.Heightmap;
import java.util.EnumSet;

/** Short, bounded flights above local loaded terrain; yields to owner following and combat. */
final class MountAirWanderGoal extends Goal {
    private final MythicMountEntity mount;
    private int ticks;
    private BlockPos destination;
    MountAirWanderGoal(MythicMountEntity mount){this.mount=mount;setFlags(EnumSet.of(Flag.MOVE));}
    @Override public boolean canUse(){
        if(mount.isVehicle() || mount.isOrderedToSit() || mount.getTarget()!=null || mount.isTame() || mount.getRandom().nextInt(140)!=0)return false;
        var pos=mount.blockPosition().offset(mount.getRandom().nextInt(17)-8,0,mount.getRandom().nextInt(17)-8);
        if(!mount.level().hasChunkAt(pos))return false;
        int floor=mount.level().getHeight(Heightmap.Types.MOTION_BLOCKING_NO_LEAVES,pos.getX(),pos.getZ());
        if(Math.abs(floor-mount.getY())>16)return false;
        destination=new BlockPos(pos.getX(),Math.min(floor+3,mount.level().getMaxY()-3),pos.getZ());return true;
    }
    @Override public void start(){ticks=0;mount.setFlying(true);mount.getNavigation().moveTo(destination.getX()+.5,destination.getY(),destination.getZ()+.5,.8);}
    @Override public boolean canContinueToUse(){return ticks<100 && !mount.getNavigation().isDone() && !mount.isVehicle() && mount.getTarget()==null;}
    @Override public void tick(){ticks++;}
    @Override public void stop(){mount.getNavigation().stop();}
}
