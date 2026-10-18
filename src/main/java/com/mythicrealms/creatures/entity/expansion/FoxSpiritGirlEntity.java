package com.mythicrealms.creatures.entity.expansion;

import com.mythicrealms.creatures.entity.CreatureKind;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.level.Level;

public final class FoxSpiritGirlEntity extends ShamanProfileEntity {
    public FoxSpiritGirlEntity(EntityType<? extends FoxSpiritGirlEntity> type, Level level) { super(type, level); }
    @Override public CreatureKind kind() { return CreatureKind.FOX_SPIRIT_GIRL; }
}
