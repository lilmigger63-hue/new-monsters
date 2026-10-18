package com.mythicrealms.creatures.client;

import net.minecraft.world.entity.Mob;
import net.minecraft.client.renderer.RenderType;
import software.bernie.geckolib.renderer.layer.AutoGlowingGeoLayer;
import software.bernie.geckolib.animatable.GeoEntity;
import com.mythicrealms.creatures.entity.mount.MythicMountEntity;
import software.bernie.geckolib.model.DefaultedEntityGeoModel;
import software.bernie.geckolib.constant.dataticket.DataTicket;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.ResourceLocation;
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
    // Only species whose mapped UV faces contribute emissive pixels need a second mesh pass.
    private static final java.util.Set<String> EMISSIVE_SPECIES = java.util.Set.of(
        "stone_troll", "goblin_shaman", "ancient_treant", "forest_dryad", "cave_basilisk", "crystal_spider", "shadow_wraith", "grave_knight", "flame_imp", "frost_elemental", "moon_stag", "harpy", "demon_sorceress", "ender_dragon_girl", "vampire", "valkyrie", "fox_spirit_girl", "anubis", "cyclops", "dhampir", "succubus");

    @Override public void onInitializeClient() {
        register(ModEntities.GOBLIN_SCOUT, .35f);
        register(ModEntities.GOBLIN_SHAMAN, .35f);
        register(ModEntities.ORC_WARRIOR, .5f);
        register(ModEntities.MINOTAUR, .75f);
        register(ModEntities.STONE_TROLL, .9f);
        register(ModEntities.ANCIENT_TREANT,1.1f);
        register(ModEntities.FOREST_DRYAD,.35f);
        register(ModEntities.GRIFFIN,.8f);
        register(ModEntities.DIRE_WOLF,.6f);
        register(ModEntities.WILD_WYVERN,.95f);
        register(ModEntities.CAVE_BASILISK,.6f);
        register(ModEntities.CRYSTAL_SPIDER,.7f);
        register(ModEntities.SHADOW_WRAITH,.35f);
        register(ModEntities.GRAVE_KNIGHT,.4f);
        register(ModEntities.FLAME_IMP,.25f);
        register(ModEntities.FROST_ELEMENTAL,.55f);
        register(ModEntities.MOON_STAG,.55f);
        register(ModEntities.SLIME_MAIDEN,.4f);
        register(ModEntities.HARPY,.45f);
        register(ModEntities.DEMON_SORCERESS,.35f);
        register(ModEntities.ENDER_DRAGON_GIRL,0.45f);
        register(ModEntities.VAMPIRE,0.35f);
        register(ModEntities.HOLSTAURUS,0.4f);
        register(ModEntities.CENTAUR,0.65f);
        register(ModEntities.SAHUAGIN,0.35f);
        register(ModEntities.VALKYRIE,0.4f);
        register(ModEntities.FOX_SPIRIT_GIRL,0.4f);
        register(ModEntities.ANUBIS,0.35f);
        register(ModEntities.KOBOLD,0.3f);
        register(ModEntities.CYCLOPS,0.45f);
        register(ModEntities.DHAMPIR,0.35f);
        register(ModEntities.SUCCUBUS,0.4f);
        register(ModEntities.WERECAT,0.35f);
        EntityRendererRegistry.register(ModEntities.CRYSTAL_BOLT, context -> new ThrownItemRenderer<>(context,.65f,true));
        EntityRendererRegistry.register(ModEntities.DARK_BOLT, context -> new ThrownItemRenderer<>(context,.7f,true));
        EntityRendererRegistry.register(ModEntities.FIRE_BOLT, context -> new ThrownItemRenderer<>(context,.6f,true));
        EntityRendererRegistry.register(ModEntities.ICE_SPIKE, context -> new ThrownItemRenderer<>(context,.8f,true));
        EntityRendererRegistry.register(ModEntities.FEATHER_BOLT, context -> new ThrownItemRenderer<>(context,.8f,false));
        EntityRendererRegistry.register(ModEntities.SLIME_BUBBLE, context -> new ThrownItemRenderer<>(context,.9f,false));
        EntityRendererRegistry.register(ModEntities.WEB_TRAP, context -> new ThrownItemRenderer<>(context,1.5f,false));
        EntityRendererRegistry.register(ModEntities.ROOT_SHARD, context -> new ThrownItemRenderer<>(context, 1.2f, false));
        EntityRendererRegistry.register(ModEntities.VINE_SEED, context -> new ThrownItemRenderer<>(context, .7f, true));
        EntityRendererRegistry.register(ModEntities.POISON_BREATH, context -> new ThrownItemRenderer<>(context, .8f, true));
        EntityRendererRegistry.register(ModEntities.SHAMAN_BOLT, context -> new ThrownItemRenderer<>(context, .65f, true));
        EntityRendererRegistry.register(ModEntities.TROLL_BOULDER, context -> new ThrownItemRenderer<>(context, 1.8f, false));
    }
    private static <T extends Mob & GeoEntity> void register(EntityType<T> type, float shadow) {
        EntityRendererRegistry.register(type, context -> new CreatureRenderer<>(context, type, shadow));
    }
    private static final class CreatureModel<T extends Mob & GeoEntity> extends DefaultedEntityGeoModel<T> {
        private static final DataTicket<Boolean> TAMED=DataTicket.create("mythic_mount_tamed",Boolean.class);
        private static final DataTicket<Boolean> RARE=DataTicket.create("mythic_mount_rare",Boolean.class);
        private final ResourceLocation texture, tamedTexture, rareTexture;
        CreatureModel(EntityType<T> type){
            super(BuiltInRegistries.ENTITY_TYPE.getKey(type));
            var id=BuiltInRegistries.ENTITY_TYPE.getKey(type);
            String path="textures/entity/"+id.getPath();
            texture=id.withPath(path+".png");
            tamedTexture=id.withPath(path+"_tamed.png");
            rareTexture=id.withPath(path+"_rare.png");
        }
        @Override public void addAdditionalStateData(T entity,GeoRenderState state){
            super.addAdditionalStateData(entity,state);
            state.addGeckolibData(TAMED,entity instanceof MythicMountEntity mount && mount.isTame());
            state.addGeckolibData(RARE,entity instanceof MythicMountEntity mount && mount.isRareVariant());
        }
        @Override public ResourceLocation getTextureResource(GeoRenderState state){
            return state.getOrDefaultGeckolibData(TAMED,false)?tamedTexture:
                state.getOrDefaultGeckolibData(RARE,false)?rareTexture:texture;
        }
    }
    private static final class CreatureRenderer<T extends Mob & GeoEntity, R extends LivingEntityRenderState & GeoRenderState>
            extends GeoEntityRenderer<T, R> {
        private final boolean translucent;
        CreatureRenderer(EntityRendererProvider.Context context, EntityType<T> type, float shadow) {
            super(context, new CreatureModel<T>(type)); this.shadowRadius = shadow;
            String id=BuiltInRegistries.ENTITY_TYPE.getKey(type).getPath();
            translucent=id.equals("shadow_wraith") || id.equals("slime_maiden");
            if (EMISSIVE_SPECIES.contains(id))
                withRenderLayer(new AutoGlowingGeoLayer<>(this));
        }
        @Override public RenderType getRenderType(R state,ResourceLocation texture) {
            return translucent && !state.isInvisible ? RenderType.entityTranslucent(texture) : super.getRenderType(state,texture);
        }
        // The model supplies its own death pose; avoid applying a second vanilla roll.
        @Override protected float getDeathMaxRotation(GeoRenderState state) { return 0; }
    }
}
