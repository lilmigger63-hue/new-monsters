package com.mythicrealms.creatures.entity.expansion;

import com.mythicrealms.creatures.entity.CreatureKind;
import com.mythicrealms.creatures.entity.CreatureProjectile;
import com.mythicrealms.creatures.magic.SpellEffects;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.entity.LivingEntity;

/** Override profile/projectile/range hooks in one species without copying its inherited goals. */
public interface ProfiledCreature {
    CreatureKind kind();
    AiProfile aiProfile();
    default double attackRange() { return kind().range; }
    default void launchProfileProjectile(ServerLevel level, LivingEntity caster, LivingEntity target) {
        if (caster.distanceToSqr(target) >= attackRange() * attackRange()) return;
        var profile = aiProfile();
        CreatureProjectile.launch(profile.projectile(), caster, target, profile.projectileSpeed);
        if (profile.combatParticle != null)
            SpellEffects.particles(level, profile.combatParticle, caster.getX(), caster.getEyeY(), caster.getZ(), 3, .15);
    }
}
