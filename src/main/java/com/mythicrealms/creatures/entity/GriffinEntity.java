package com.mythicrealms.creatures.entity;

import com.mythicrealms.creatures.entity.mount.MythicMountEntity;
import net.minecraft.sounds.*;
import net.minecraft.world.entity.*;
import net.minecraft.world.item.*;
import net.minecraft.world.level.Level;

public final class GriffinEntity extends MythicMountEntity {
    public GriffinEntity(EntityType<? extends GriffinEntity> type,Level level){super(type,level);}
    @Override public CreatureKind kind(){return CreatureKind.GRIFFIN;}
    @Override public Item tamingItem(){return Items.RABBIT;}
    @Override protected SoundEvent getAmbientSound(){return SoundEvents.PARROT_AMBIENT;}
}
