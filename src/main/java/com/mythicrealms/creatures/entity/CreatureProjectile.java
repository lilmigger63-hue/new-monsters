package com.mythicrealms.creatures.entity;

import com.mythicrealms.creatures.registry.ModEntities;
import net.minecraft.core.particles.ParticleTypes;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.effect.*;
import net.minecraft.world.entity.*;
import net.minecraft.world.entity.projectile.ThrowableItemProjectile;
import net.minecraft.world.item.*;
import net.minecraft.world.level.Level;
import net.minecraft.world.phys.*;

public final class CreatureProjectile extends ThrowableItemProjectile {
    public CreatureProjectile(EntityType<? extends CreatureProjectile> type, Level level) { super(type, level); }
    @Override protected Item getDefaultItem() { return getType() == ModEntities.TROLL_BOULDER ? Items.COBBLESTONE : Items.SLIME_BALL; }
    public static void launch(EntityType<CreatureProjectile> type, MythicHostileEntity caster, LivingEntity target, float speed) {
        CreatureProjectile bolt = new CreatureProjectile(type, caster.level());
        bolt.setOwner(caster);
        bolt.setPos(caster.getX(), caster.getEyeY() - .15, caster.getZ());
        Vec3 delta = target.getEyePosition().subtract(bolt.position());
        bolt.shoot(delta.x, delta.y + delta.horizontalDistance() * .1, delta.z, speed, 2);
        caster.level().addFreshEntity(bolt);
    }
    @Override protected boolean canHitEntity(Entity entity) { return !(entity instanceof MythicHostileEntity) && super.canHitEntity(entity); }
    @Override protected void onHitEntity(EntityHitResult result) {
        super.onHitEntity(result);
        if (level() instanceof ServerLevel level && result.getEntity() instanceof LivingEntity target) {
            boolean rock = getType() == ModEntities.TROLL_BOULDER;
            float damage = getOwner() instanceof LivingEntity owner
                ? (float)owner.getAttributeValue(net.minecraft.world.entity.ai.attributes.Attributes.ATTACK_DAMAGE) : 4;
            target.hurtServer(level, damageSources().thrown(this, getOwner()), damage);
            if (!rock) target.addEffect(new MobEffectInstance(MobEffects.POISON, 60, 0), getOwner());
            else target.knockback(.7, -getDeltaMovement().x, -getDeltaMovement().z);
        }
    }
    @Override protected void onHit(HitResult result) {
        super.onHit(result);
        if (level() instanceof ServerLevel level) {
            level.sendParticles(getType() == ModEntities.TROLL_BOULDER ? ParticleTypes.CLOUD : ParticleTypes.HAPPY_VILLAGER,
                getX(), getY(), getZ(), 5, .15, .15, .15, .02);
            discard();
        }
    }
    @Override public void tick() {
        super.tick();
        if (!level().isClientSide() && tickCount > 100) discard();
        if (level().isClientSide() && tickCount % 3 == 0 && getType() == ModEntities.SHAMAN_BOLT)
            level().addParticle(ParticleTypes.HAPPY_VILLAGER, getX(), getY(), getZ(), 0, .01, 0);
    }
}
