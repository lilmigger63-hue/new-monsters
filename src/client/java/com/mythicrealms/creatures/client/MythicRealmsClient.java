package com.mythicrealms.creatures.client;

import com.mythicrealms.creatures.entity.MythicHostileEntity;
import com.mythicrealms.creatures.registry.ModEntities;
import net.fabricmc.api.ClientModInitializer;
import net.fabricmc.fabric.api.client.rendering.v1.EntityRendererRegistry;
import net.minecraft.client.renderer.entity.ThrownItemRenderer;
import net.minecraft.client.renderer.entity.EntityRendererProvider;
import net.minecraft.client.renderer.entity.state.LivingEntityRenderState;
import net.minecraft.world.entity.EntityType;
import software.bernie.geckolib.renderer.GeoEntityRenderer;
import software.bernie.geckolib.renderer.base.GeoRenderState;

public final class MythicRealmsClient implements ClientModInitializer {
    @Override public void onInitializeClient() {
        register(ModEntities.GOBLIN_SCOUT, .35f);
        register(ModEntities.GOBLIN_SHAMAN, .35f);
        register(ModEntities.ORC_WARRIOR, .5f);
        register(ModEntities.MINOTAUR, .75f);
        register(ModEntities.STONE_TROLL, .9f);
        EntityRendererRegistry.register(ModEntities.SHAMAN_BOLT, context -> new ThrownItemRenderer<>(context, .65f, true));
        EntityRendererRegistry.register(ModEntities.TROLL_BOULDER, context -> new ThrownItemRenderer<>(context, 1.8f, false));
    }
    private static <T extends MythicHostileEntity> void register(EntityType<T> type, float shadow) {
        EntityRendererRegistry.register(type, context -> new CreatureRenderer<>(context, type, shadow));
    }
    private static final class CreatureRenderer<T extends MythicHostileEntity, R extends LivingEntityRenderState & GeoRenderState>
            extends GeoEntityRenderer<T, R> {
        CreatureRenderer(EntityRendererProvider.Context context, EntityType<T> type, float shadow) {
            super(context, type); this.shadowRadius = shadow;
        }
        // The model supplies its own death pose; avoid applying a second vanilla roll.
        @Override protected float getDeathMaxRotation(GeoRenderState state) { return 0; }
    }
}
