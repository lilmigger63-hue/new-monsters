package com.mythicrealms.creatures.entity;

import com.mythicrealms.creatures.registry.ModEntities;
import net.minecraft.core.particles.ParticleTypes;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.sounds.SoundEvents;
import net.minecraft.world.entity.*;
import net.minecraft.world.level.Level;

public class GoblinShamanEntity extends MythicHostileEntity {
    public GoblinShamanEntity(EntityType<? extends GoblinShamanEntity> type, Level level) { super(type, level); }
    @Override public CreatureKind kind() { return CreatureKind.GOBLIN_SHAMAN; }
    @Override public boolean ranged() { return true; }
    @Override public void performAttack(ServerLevel level, LivingEntity target) {
        if (distanceToSqr(target) < 225) CreatureProjectile.launch(ModEntities.SHAMAN_BOLT, this, target, 1.1f);
    }
    @Override protected void customServerAiStep(ServerLevel level) {
        super.customServerAiStep(level);
        if (tickCount % 160 != 0 || attack.isWindingUp()) return;
        var wounded = level.getEntitiesOfClass(MythicHostileEntity.class, getBoundingBox().inflate(7),
            ally -> ally.isAlive() && ally.getHealth() < ally.getMaxHealth() && getSensing().hasLineOfSight(ally));
        if (!wounded.isEmpty()) {
            var ally = wounded.getFirst(); ally.heal(4);
            triggerAnim("action", "cast");
            com.mythicrealms.creatures.magic.SpellEffects.particles(level,ParticleTypes.HAPPY_VILLAGER,ally.getX(),ally.getY()+1,ally.getZ(),6,.3);
            playSound(SoundEvents.EVOKER_CAST_SPELL, .6f, 1.4f);
        }
    }
}
