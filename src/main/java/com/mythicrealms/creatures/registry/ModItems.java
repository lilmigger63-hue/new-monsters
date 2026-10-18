package com.mythicrealms.creatures.registry;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Function;
import com.mythicrealms.creatures.MythicRealmsCreatures;
import net.fabricmc.fabric.api.itemgroup.v1.ItemGroupEvents;
import net.minecraft.core.Registry;
import net.minecraft.core.particles.ParticleTypes;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.core.registries.Registries;
import net.minecraft.resources.ResourceKey;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.tags.BlockTags;
import net.minecraft.tags.TagKey;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.sounds.SoundEvents;
import net.minecraft.sounds.SoundSource;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.InteractionResult;
import net.minecraft.world.effect.MobEffectInstance;
import net.minecraft.world.effect.MobEffects;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.food.FoodProperties;
import net.minecraft.world.item.*;
import net.minecraft.world.level.Level;

/** Small survival progression, registered before creature factories can request taming foods. */
public final class ModItems {
    private static final List<Item> MATERIALS = new ArrayList<>();
    private static final List<Item> EQUIPMENT = new ArrayList<>();
    private static final List<Item> FOODS = new ArrayList<>();
    private static final ToolMaterial ORC_MATERIAL = new ToolMaterial(BlockTags.INCORRECT_FOR_IRON_TOOL,
        480, 6, 2, 14, TagKey.create(Registries.ITEM, id("orc_steel_repair")));

    public static final Item GOBLIN_SCRAP = material("goblin_scrap");
    public static final Item ORC_STEEL = material("orc_steel");
    public static final Item MINOTAUR_HORN = material("minotaur_horn");
    public static final Item TROLL_HEARTSTONE = material("troll_heartstone");
    public static final Item LIVING_WOOD = material("living_wood");
    public static final Item FOREST_ESSENCE = material("forest_essence");
    public static final Item GRIFFIN_FEATHER = material("griffin_feather");
    public static final Item DIRE_FANG = material("dire_fang");
    public static final Item WYVERN_SCALE = material("wyvern_scale");
    public static final Item BASILISK_SCALE = material("basilisk_scale");
    public static final Item CRYSTAL_SHARD = material("crystal_shard");
    public static final Item SHADOW_ESSENCE = material("shadow_essence");
    public static final Item FROST_ESSENCE = material("frost_essence");
    public static final Item INFERNAL_EMBER = material("infernal_ember");
    public static final Item SLIME_PEARL = material("slime_pearl");

    public static final Item SUNSEED_BISCUIT = food("sunseed_biscuit", 5, .6f);
    public static final Item HEARTY_MEAT = food("hearty_meat", 8, .8f);
    public static final Item MOONBLOSSOM = food("moonblossom", 3, .5f);
    public static final Item VENOMOUS_MORSEL = food("venomous_morsel", 4, .3f);

    public static final Item GRIFFIN_SADDLE = equipment("griffin_saddle", p -> new Item(p.stacksTo(1)));
    public static final Item WYVERN_HARNESS = equipment("wyvern_harness", p -> new Item(p.stacksTo(1).fireResistant()));
    public static final Item CRYSTAL_FANG_SWORD = equipment("crystal_fang_sword", p -> new Item(p
        .sword(ToolMaterial.DIAMOND, 3, -2.4f).durability(720).repairable(CRYSTAL_SHARD)));
    public static final Item ORC_WAR_AXE = equipment("orc_war_axe", p -> new AxeItem(ORC_MATERIAL, 6, -3.2f, p));
    public static final Item BASILISK_SPEAR = equipment("basilisk_spear", p -> new Item(p
        .sword(ToolMaterial.IRON, 3, -2.8f).durability(420).repairable(BASILISK_SCALE)));
    public static final Item FROSTBOUND_STAFF = equipment("frostbound_staff", p -> new FrostStaffItem(p
        .sword(ToolMaterial.WOOD, 3, -2.6f).durability(260).repairable(FROST_ESSENCE).rarity(Rarity.UNCOMMON)));
    public static final Item TWILIGHT_RELIC = equipment("twilight_relic", p -> new Item(p.stacksTo(1).rarity(Rarity.RARE)));

    private ModItems() { }

    private static Item register(String name, Function<Item.Properties, Item> factory, List<Item> collection) {
        var key = ResourceKey.create(Registries.ITEM, id(name));
        Item item = Registry.register(BuiltInRegistries.ITEM, key, factory.apply(new Item.Properties().setId(key)));
        collection.add(item);
        return item;
    }

    private static Item material(String name) { return register(name, Item::new, MATERIALS); }
    private static ResourceLocation id(String name) {
        return ResourceLocation.fromNamespaceAndPath(MythicRealmsCreatures.MOD_ID, name);
    }
    private static Item food(String name, int nutrition, float saturationModifier) {
        return register(name, p -> new Item(p.food(new FoodProperties(nutrition, nutrition * saturationModifier * 2, false))), FOODS);
    }
    private static Item equipment(String name, Function<Item.Properties, Item> factory) {
        return register(name, factory, EQUIPMENT);
    }

    public static List<Item> all() {
        var items = new ArrayList<Item>(MATERIALS);
        items.addAll(FOODS);
        items.addAll(EQUIPMENT);
        return List.copyOf(items);
    }

    public static void initialize() {
        ItemGroupEvents.modifyEntriesEvent(CreativeModeTabs.INGREDIENTS).register(entries -> MATERIALS.forEach(entries::accept));
        ItemGroupEvents.modifyEntriesEvent(CreativeModeTabs.FOOD_AND_DRINKS).register(entries -> FOODS.forEach(entries::accept));
        ItemGroupEvents.modifyEntriesEvent(CreativeModeTabs.COMBAT).register(entries -> {
            entries.accept(CRYSTAL_FANG_SWORD); entries.accept(ORC_WAR_AXE);
            entries.accept(BASILISK_SPEAR); entries.accept(FROSTBOUND_STAFF);
        });
        ItemGroupEvents.modifyEntriesEvent(CreativeModeTabs.TOOLS_AND_UTILITIES).register(entries -> {
            entries.accept(GRIFFIN_SADDLE); entries.accept(WYVERN_HARNESS); entries.accept(TWILIGHT_RELIC);
        });
    }

    /** Vanilla cooldown and durability; no player attack hooks or client-only classes. */
    private static final class FrostStaffItem extends Item {
        private FrostStaffItem(Properties properties) { super(properties); }

        @Override
        public InteractionResult use(Level level, Player player, InteractionHand hand) {
            var stack = player.getItemInHand(hand);
            if (player.getCooldowns().isOnCooldown(stack)) return InteractionResult.FAIL;
            if (level instanceof ServerLevel server) {
                player.addEffect(new MobEffectInstance(MobEffects.RESISTANCE, 100, 0));
                player.getCooldowns().addCooldown(stack, 240);
                stack.hurtAndBreak(3, player, hand);
                com.mythicrealms.creatures.magic.SpellEffects.particles(server,ParticleTypes.SNOWFLAKE,
                    player.getX(),player.getY()+1,player.getZ(),24,.65);
                server.playSound(null, player.blockPosition(), SoundEvents.AMETHYST_BLOCK_CHIME, SoundSource.PLAYERS, .8f, .65f);
            }
            return InteractionResult.SUCCESS;
        }
    }
}
