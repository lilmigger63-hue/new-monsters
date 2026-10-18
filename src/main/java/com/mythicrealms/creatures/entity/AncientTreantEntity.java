package com.mythicrealms.creatures.entity;

import com.mythicrealms.creatures.registry.ModEntities;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.entity.*;
import net.minecraft.world.level.Level;

public final class AncientTreantEntity extends ForestGuardianEntity {
    public AncientTreantEntity(EntityType<? extends AncientTreantEntity> type,Level level){super(type,level);}
    @Override public CreatureKind kind(){return CreatureKind.ANCIENT_TREANT;}
    @Override public void performAttack(ServerLevel level,LivingEntity target){
        CreatureProjectile.launch(ModEntities.ROOT_SHARD,this,target,1.05f);
    }
}
