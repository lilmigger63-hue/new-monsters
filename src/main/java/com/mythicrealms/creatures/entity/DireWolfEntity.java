package com.mythicrealms.creatures.entity;

import com.mythicrealms.creatures.entity.mount.MythicMountEntity;
import net.minecraft.sounds.*;
import net.minecraft.world.entity.*;
import net.minecraft.world.item.*;
import net.minecraft.world.level.Level;

public final class DireWolfEntity extends MythicMountEntity {
    public DireWolfEntity(EntityType<? extends DireWolfEntity> type,Level level){super(type,level);}
    @Override public CreatureKind kind(){return CreatureKind.DIRE_WOLF;}
    @Override public Item tamingItem(){return Items.BONE;}
    @Override public Item healingItem(){return Items.BEEF;}
    @Override protected SoundEvent getAmbientSound(){return SoundEvents.WOLF_SOUNDS.get(net.minecraft.world.entity.animal.wolf.WolfSoundVariants.SoundSet.BIG).ambientSound().value();}
}
