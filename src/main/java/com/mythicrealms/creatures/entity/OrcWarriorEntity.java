package com.mythicrealms.creatures.entity;

import net.minecraft.server.level.ServerLevel;
import net.minecraft.sounds.SoundEvents;
import net.minecraft.tags.DamageTypeTags;
import net.minecraft.world.damagesource.DamageSource;
import net.minecraft.world.entity.*;
import net.minecraft.world.level.Level;

public final class OrcWarriorEntity extends MythicHostileEntity {
    public OrcWarriorEntity(EntityType<? extends OrcWarriorEntity> type, Level level) { super(type, level); }
    @Override public CreatureKind kind() { return CreatureKind.ORC_WARRIOR; }
    @Override public void performAttack(ServerLevel level, LivingEntity target) {
        melee(level, target, 2.8, 1);
        if (distanceToSqr(target) < 8) target.knockback(.6, getX() - target.getX(), getZ() - target.getZ());
    }
    @Override public boolean hurtServer(ServerLevel level, DamageSource source, float amount) {
        var from = source.getSourcePosition();
        if (attack != null && !attack.isWindingUp() && getTarget() != null && from != null
            && !source.is(DamageTypeTags.BYPASSES_SHIELD)
            && from.subtract(position()).normalize().dot(getLookAngle()) > .5) {
            amount *= .45f;
            playSound(SoundEvents.SHIELD_BLOCK.value(), .7f, .8f);
        }
        return super.hurtServer(level, source, amount);
    }
}
