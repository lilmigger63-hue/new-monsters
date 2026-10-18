package com.mythicrealms.creatures.entity.expansion;

import com.mythicrealms.creatures.entity.DemonSorceressEntity;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.level.Level;

/** Inherits the original DemonSorceress goals, cooperation and server combat timeline. */
public abstract class DemonProfileEntity extends DemonSorceressEntity implements ProfiledCreature {
    protected DemonProfileEntity(EntityType<? extends DemonProfileEntity> type, Level level) { super(type, level); }
    @Override public AiProfile aiProfile() { return AiProfile.DEMON; }
    @Override public void performAttack(ServerLevel level, LivingEntity target) {
        if (distanceToSqr(target) < 16) teleportAway(level, target);
        launchProfileProjectile(level, this, target);
    }
}
