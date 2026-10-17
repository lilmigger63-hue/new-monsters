package com.mythicrealms.creatures.entity.ai;

import com.mythicrealms.creatures.entity.MythicHostileEntity;
import net.minecraft.world.entity.ai.goal.Goal;
import net.minecraft.world.phys.Vec3;
import java.util.EnumSet;

public final class CreatureCombatGoal extends Goal {
    private final MythicHostileEntity mob;
    public CreatureCombatGoal(MythicHostileEntity mob) {
        this.mob = mob;
        setFlags(EnumSet.of(Flag.MOVE, Flag.LOOK));
    }
    @Override public boolean canUse() { return mob.getTarget() != null && mob.getTarget().isAlive(); }
    @Override public boolean canContinueToUse() { return canUse() && mob.distanceToSqr(mob.getTarget()) < 1600; }
    @Override public boolean requiresUpdateEveryTick() { return true; }
    @Override public void stop() { mob.interruptAttack(); mob.getNavigation().stop(); }
    @Override public void tick() {
        var target = mob.getTarget();
        if (target == null) return;
        mob.getLookControl().setLookAt(target, 30, 30);
        if (mob.busy()) return;
        if (mob.attack.isWindingUp()) { mob.getNavigation().stop(); return; }
        double distance = mob.distanceToSqr(target);
        if (mob.reposition(target)) return;
        if (mob.ranged() && distance < 16 && mob.tickCount % 10 == 0) {
            Vec3 retreat = mob.position().subtract(target.position()).normalize().scale(4).add(mob.position());
            mob.getNavigation().moveTo(retreat.x, retreat.y, retreat.z, 1.1);
        } else if (distance > mob.kind().range * mob.kind().range || !mob.getSensing().hasLineOfSight(target)) {
            if (mob.tickCount % 10 == 0) mob.getNavigation().moveTo(target, 1.1);
        } else {
            mob.getNavigation().stop();
            mob.tryAttack(target);
        }
    }
}
