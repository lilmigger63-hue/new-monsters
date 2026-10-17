package com.mythicrealms.creatures;

import com.mythicrealms.creatures.entity.*;
import com.mythicrealms.creatures.registry.ModEntities;
import net.fabricmc.fabric.api.gametest.v1.GameTest;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.gametest.framework.GameTestHelper;
import net.minecraft.network.chat.Component;
import net.minecraft.world.entity.*;
import net.minecraft.world.item.SpawnEggItem;
import net.minecraft.world.level.block.Blocks;

public final class CreatureGameTests {
    private void floor(GameTestHelper helper) {
        for (int x = 0; x < 8; x++) for (int z = 0; z < 8; z++) helper.setBlock(x, 1, z, Blocks.STONE);
    }
    @GameTest
    public void fiveSpeciesRegisterWithAttributesEggsAndLoot(GameTestHelper helper) {
        floor(helper);
        var types = java.util.List.of(ModEntities.GOBLIN_SCOUT, ModEntities.GOBLIN_SHAMAN,
            ModEntities.ORC_WARRIOR, ModEntities.MINOTAUR, ModEntities.STONE_TROLL);
        int x = 1;
        for (var type : types) {
            var creature = helper.spawn(type, x++, 2, 3);
            creature.setNoAi(true);
            helper.assertTrue(creature.getMaxHealth() == creature.kind().health, Component.literal("species health"));
            helper.assertTrue(creature.getType().getDefaultLootTable().isPresent(), Component.literal("loot table key"));
            var lootKey = creature.getType().getDefaultLootTable().orElseThrow();
            helper.assertTrue(helper.getLevel().getServer().reloadableRegistries().getLootTable(lootKey)
                != net.minecraft.world.level.storage.loot.LootTable.EMPTY, Component.literal("loaded loot table"));
            helper.assertTrue(BuiltInRegistries.ITEM.getValue(ModEntities.id(creature.kind().id + "_spawn_egg"))
                instanceof SpawnEggItem, Component.literal("registered spawn egg"));
        }
        helper.succeed();
    }
    @GameTest(maxTicks = 50)
    public void scoutWindupThenServerDamage(GameTestHelper helper) {
        floor(helper);
        var scout = helper.spawn(ModEntities.GOBLIN_SCOUT, 2, 2, 2);
        var victim = helper.spawn(EntityType.IRON_GOLEM, 3, 2, 2);
        victim.setNoAi(true);
        float health = victim.getHealth();
        scout.setTarget(victim);
        helper.assertTrue(scout.tryAttack(victim), Component.literal("attack begins"));
        helper.runAfterDelay(2, () -> helper.assertTrue(victim.getHealth() == health, Component.literal("windup has no early damage")));
        helper.runAfterDelay(12, () -> {
            helper.assertTrue(victim.getHealth() < health, Component.literal("server attack impacts after windup"));
            helper.succeed();
        });
    }
    @GameTest(maxTicks = 60)
    public void shamanProjectileDamagesTarget(GameTestHelper helper) {
        floor(helper);
        var shaman = helper.spawn(ModEntities.GOBLIN_SHAMAN, 2, 2, 2);
        var victim = helper.spawn(EntityType.IRON_GOLEM, 5, 2, 2);
        shaman.setNoAi(true); victim.setNoAi(true);
        float health = victim.getHealth();
        CreatureProjectile.launch(ModEntities.SHAMAN_BOLT, shaman, victim, 1.1f);
        helper.runAfterDelay(20, () -> {
            helper.assertTrue(victim.getHealth() < health, Component.literal("projectile deals damage"));
            helper.succeed();
        });
    }
    @GameTest
    public void minotaurRetaliatesAgainstNearbyGolem(GameTestHelper helper) {
        floor(helper);
        var minotaur = helper.spawn(ModEntities.MINOTAUR, 2, 2, 2);
        var golem = helper.spawn(EntityType.IRON_GOLEM, 3, 2, 2);
        minotaur.setNoAi(true); golem.setNoAi(true);
        minotaur.setTarget(golem);
        float health = golem.getHealth();
        minotaur.performAttack(helper.getLevel(), golem);
        helper.assertTrue(golem.getHealth() < health, Component.literal("minotaur retaliates against non-player target"));
        helper.succeed();
    }
    @GameTest
    public void trollRetaliatesAgainstNearbyGolem(GameTestHelper helper) {
        floor(helper);
        var troll = helper.spawn(ModEntities.STONE_TROLL, 2, 2, 2);
        var golem = helper.spawn(EntityType.IRON_GOLEM, 3, 2, 2);
        troll.setNoAi(true); golem.setNoAi(true);
        troll.setTarget(golem);
        float health = golem.getHealth();
        troll.performAttack(helper.getLevel(), golem);
        helper.assertTrue(golem.getHealth() < health, Component.literal("troll retaliates against non-player target"));
        helper.succeed();
    }

}
