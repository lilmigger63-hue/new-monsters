package com.mythicrealms.creatures.entity;

import com.mythicrealms.creatures.registry.ModEntities;
import net.minecraft.network.syncher.*;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.entity.*;
import net.minecraft.world.entity.ai.navigation.*;
import net.minecraft.world.level.Level;

public final class CrystalSpiderEntity extends MythicHostileEntity {
    private static final EntityDataAccessor<Boolean> CLIMBING=SynchedEntityData.defineId(CrystalSpiderEntity.class,EntityDataSerializers.BOOLEAN);
    public CrystalSpiderEntity(EntityType<? extends CrystalSpiderEntity> type,Level level){super(type,level);}
    @Override public CreatureKind kind(){return CreatureKind.CRYSTAL_SPIDER;}
    @Override protected PathNavigation createNavigation(Level level){return new WallClimberNavigation(this,level);}
    @Override protected void defineSynchedData(SynchedEntityData.Builder data){super.defineSynchedData(data);data.define(CLIMBING,false);}
    @Override public boolean onClimbable(){return entityData.get(CLIMBING);}
    @Override public void tick(){super.tick();if(!level().isClientSide())entityData.set(CLIMBING,horizontalCollision);}
    @Override public boolean ranged(){return true;}
    @Override public void performAttack(ServerLevel level,LivingEntity target){if(distanceToSqr(target)<169)CreatureProjectile.launch(ModEntities.CRYSTAL_BOLT,this,target,1.2f);}
}
