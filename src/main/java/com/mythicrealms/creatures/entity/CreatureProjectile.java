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
    @Override protected Item getDefaultItem() {
        if(getType()==ModEntities.TROLL_BOULDER)return Items.COBBLESTONE;
        if(getType()==ModEntities.ROOT_SHARD)return Items.STICK;
        if(getType()==ModEntities.VINE_SEED)return Items.OAK_SAPLING;
        if(getType()==ModEntities.POISON_BREATH)return Items.SPIDER_EYE;
        if(getType()==ModEntities.CRYSTAL_BOLT)return Items.AMETHYST_SHARD;
        if(getType()==ModEntities.FIRE_BOLT)return Items.FIRE_CHARGE;
        if(getType()==ModEntities.ICE_SPIKE)return Items.PACKED_ICE;
        if(getType()==ModEntities.DARK_BOLT)return Items.ENDER_PEARL;
        if(getType()==ModEntities.FEATHER_BOLT)return Items.FEATHER;
        return Items.SLIME_BALL;
    }
    public static void launch(EntityType<CreatureProjectile> type, LivingEntity caster, LivingEntity target, float speed) {
        CreatureProjectile bolt = new CreatureProjectile(type, caster.level());
        bolt.setOwner(caster);
        bolt.setPos(caster.getX(), caster.getEyeY() - .15, caster.getZ());
        Vec3 delta = target.getEyePosition().subtract(bolt.position());
        bolt.shoot(delta.x, delta.y + delta.horizontalDistance() * .1, delta.z, speed, 2);
        caster.level().addFreshEntity(bolt);
    }
    @Override protected boolean canHitEntity(Entity entity) {
        if(!super.canHitEntity(entity))return false;
        if(getOwner() instanceof LivingEntity owner && entity instanceof LivingEntity target
            && (owner.isAlliedTo(target) || !owner.canAttack(target)))return false;
        if(getType()==ModEntities.ROOT_SHARD || getType()==ModEntities.VINE_SEED)return !(entity instanceof ForestGuardianEntity);
        if(getOwner() instanceof MythicHostileEntity && entity instanceof MythicHostileEntity)return false;
        return true;
    }
    @Override protected void onHitEntity(EntityHitResult result) {
        super.onHitEntity(result);
        if (level() instanceof ServerLevel level && result.getEntity() instanceof LivingEntity target) {
            boolean rock = getType() == ModEntities.TROLL_BOULDER;
            float damage = getOwner() instanceof LivingEntity owner
                ? (float)owner.getAttributeValue(net.minecraft.world.entity.ai.attributes.Attributes.ATTACK_DAMAGE) : 4;
            boolean damaged=target.hurtServer(level, damageSources().thrown(this, getOwner()), damage);
            if(!damaged)return;
            if(getType()==ModEntities.ROOT_SHARD || getType()==ModEntities.VINE_SEED)
                target.addEffect(new MobEffectInstance(MobEffects.SLOWNESS,80,getType()==ModEntities.ROOT_SHARD?2:1),getOwner());
            else if(getType()==ModEntities.FIRE_BOLT || getType()==ModEntities.SHAMAN_BOLT)target.igniteForSeconds(2);
            else if(getType()==ModEntities.CRYSTAL_BOLT){
                target.addEffect(new MobEffectInstance(MobEffects.SLOWNESS,60,1),getOwner());
                var web=ModEntities.WEB_TRAP.create(level,EntitySpawnReason.TRIGGERED);
                if(web!=null && getOwner() instanceof LivingEntity caster){web.setOwner(caster);web.setPos(target.getX(),target.getY()+.1,target.getZ());level.addFreshEntity(web);}
            }
            else if(getType()==ModEntities.ICE_SPIKE)target.addEffect(new MobEffectInstance(MobEffects.SLOWNESS,80,2),getOwner());
            else if(getType()==ModEntities.DARK_BOLT){target.addEffect(new MobEffectInstance(MobEffects.WEAKNESS,100,0),getOwner());target.addEffect(new MobEffectInstance(MobEffects.DARKNESS,50,0),getOwner());}
            else if(getType()==ModEntities.SLIME_BUBBLE){target.addEffect(new MobEffectInstance(MobEffects.SLOWNESS,50,1),getOwner());target.setDeltaMovement(target.getDeltaMovement().add(0,.15,0));}
            else if(getType()==ModEntities.FEATHER_BOLT)target.knockback(.25,-getDeltaMovement().x,-getDeltaMovement().z);
            else if(!rock)target.addEffect(new MobEffectInstance(MobEffects.POISON,60,0),getOwner());
            else target.knockback(.7, -getDeltaMovement().x, -getDeltaMovement().z);
        }
    }
    @Override protected void onHit(HitResult result) {
        super.onHit(result);
        if (level() instanceof ServerLevel level) {
            com.mythicrealms.creatures.magic.SpellEffects.particles(level,
                getType()==ModEntities.TROLL_BOULDER?ParticleTypes.CLOUD:getType()==ModEntities.FIRE_BOLT?ParticleTypes.FLAME:
                getType()==ModEntities.ICE_SPIKE?ParticleTypes.SNOWFLAKE:getType()==ModEntities.DARK_BOLT?ParticleTypes.WITCH:ParticleTypes.HAPPY_VILLAGER,
                getX(),getY(),getZ(),5,.15);
            discard();
        }
    }
    @Override public void tick() {
        super.tick();
        if (!level().isClientSide() && tickCount > 100) discard();
        if(level() instanceof ServerLevel level && tickCount%6==0 && getType()!=ModEntities.TROLL_BOULDER) {
            var particle=getType()==ModEntities.FIRE_BOLT?ParticleTypes.FLAME:
                getType()==ModEntities.ICE_SPIKE?ParticleTypes.SNOWFLAKE:getType()==ModEntities.DARK_BOLT?ParticleTypes.WITCH:
                getType()==ModEntities.CRYSTAL_BOLT?ParticleTypes.END_ROD:ParticleTypes.HAPPY_VILLAGER;
            com.mythicrealms.creatures.magic.SpellEffects.particles(level,particle,getX(),getY(),getZ(),1,.05);
        }
    }
}
