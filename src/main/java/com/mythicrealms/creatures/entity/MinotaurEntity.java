package com.mythicrealms.creatures.entity;

import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.entity.*;
import net.minecraft.world.level.Level;
import net.minecraft.world.phys.Vec3;
import java.util.HashSet;
import java.util.Set;

public final class MinotaurEntity extends MythicHostileEntity {
    private int chargeTicks;
    private LivingEntity chargeTarget;
    private Vec3 chargeDirection = Vec3.ZERO;
    private final Set<Integer> hit = new HashSet<>();
    public MinotaurEntity(EntityType<? extends MinotaurEntity> type, Level level) { super(type, level); }
    @Override public CreatureKind kind() { return CreatureKind.MINOTAUR; }
    @Override public boolean busy() { return chargeTicks > 0; }
    @Override public void performAttack(ServerLevel level, LivingEntity target) {
        if (distanceToSqr(target) < 12) {
            for (LivingEntity player : level.getEntitiesOfClass(LivingEntity.class, getBoundingBox().inflate(2.2), p -> areaVictim(p, target)))
                melee(level, player, 3.5, 1);
        } else if (distanceToSqr(target) < 100) {
            chargeDirection = target.position().subtract(position()).multiply(1, 0, 1).normalize().scale(.65);
            chargeTicks = 16; chargeTarget = target; hit.clear();
        }
    }
    @Override protected void customServerAiStep(ServerLevel level) {
        super.customServerAiStep(level);
        if (chargeTicks <= 0) return;
        --chargeTicks;
        if (horizontalCollision) { chargeTicks = 0; return; }
        getNavigation().stop();
        setDeltaMovement(chargeDirection.x, getDeltaMovement().y, chargeDirection.z);
        for (LivingEntity player : level.getEntitiesOfClass(LivingEntity.class, getBoundingBox().inflate(.7), p -> areaVictim(p, chargeTarget))) {
            if (hit.add(player.getId())) {
                melee(level, player, 3, 1.25);
                player.knockback(1, getX() - player.getX(), getZ() - player.getZ());
            }
        }
    }
}
