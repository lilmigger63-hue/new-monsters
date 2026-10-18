package com.mythicrealms.creatures.entity.expansion;

import com.mythicrealms.creatures.entity.GoblinScoutEntity;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.level.Level;

/** Inherits the original GoblinScout goals, cooperation and server combat timeline. */
public abstract class ScoutProfileEntity extends GoblinScoutEntity implements ProfiledCreature {
    protected ScoutProfileEntity(EntityType<? extends ScoutProfileEntity> type, Level level) { super(type, level); }
    @Override public AiProfile aiProfile() { return AiProfile.SCOUT; }
    @Override public void performAttack(ServerLevel level, LivingEntity target) {
        melee(level, target, attackRange(), 1);
    }
}
