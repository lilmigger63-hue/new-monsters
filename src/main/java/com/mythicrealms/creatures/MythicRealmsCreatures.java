package com.mythicrealms.creatures;

import net.fabricmc.api.ModInitializer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public final class MythicRealmsCreatures implements ModInitializer {
    public static final String MOD_ID = "mythic_realms_creatures";
    public static final Logger LOGGER = LoggerFactory.getLogger(MOD_ID);

    @Override
    public void onInitialize() {
        LOGGER.info("Mythic Realms: Creatures development foundation initialized");
    }
}
