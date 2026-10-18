package com.mythicrealms.creatures.entity;

import com.mythicrealms.creatures.entity.mount.MythicMountEntity;
import com.mythicrealms.creatures.magic.SpellEffects;
import net.minecraft.core.particles.ParticleTypes;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.sounds.*;
import net.minecraft.world.entity.*;
import net.minecraft.world.item.*;
import net.minecraft.world.level.Level;

public final class MoonStagEntity extends MythicMountEntity {
    public MoonStagEntity(EntityType<? extends MoonStagEntity> type,Level level){super(type,level);}
    @Override public CreatureKind kind(){return CreatureKind.MOON_STAG;}
    @Override public boolean canFly(){return false;}
    @Override public Item tamingItem(){return Items.GOLDEN_CARROT;}
    @Override public Item healingItem(){return Items.GLOW_BERRIES;}
    @Override protected SoundEvent getAmbientSound(){return SoundEvents.HORSE_AMBIENT;}
    @Override protected void customServerAiStep(ServerLevel level){
        super.customServerAiStep(level);
        if(isTame() && tickCount%240==0 && level.getDayTime()%24000>=13000 && getOwner()!=null && distanceToSqr(getOwner())<36){
            var owner=getOwner();if(owner.getHealth()<owner.getMaxHealth()){
                owner.heal(2);triggerAnim("action","cast");SpellEffects.particles(level,ParticleTypes.END_ROD,getX(),getY()+1,getZ(),6,.5);
            }
        }
    }
}
