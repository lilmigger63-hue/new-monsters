package com.mythicrealms.creatures.compat;

import com.mythicrealms.creatures.MythicRealmsCreatures;
import net.fabricmc.loader.api.FabricLoader;

/** Integration is entirely data-driven so Better Combat is never a class-loading dependency. */
public final class BetterCombatCompat {
    private BetterCombatCompat() { }

    public static boolean isLoaded() { return FabricLoader.getInstance().isModLoaded("bettercombat"); }

    public static void initialize() {
        if (isLoaded()) MythicRealmsCreatures.LOGGER.info("Better Combat detected: sword, axe, spear and staff presets enabled");
    }
}
