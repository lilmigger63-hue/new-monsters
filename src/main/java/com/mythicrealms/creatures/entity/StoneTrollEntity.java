package com.mythicrealms.creatures.entity;

import com.mythicrealms.creatures.registry.ModEntities;
import net.minecraft.core.particles.ParticleTypes;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.sounds.SoundEvents;
import net.minecraft.world.entity.*;
import net.minecraft.world.level.Level;

public final class StoneTrollEntity extends MythicHostileEntity {
    public StoneTrollEntity(EntityType<? extends StoneTrollEntity> type, Level level) { super(type, level); }
    @Override public CreatureKind kind() { return CreatureKind.STONE_TROLL; }
    @Override public boolean ranged() { return true; }
    @Override public void performAttack(ServerLevel level, LivingEntity target) {
        if (distanceToSqr(target) < 25) {
            for (LivingEntity player : level.getEntitiesOfClass(LivingEntity.class, getBoundingBox().inflate(2.8), p -> areaVictim(p, target))) {
                melee(level, player, 4.5, 1);
                player.knockback(.9, getX() - player.getX(), getZ() - player.getZ());
            }
            level.sendParticles(ParticleTypes.CLOUD, getX(), getY() + .2, getZ(), 16, 1.5, .1, 1.5, .03);
            playSound(SoundEvents.GENERIC_EXPLODE.value(), .5f, .6f);
        } else if (distanceToSqr(target) < 256) CreatureProjectile.launch(ModEntities.TROLL_BOULDER, this, target, 1.2f);
    }
}
