package com.mythicrealms.creatures.entity.expansion;

import com.mythicrealms.creatures.entity.SlimeMaidenEntity;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.level.Level;

/** Inherits the original SlimeMaiden goals, cooperation and server combat timeline. */
public abstract class SlimeProfileEntity extends SlimeMaidenEntity implements ProfiledCreature {
    protected SlimeProfileEntity(EntityType<? extends SlimeProfileEntity> type, Level level) { super(type, level); }
    @Override public AiProfile aiProfile() { return AiProfile.SLIME; }
    @Override public void performAttack(ServerLevel level, LivingEntity target) {
        launchProfileProjectile(level, this, target);
    }
}
