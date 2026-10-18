package com.mythicrealms.creatures.entity.ai;

import com.mythicrealms.creatures.entity.CreatureCombatant;
import com.mythicrealms.creatures.entity.mount.MythicMountEntity;
import net.minecraft.world.entity.ai.goal.Goal;
import java.util.EnumSet;

/** Shared pursuit and windup rules for neutral guardians and tameable creatures. */
public final class GuardianCombatGoal extends Goal {
    private final CreatureCombatant fighter;
    public GuardianCombatGoal(CreatureCombatant fighter) {
        this.fighter=fighter;setFlags(EnumSet.of(Flag.MOVE,Flag.LOOK));
    }
    @Override public boolean canUse() {
        var mob=fighter.actor();
        return fighter.canEngage() && mob.getTarget()!=null && mob.getTarget().isAlive() && mob.canAttack(mob.getTarget());
    }
    @Override public boolean canContinueToUse() { return canUse() && fighter.actor().distanceToSqr(fighter.actor().getTarget())<1600; }
    @Override public boolean requiresUpdateEveryTick() { return true; }
    @Override public void stop() { fighter.interruptAttack();fighter.actor().getNavigation().stop(); }
    @Override public void tick() {
        var mob=fighter.actor();var target=mob.getTarget();if(target==null)return;
        mob.getLookControl().setLookAt(target,30,30);
        if (fighter.combatTimeline().isWindingUp() || fighter.busyCasting()) { mob.getNavigation().stop();return; }
        double distance=mob.distanceToSqr(target);
        if (mob instanceof MythicMountEntity mount && mount.canFly() && (distance>36 || target.getY()>mob.getY()+2)) mount.setFlying(true);
        if(distance>fighter.kind().range*fighter.kind().range || !mob.getSensing().hasLineOfSight(target)) {
            if(mob.tickCount%com.mythicrealms.creatures.config.CreatureConfig.INSTANCE.aiUpdateInterval==0)mob.getNavigation().moveTo(target,1.1);
        } else {
            mob.getNavigation().stop();fighter.beginAttack(target);
        }
    }
}
