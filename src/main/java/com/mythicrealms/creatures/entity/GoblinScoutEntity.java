package com.mythicrealms.creatures.entity;

import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.entity.*;
import net.minecraft.world.level.Level;
import net.minecraft.world.phys.Vec3;

public class GoblinScoutEntity extends MythicHostileEntity {
    public GoblinScoutEntity(EntityType<? extends GoblinScoutEntity> type, Level level) { super(type, level); }
    @Override public CreatureKind kind() { return CreatureKind.GOBLIN_SCOUT; }
    @Override public boolean reposition(LivingEntity target) {
        if (distanceToSqr(target) < 9 || distanceToSqr(target) > 49 || tickCount % 60 >= 14) return false;
        if (tickCount % 7 == 0) {
            Vec3 offset = position().subtract(target.position()).normalize();
            double side = (getId() & 1) == 0 ? 1 : -1;
            Vec3 point = target.position().add(-offset.z * 2.5 * side, 0, offset.x * 2.5 * side);
            getNavigation().moveTo(point.x, point.y, point.z, 1.2);
        }
        return true;
    }
    @Override protected void customServerAiStep(ServerLevel level) {
        super.customServerAiStep(level);
        var target=getTarget();
        if(tickCount%40!=0 || target==null || !target.isAlive() || !canAttack(target))return;
        int recruited=0;
        for(var ally:level.getEntitiesOfClass(GoblinScoutEntity.class,getBoundingBox().inflate(8))) {
            if(ally==this || ally.kind()!=kind() || ally.getTarget()!=null || !ally.canAttack(target)
                || ally.distanceToSqr(target)>28*28 || !ally.getSensing().hasLineOfSight(target))continue;
            ally.setTarget(target);
            if(++recruited==4)break;
        }
    }
    @Override public void performAttack(ServerLevel level, LivingEntity target) { melee(level, target, 2.1, 1); }
}
