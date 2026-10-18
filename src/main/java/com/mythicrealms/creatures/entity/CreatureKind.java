package com.mythicrealms.creatures.entity;

import net.minecraft.world.entity.ai.attributes.AttributeSupplier;
import net.minecraft.world.entity.ai.attributes.Attributes;
import net.minecraft.world.entity.monster.Monster;

public enum CreatureKind {
    GOBLIN_SCOUT("goblin_scout", 18, 3, .32, 1, .65f, 1.25f, 7, 18, 2.1, 12),
    GOBLIN_SHAMAN("goblin_shaman", 24, 4, .24, 1, .65f, 1.55f, 16, 45, 12, 5),
    ORC_WARRIOR("orc_warrior", 40, 7, .23, 7, .95f, 2.15f, 18, 28, 2.8, 7),
    MINOTAUR("minotaur", 65, 9, .27, 5, 1.35f, 2.85f, 24, 55, 9, 3),
    STONE_TROLL("stone_troll", 80, 11, .17, 10, 1.6f, 3.2f, 22, 55, 14, 3),
    ANCIENT_TREANT("ancient_treant", 100, 8, .16, 8, 1.8f, 4.6f, 24, 45, 13, 2),
    FOREST_DRYAD("forest_dryad", 28, 3, .26, 2, .65f, 1.9f, 16, 40, 10, 5),
    GRIFFIN("griffin", 48, 6, .28, 3, 1.4f, 1.8f, 12, 25, 2.8, 3),
    DIRE_WOLF("dire_wolf", 36, 5, .34, 2, 1.05f, 1.35f, 7, 18, 2.3, 6),
    WILD_WYVERN("wild_wyvern", 64, 7, .25, 5, 1.6f, 2.1f, 20, 55, 9, 1),
    CAVE_BASILISK("cave_basilisk", 34, 5, .25, 4, 1.2f, .85f, 20, 40, 9, 4),
    CRYSTAL_SPIDER("crystal_spider", 28, 4, .29, 3, 1.4f, 1.1f, 14, 35, 12, 5),
    SHADOW_WRAITH("shadow_wraith", 30, 5, .25, 1, .7f, 2f, 18, 36, 12, 4),
    GRAVE_KNIGHT("grave_knight", 46, 6, .24, 9, .8f, 2.1f, 12, 20, 2.8, 4),
    FLAME_IMP("flame_imp", 16, 4, .28, 0, .5f, .8f, 14, 35, 12, 5),
    FROST_ELEMENTAL("frost_elemental", 42, 6, .2, 5, 1.1f, 2.4f, 24, 45, 12, 4),
    MOON_STAG("moon_stag", 32, 3, .32, 1, 1.1f, 1.8f, 8, 25, 2.5, 1),
    SLIME_MAIDEN("slime_maiden", 30, 4, .24, 1, .85f, 1.65f, 14, 30, 9, 4),
    HARPY("harpy", 26, 4, .3, 2, .9f, 1.8f, 12, 25, 10, 4),
    DEMON_SORCERESS("demon_sorceress", 40, 6, .25, 3, .7f, 1.95f, 22, 50, 13, 2),
    ENDER_DRAGON_GIRL("ender_dragon_girl",40,6,.25,4,.85f,2.05f,22,50,13,1),
    VAMPIRE("vampire",28,4,.32,2,.7f,1.85f,7,22,2.1,3),
    HOLSTAURUS("holstaurus",30,4,.24,2,.8f,1.9f,14,30,9,3),
    CENTAUR("centaur",38,5,.32,4,1.25f,2.15f,10,24,2.6,2),
    SAHUAGIN("sahuagin",28,4,.29,3,.7f,1.85f,10,24,2.4,3),
    VALKYRIE("valkyrie",42,6,.28,8,.8f,2f,14,30,2.8,1),
    FOX_SPIRIT_GIRL("fox_spirit_girl",30,4,.27,2,.75f,1.85f,16,40,13,2),
    ANUBIS("anubis",34,5,.29,5,.7f,1.95f,10,24,2.5,2),
    KOBOLD("kobold",20,3,.32,3,.6f,1.3f,7,20,2.1,4),
    CYCLOPS("cyclops",48,7,.23,7,.85f,2.05f,18,36,3.2,1),
    DHAMPIR("dhampir",30,5,.3,4,.7f,1.85f,9,24,2.6,2),
    SUCCUBUS("succubus",36,5,.25,3,.75f,1.9f,22,50,13,2),
    WERECAT("werecat",28,4,.29,3,.7f,1.8f,16,38,13,3);

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
    public boolean isExpansion() { return ordinal()>DEMON_SORCERESS.ordinal(); }
    public boolean allowsNaturalSpawning() { return isExpansion() || this==FOREST_DRYAD || this==SLIME_MAIDEN; }
    public AttributeSupplier.Builder attributes(double difficulty) {
        return Monster.createMonsterAttributes().add(Attributes.MAX_HEALTH, health * difficulty)
            .add(Attributes.ATTACK_DAMAGE, damage * difficulty).add(Attributes.MOVEMENT_SPEED, speed)
            .add(Attributes.TEMPT_RANGE, 10).add(Attributes.FLYING_SPEED, .35).add(Attributes.STEP_HEIGHT, 1)
            .add(Attributes.ARMOR, armor).add(Attributes.FOLLOW_RANGE, 28)
            .add(Attributes.KNOCKBACK_RESISTANCE, width >= 1.3 ? .6 : .1);
    }
}
