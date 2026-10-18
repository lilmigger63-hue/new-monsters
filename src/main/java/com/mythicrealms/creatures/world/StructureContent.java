package com.mythicrealms.creatures.world;

import com.mojang.serialization.Codec;
import com.mojang.serialization.MapCodec;
import com.mythicrealms.creatures.config.CreatureConfig;
import net.fabricmc.fabric.api.resource.conditions.v1.ResourceCondition;
import net.fabricmc.fabric.api.resource.conditions.v1.ResourceConditionType;
import net.fabricmc.fabric.api.resource.conditions.v1.ResourceConditions;
import net.minecraft.resources.RegistryOps;
import net.minecraft.resources.ResourceLocation;

/** Data-driven jigsaw generation; no chunk-load handlers or fixed terrain heights. */
public final class StructureContent {
    public static final java.util.List<String> STRUCTURES = java.util.List.of(
        "goblin_watchtower", "forest_shrine", "grave_crypt", "wyvern_nest");
    public static final ResourceConditionType<Enabled> ENABLED = ResourceConditionType.create(
        ResourceLocation.fromNamespaceAndPath("mythic_realms_creatures", "structure_enabled"), Enabled.CODEC);

    private StructureContent() {}

    public static void initialize() {
        ResourceConditions.register(ENABLED);
    }

    /** Applied to structure sets, leaving templates and /place structure available for administrators. */
    public record Enabled(String structure) implements ResourceCondition {
        public static final MapCodec<Enabled> CODEC = Codec.STRING.fieldOf("structure")
            .xmap(Enabled::new, Enabled::structure);
        @Override public ResourceConditionType<?> getType() { return ENABLED; }
        @Override public boolean test(RegistryOps.RegistryInfoLookup registryInfo) {
            return STRUCTURES.contains(structure) && CreatureConfig.INSTANCE.structuresEnabled
                && Boolean.TRUE.equals(CreatureConfig.INSTANCE.structures.getOrDefault(structure, true));
        }
    }
}
