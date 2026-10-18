package com.mythicrealms.creatures;

import net.fabricmc.api.ModInitializer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public final class MythicRealmsCreatures implements ModInitializer {
    public static final String MOD_ID = "mythic_realms_creatures";
    public static final Logger LOGGER = LoggerFactory.getLogger(MOD_ID);

    @Override
    public void onInitialize() {
        com.mythicrealms.creatures.config.CreatureConfig.load();
        com.mythicrealms.creatures.registry.ModItems.initialize();
        com.mythicrealms.creatures.world.StructureContent.initialize();
        com.mythicrealms.creatures.compat.BetterCombatCompat.initialize();
        com.mythicrealms.creatures.registry.ModEntities.initialize();
        LOGGER.info("Mythic Realms: Creatures initialized: 20 creature species");
    }
}
