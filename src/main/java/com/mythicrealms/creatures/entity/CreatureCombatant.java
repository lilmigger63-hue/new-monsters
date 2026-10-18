package com.mythicrealms.creatures.entity;

import com.mythicrealms.creatures.entity.combat.AttackTimeline;
import net.minecraft.world.entity.*;

public interface CreatureCombatant extends MythicCreature {
    AttackTimeline combatTimeline();
    boolean beginAttack(LivingEntity target);
    void interruptAttack();
    default PathfinderMob actor() { return (PathfinderMob)this; }
    default boolean canEngage() { return actor().isAlive(); }
    default boolean busyCasting() { return false; }
}
