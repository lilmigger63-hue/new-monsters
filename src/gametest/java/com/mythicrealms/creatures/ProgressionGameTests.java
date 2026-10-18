package com.mythicrealms.creatures;

import java.util.List;
import java.util.Map;
import com.mythicrealms.creatures.compat.BetterCombatCompat;
import com.mythicrealms.creatures.registry.ModEntities;
import com.mythicrealms.creatures.registry.ModItems;
import net.fabricmc.fabric.api.gametest.v1.GameTest;
import net.minecraft.core.component.DataComponents;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.core.registries.Registries;
import net.minecraft.gametest.framework.GameTestHelper;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.ResourceKey;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.effect.MobEffects;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Items;
import net.minecraft.world.item.crafting.CraftingInput;
import net.minecraft.world.item.crafting.RecipeType;
import net.minecraft.world.level.GameType;
import net.minecraft.world.level.storage.loot.LootParams;
import net.minecraft.world.level.storage.loot.parameters.LootContextParams;
import net.minecraft.world.level.storage.loot.parameters.LootContextParamSets;

public final class ProgressionGameTests {
    private static void check(GameTestHelper helper, boolean condition, String message) {
        helper.assertTrue(condition, Component.literal(message));
    }

    @GameTest
    public void progressionItemsRegisterAndRecipesLoad(GameTestHelper helper) {
        check(helper, ModItems.all().size() == 26, "26 progression items");
        for (Item item : ModItems.all()) {
            var id = BuiltInRegistries.ITEM.getKey(item);
            check(helper, id.getNamespace().equals(MythicRealmsCreatures.MOD_ID), "registered custom item " + id);
            check(helper, item != Items.AIR, "item is not fallback air");
        }
        for (String recipe : List.of("sunseed_biscuit", "hearty_meat", "moonblossom", "venomous_morsel",
                "griffin_saddle", "wyvern_harness", "crystal_fang_sword", "orc_war_axe", "basilisk_spear",
                "frostbound_staff", "twilight_relic", "salvaged_iron", "living_wood_planks", "forest_bonemeal")) {
            check(helper, helper.getLevel().getServer().getRecipeManager()
                .byKey(ResourceKey.create(Registries.RECIPE, ModEntities.id(recipe))).isPresent(), "loaded recipe " + recipe);
        }
        for (Item food : List.of(ModItems.SUNSEED_BISCUIT, ModItems.HEARTY_MEAT, ModItems.MOONBLOSSOM, ModItems.VENOMOUS_MORSEL)) {
            check(helper, new ItemStack(food).has(DataComponents.FOOD), "taming food is edible");
        }
        var input = CraftingInput.of(1, 3, List.of(new ItemStack(ModItems.CRYSTAL_SHARD),
            new ItemStack(ModItems.DIRE_FANG), new ItemStack(Items.IRON_INGOT)));
        var recipe = helper.getLevel().getServer().getRecipeManager().getRecipeFor(RecipeType.CRAFTING, input, helper.getLevel());
        check(helper, recipe.isPresent(), "crystal fang sword ingredients match");
        var result = recipe.orElseThrow().value().assemble(input, helper.getLevel().registryAccess());
        check(helper, result.is(ModItems.CRYSTAL_FANG_SWORD), "crafting produces registered weapon");
        check(helper, result.getMaxDamage() == 720, "crafted weapon has usable durability");
        helper.succeed();
    }

    @GameTest
    public void creatureLootSuppliesAllCraftingMaterials(GameTestHelper helper) {
        var sources = Map.ofEntries(
            Map.entry("goblin_scout", ModItems.GOBLIN_SCRAP), Map.entry("orc_warrior", ModItems.ORC_STEEL),
            Map.entry("minotaur", ModItems.MINOTAUR_HORN), Map.entry("stone_troll", ModItems.TROLL_HEARTSTONE),
            Map.entry("ancient_treant", ModItems.LIVING_WOOD), Map.entry("forest_dryad", ModItems.FOREST_ESSENCE),
            Map.entry("griffin", ModItems.GRIFFIN_FEATHER), Map.entry("dire_wolf", ModItems.DIRE_FANG),
            Map.entry("wild_wyvern", ModItems.WYVERN_SCALE), Map.entry("cave_basilisk", ModItems.BASILISK_SCALE),
            Map.entry("crystal_spider", ModItems.CRYSTAL_SHARD), Map.entry("shadow_wraith", ModItems.SHADOW_ESSENCE),
            Map.entry("frost_elemental", ModItems.FROST_ESSENCE), Map.entry("flame_imp", ModItems.INFERNAL_EMBER),
            Map.entry("slime_maiden", ModItems.SLIME_PEARL));
        var contextEntity = helper.spawn(EntityType.PIG, 2, 2, 2);
        contextEntity.setNoAi(true);
        var params = new LootParams.Builder(helper.getLevel())
            .withParameter(LootContextParams.THIS_ENTITY, contextEntity)
            .withParameter(LootContextParams.ORIGIN, contextEntity.position())
            .withParameter(LootContextParams.DAMAGE_SOURCE, contextEntity.damageSources().generic())
            .create(LootContextParamSets.ENTITY);
        for (var source : sources.entrySet()) {
            var key = ResourceKey.create(Registries.LOOT_TABLE, ModEntities.id("entities/" + source.getKey()));
            var table = helper.getLevel().getServer().reloadableRegistries().getLootTable(key);
            boolean obtainable = false;
            for (int seed = 0; seed < 64 && !obtainable; seed++) {
                obtainable = table.getRandomItems(params, seed).stream().anyMatch(stack -> stack.is(source.getValue()));
            }
            check(helper, obtainable, "survival source for " + BuiltInRegistries.ITEM.getKey(source.getValue()));
        }
        helper.succeed();
    }

    @GameTest
    public void frostStaffUsesServerCooldownAndDurability(GameTestHelper helper) {
        // makeMockServerPlayerInLevel hardcodes gameMode() to CREATIVE, ignoring setGameMode.
        var player = helper.makeMockPlayer(GameType.SURVIVAL);
        var stack = new ItemStack(ModItems.FROSTBOUND_STAFF);
        player.setItemInHand(InteractionHand.MAIN_HAND, stack);
        ModItems.FROSTBOUND_STAFF.use(helper.getLevel(), player, InteractionHand.MAIN_HAND);
        check(helper, player.hasEffect(MobEffects.RESISTANCE), "staff applies defensive magic");
        check(helper, player.getCooldowns().isOnCooldown(stack), "server cooldown starts");
        check(helper, stack.getDamageValue() == 3, "casting costs durability");
        ModItems.FROSTBOUND_STAFF.use(helper.getLevel(), player, InteractionHand.MAIN_HAND);
        check(helper, stack.getDamageValue() == 3, "cooldown prevents repeated casting");
        helper.succeed();
    }

    @GameTest
    public void betterCombatPresetsResolveWhenInstalled(GameTestHelper helper) throws ReflectiveOperationException {
        var categories = Map.of(ModItems.CRYSTAL_FANG_SWORD, "sword", ModItems.ORC_WAR_AXE, "axe",
            ModItems.BASILISK_SPEAR, "spear", ModItems.FROSTBOUND_STAFF, "staff");
        for (var entry : categories.entrySet()) {
            var id = BuiltInRegistries.ITEM.getKey(entry.getKey());
            var resource = ModEntities.id("weapon_attributes/" + id.getPath() + ".json");
            check(helper, helper.getLevel().getServer().getResourceManager().getResource(resource).isPresent(),
                "weapon attributes resource exists " + id);
        }
        if (BetterCombatCompat.isLoaded()) {
            // Reflection keeps the test and base mod independent of optional Better Combat classes.
            var registry = Class.forName("net.bettercombat.logic.WeaponRegistry");
            var lookup = registry.getMethod("getAttributes", ItemStack.class);
            for (var entry : categories.entrySet()) {
                var attributes = lookup.invoke(null, new ItemStack(entry.getKey()));
                check(helper, attributes != null, "Better Combat resolves custom item attributes");
                check(helper, entry.getValue().equals(attributes.getClass().getMethod("category").invoke(attributes)),
                    "Better Combat resolves the correct weapon category");
                var attacks = (Object[]) attributes.getClass().getMethod("attacks").invoke(attributes);
                check(helper, attacks.length > 0, "Better Combat preset supplies attack animations");
            }
        }
        helper.succeed();
    }
}
