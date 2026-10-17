package com.mythicrealms.creatures.entity;

import net.minecraft.world.entity.ai.attributes.AttributeSupplier;
import net.minecraft.world.entity.ai.attributes.Attributes;
import net.minecraft.world.entity.monster.Monster;

public enum CreatureKind {
    GOBLIN_SCOUT("goblin_scout", 18, 3, .32, 1, .65f, 1.25f, 7, 18, 2.1, 12),
    GOBLIN_SHAMAN("goblin_shaman", 24, 4, .24, 1, .65f, 1.55f, 16, 45, 12, 5),
    ORC_WARRIOR("orc_warrior", 40, 7, .23, 7, .95f, 2.15f, 18, 28, 2.8, 7),
    MINOTAUR("minotaur", 65, 9, .27, 5, 1.35f, 2.85f, 24, 55, 9, 3),
    STONE_TROLL("stone_troll", 80, 11, .17, 10, 1.6f, 3.2f, 22, 55, 14, 3);

    public final String id;
    public final double health, damage, speed, armor, range;
    public final float width, height;
    public final int windup, recovery, spawnWeight;
    CreatureKind(String id, double health, double damage, double speed, double armor,
                 float width, float height, int windup, int recovery, double range, int weight) {
        this.id = id; this.health = health; this.damage = damage; this.speed = speed;
        this.armor = armor; this.width = width; this.height = height;
        this.windup = windup; this.recovery = recovery; this.range = range; this.spawnWeight = weight;
    }
    public AttributeSupplier.Builder attributes(double difficulty) {
        return Monster.createMonsterAttributes().add(Attributes.MAX_HEALTH, health * difficulty)
            .add(Attributes.ATTACK_DAMAGE, damage * difficulty).add(Attributes.MOVEMENT_SPEED, speed)
            .add(Attributes.ARMOR, armor).add(Attributes.FOLLOW_RANGE, 28)
            .add(Attributes.KNOCKBACK_RESISTANCE, width >= 1.3 ? .6 : .1);
    }
}
