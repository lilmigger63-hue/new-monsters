package com.mythicrealms.creatures.config;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.mythicrealms.creatures.MythicRealmsCreatures;
import com.mythicrealms.creatures.entity.CreatureKind;
import net.fabricmc.loader.api.FabricLoader;
import java.nio.file.Files;
import java.nio.file.StandardOpenOption;
import java.util.LinkedHashMap;
import java.util.Map;

public final class CreatureConfig {
    public static CreatureConfig INSTANCE = new CreatureConfig();
    public double difficultyMultiplier = 1;
    public Map<String, SpawnRule> spawning = new LinkedHashMap<>();
    public static final class SpawnRule {
        public boolean enabled = true;
        public int weight, minGroup = 1, maxGroup = 2, frequency = 1;
        SpawnRule(int weight) { this.weight = weight; }
    }
    public CreatureConfig() {
        for (CreatureKind kind : CreatureKind.values()) spawning.put(kind.id, new SpawnRule(kind.spawnWeight));
    }
    public static void load() {
        var path = FabricLoader.getInstance().getConfigDir().resolve("mythic_realms_creatures.json");
        Gson gson = new GsonBuilder().setPrettyPrinting().create();
        try {
            if (!Files.exists(path)) {
                Files.createDirectories(path.getParent());
                Files.writeString(path, gson.toJson(INSTANCE), StandardOpenOption.CREATE_NEW);
            } else {
                var loaded = gson.fromJson(Files.readString(path), CreatureConfig.class);
                if (loaded == null || !Double.isFinite(loaded.difficultyMultiplier)
                    || loaded.difficultyMultiplier < .25 || loaded.difficultyMultiplier > 4 || loaded.spawning == null)
                    throw new IllegalArgumentException("Invalid difficulty or spawning settings");
                for (CreatureKind kind : CreatureKind.values()) {
                    var rule = loaded.spawning.get(kind.id);
                    if (rule == null) loaded.spawning.put(kind.id, new SpawnRule(kind.spawnWeight));
                    else if (rule.weight < 0 || rule.weight > 100 || rule.minGroup < 1
                        || rule.maxGroup < rule.minGroup || rule.maxGroup > 6 || rule.frequency < 1 || rule.frequency > 1000)
                        throw new IllegalArgumentException("Invalid spawn settings for " + kind.id);
                }
                INSTANCE = loaded;
            }
        } catch (Exception e) {
            MythicRealmsCreatures.LOGGER.error("Unable to load creature config; using defaults and preserving the file", e);
        }
    }
}
