package com.mythicrealms.creatures.entity.expansion;

import com.mythicrealms.creatures.entity.GoblinShamanEntity;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.level.Level;

/** Inherits the original GoblinShaman goals, cooperation and server combat timeline. */
public abstract class ShamanProfileEntity extends GoblinShamanEntity implements ProfiledCreature {
    protected ShamanProfileEntity(EntityType<? extends ShamanProfileEntity> type, Level level) { super(type, level); }
    @Override public AiProfile aiProfile() { return AiProfile.SHAMAN; }
    @Override public void performAttack(ServerLevel level, LivingEntity target) {
        launchProfileProjectile(level, this, target);
    }
}
