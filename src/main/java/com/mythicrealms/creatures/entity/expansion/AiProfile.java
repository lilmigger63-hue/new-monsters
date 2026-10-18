package com.mythicrealms.creatures.entity.expansion;

import com.mythicrealms.creatures.entity.CreatureProjectile;
import com.mythicrealms.creatures.registry.ModEntities;
import net.minecraft.core.particles.ParticleOptions;
import net.minecraft.core.particles.ParticleTypes;
import net.minecraft.world.entity.EntityType;

/** Shared capabilities; species balance remains in CreatureKind and entity attributes. */
public enum AiProfile {
    SCOUT(false, true, 0, null),
    SHAMAN(true, true, 1.1f, ParticleTypes.HAPPY_VILLAGER),
    SLIME(true, false, 1.1f, ParticleTypes.ITEM_SLIME),
    DEMON(true, true, 1.2f, ParticleTypes.PORTAL);

    public final boolean ranged, attacksPlayers;
    public final float projectileSpeed;
    public final ParticleOptions combatParticle;
    AiProfile(boolean ranged, boolean attacksPlayers, float projectileSpeed, ParticleOptions particle) {
        this.ranged = ranged;
        this.attacksPlayers = attacksPlayers;
        this.projectileSpeed = projectileSpeed;
        this.combatParticle = particle;
    }
    public EntityType<CreatureProjectile> projectile() {
        return switch (this) {
            case SHAMAN -> ModEntities.SHAMAN_BOLT;
            case SLIME -> ModEntities.SLIME_BUBBLE;
            case DEMON -> ModEntities.DARK_BOLT;
            case SCOUT -> throw new IllegalStateException("Scout profile uses melee");
        };
    }
    public String attackAnimation() { return ranged ? "cast" : "attack"; }
}
