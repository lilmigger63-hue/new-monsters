package com.mythicrealms.creatures.entity.expansion;

import com.mythicrealms.creatures.entity.CreatureKind;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.level.Level;

public final class SuccubusEntity extends DemonProfileEntity {
    public SuccubusEntity(EntityType<? extends SuccubusEntity> type, Level level) { super(type, level); }
    @Override public CreatureKind kind() { return CreatureKind.SUCCUBUS; }
}
