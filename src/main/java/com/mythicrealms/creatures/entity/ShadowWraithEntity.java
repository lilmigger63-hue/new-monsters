package com.mythicrealms.creatures.entity;

import com.mythicrealms.creatures.registry.ModEntities;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.sounds.*;
import net.minecraft.world.entity.*;
import net.minecraft.world.level.Level;

public final class ShadowWraithEntity extends AerialHostileEntity {
    public ShadowWraithEntity(EntityType<? extends ShadowWraithEntity> type,Level level){super(type,level);}
    @Override public CreatureKind kind(){return CreatureKind.SHADOW_WRAITH;}
    @Override public boolean ranged(){return true;}
    @Override public void performAttack(ServerLevel level,LivingEntity target){if(distanceToSqr(target)<169)CreatureProjectile.launch(ModEntities.DARK_BOLT,this,target,1.05f);}
    @Override protected SoundEvent getAmbientSound(){return SoundEvents.SOUL_ESCAPE.value();}
}
