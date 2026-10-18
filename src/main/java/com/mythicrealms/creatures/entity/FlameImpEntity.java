package com.mythicrealms.creatures.entity;

import com.mythicrealms.creatures.registry.ModEntities;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.sounds.*;
import net.minecraft.world.entity.*;
import net.minecraft.world.level.Level;

public final class FlameImpEntity extends AerialHostileEntity {
    public FlameImpEntity(EntityType<? extends FlameImpEntity> type,Level level){super(type,level);}
    @Override public CreatureKind kind(){return CreatureKind.FLAME_IMP;}
    @Override public boolean ranged(){return true;}
    @Override public void performAttack(ServerLevel level,LivingEntity target){if(distanceToSqr(target)<169)CreatureProjectile.launch(ModEntities.FIRE_BOLT,this,target,1.15f);}
    @Override protected SoundEvent getAmbientSound(){return SoundEvents.BLAZE_AMBIENT;}
}
