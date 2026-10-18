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
    public double magicParticleIntensity = 1;
    public int aiUpdateInterval = 10;
    public boolean structuresEnabled = true;
    public Map<String,Boolean> structures = new LinkedHashMap<>(Map.of("goblin_watchtower",true,"forest_shrine",true,"grave_crypt",true,"wyvern_nest",true));
    public double mountSpeedMultiplier = 1;
    public double flightSpeedMultiplier = 1;
    public int tamingDifficulty = 3;
    public int rareWyvernChance = 20;
    public Map<String, SpawnRule> spawning = new LinkedHashMap<>();
    public static final class SpawnRule {
        public boolean enabled = true;
        public int weight, minGroup = 1, maxGroup = 2, frequency = 1;
        public double difficultyMultiplier = 1;
        public java.util.List<String> dimensions = new java.util.ArrayList<>(java.util.List.of("minecraft:overworld"));
        public java.util.List<String> biomes = new java.util.ArrayList<>();
        public SpawnRule() { }
        SpawnRule(int weight) { this.weight = weight; }
        SpawnRule(CreatureKind kind) {
            weight=kind.spawnWeight;
            if(kind==CreatureKind.FLAME_IMP || kind==CreatureKind.DEMON_SORCERESS)dimensions=new java.util.ArrayList<>(java.util.List.of("minecraft:the_nether"));
        }
    }
    public CreatureConfig() {
        for (CreatureKind kind : CreatureKind.values()) spawning.put(kind.id, new SpawnRule(kind));
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
                    || !Double.isFinite(loaded.magicParticleIntensity) || loaded.magicParticleIntensity<0 || loaded.magicParticleIntensity>2
                    || loaded.aiUpdateInterval<2 || loaded.aiUpdateInterval>40 || loaded.structures==null
                    || loaded.difficultyMultiplier < .25 || loaded.difficultyMultiplier > 4 || loaded.spawning == null
                    || !Double.isFinite(loaded.mountSpeedMultiplier) || loaded.mountSpeedMultiplier < .25 || loaded.mountSpeedMultiplier > 2
                    || !Double.isFinite(loaded.flightSpeedMultiplier) || loaded.flightSpeedMultiplier < .25 || loaded.flightSpeedMultiplier > 2
                    || loaded.tamingDifficulty < 1 || loaded.tamingDifficulty > 100
                    || loaded.rareWyvernChance < 1 || loaded.rareWyvernChance > 1000)
                    throw new IllegalArgumentException("Invalid difficulty or spawning settings");
                for (CreatureKind kind : CreatureKind.values()) {
                    var rule = loaded.spawning.get(kind.id);
                    if (rule == null) loaded.spawning.put(kind.id, new SpawnRule(kind));
                    else if (rule.weight < 0 || rule.weight > 100 || rule.minGroup < 1
                        || rule.maxGroup < rule.minGroup || rule.maxGroup > 6 || rule.frequency < 1 || rule.frequency > 1000 || !Double.isFinite(rule.difficultyMultiplier)
                        || rule.difficultyMultiplier<.25 || rule.difficultyMultiplier>4 || rule.dimensions==null || rule.biomes==null
                        || rule.dimensions.stream().anyMatch(id -> net.minecraft.resources.ResourceLocation.tryParse(id)==null)
                        || rule.biomes.stream().anyMatch(id -> net.minecraft.resources.ResourceLocation.tryParse(id.startsWith("#")?id.substring(1):id)==null))
                        throw new IllegalArgumentException("Invalid spawn settings for " + kind.id);
                }
                INSTANCE = loaded;
            }
        } catch (Exception e) {
            MythicRealmsCreatures.LOGGER.error("Unable to load creature config; using defaults and preserving the file", e);
        }
    }
}
