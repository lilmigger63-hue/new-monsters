package com.mythicrealms.creatures.entity;

import com.mythicrealms.creatures.config.CreatureConfig;
import com.mythicrealms.creatures.entity.mount.MythicMountEntity;
import com.mythicrealms.creatures.registry.ModEntities;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.sounds.*;
import net.minecraft.world.*;
import net.minecraft.world.entity.*;
import net.minecraft.world.entity.ai.goal.target.NearestAttackableTargetGoal;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.*;
import net.minecraft.world.level.*;

public final class WildWyvernEntity extends MythicMountEntity {
    public WildWyvernEntity(EntityType<? extends WildWyvernEntity> type,Level level){super(type,level);}
    @Override public CreatureKind kind(){return CreatureKind.WILD_WYVERN;}
    @Override public Item tamingItem(){return Items.FERMENTED_SPIDER_EYE;}
    @Override public boolean canBeTamed(){return isRareVariant();}
    @Override protected void registerGoals(){
        super.registerGoals();
        targetSelector.addGoal(4,new NearestAttackableTargetGoal<Player>(this,Player.class,true){
            @Override public boolean canUse(){return !isTame() && super.canUse();}
            @Override public boolean canContinueToUse(){return !isTame() && super.canContinueToUse();}
        });
    }
    @Override public SpawnGroupData finalizeSpawn(ServerLevelAccessor level,DifficultyInstance difficulty,EntitySpawnReason reason,SpawnGroupData data){
        setRareVariant(getRandom().nextInt(CreatureConfig.INSTANCE.rareWyvernChance)==0);
        return super.finalizeSpawn(level,difficulty,reason,data);
    }
    @Override public void performAttack(ServerLevel level,LivingEntity target){
        if(canAttack(target) && distanceToSqr(target)<100 && getSensing().hasLineOfSight(target)){
            CreatureProjectile.launch(ModEntities.POISON_BREATH,this,target,1.2f);
            playSound(SoundEvents.ENDER_DRAGON_GROWL,.5f,1.5f);
        }
    }
    @Override protected SoundEvent getAmbientSound(){return SoundEvents.ENDER_DRAGON_AMBIENT;}
}
