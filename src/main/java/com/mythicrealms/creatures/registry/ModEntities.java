package com.mythicrealms.creatures.registry;

import com.mythicrealms.creatures.MythicRealmsCreatures;
import com.mythicrealms.creatures.config.CreatureConfig;
import com.mythicrealms.creatures.entity.*;
import com.mythicrealms.creatures.entity.expansion.*;
import net.fabricmc.fabric.api.biome.v1.*;
import net.fabricmc.fabric.api.itemgroup.v1.ItemGroupEvents;
import net.fabricmc.fabric.api.object.builder.v1.entity.FabricEntityType;
import net.minecraft.core.Registry;
import net.minecraft.core.registries.*;
import net.minecraft.resources.*;
import net.minecraft.tags.TagKey;
import net.minecraft.tags.BlockTags;
import net.minecraft.world.Difficulty;
import net.minecraft.world.entity.*;
import net.minecraft.world.entity.monster.Monster;
import net.minecraft.world.item.*;
import net.minecraft.world.level.biome.Biome;
import net.minecraft.world.level.levelgen.Heightmap;

public final class ModEntities {
    public static final EntityType<GoblinScoutEntity> GOBLIN_SCOUT = creature(CreatureKind.GOBLIN_SCOUT, GoblinScoutEntity::new);
    public static final EntityType<GoblinShamanEntity> GOBLIN_SHAMAN = creature(CreatureKind.GOBLIN_SHAMAN, GoblinShamanEntity::new);
    public static final EntityType<OrcWarriorEntity> ORC_WARRIOR = creature(CreatureKind.ORC_WARRIOR, OrcWarriorEntity::new);
    public static final EntityType<MinotaurEntity> MINOTAUR = creature(CreatureKind.MINOTAUR, MinotaurEntity::new);
    public static final EntityType<StoneTrollEntity> STONE_TROLL = creature(CreatureKind.STONE_TROLL, StoneTrollEntity::new);
    public static final EntityType<AncientTreantEntity> ANCIENT_TREANT = companion(CreatureKind.ANCIENT_TREANT, AncientTreantEntity::new);
    public static final EntityType<ForestDryadEntity> FOREST_DRYAD = companion(CreatureKind.FOREST_DRYAD, ForestDryadEntity::new);
    public static final EntityType<GriffinEntity> GRIFFIN = companion(CreatureKind.GRIFFIN, GriffinEntity::new);
    public static final EntityType<DireWolfEntity> DIRE_WOLF = companion(CreatureKind.DIRE_WOLF, DireWolfEntity::new);
    public static final EntityType<WildWyvernEntity> WILD_WYVERN = companion(CreatureKind.WILD_WYVERN, WildWyvernEntity::new);
    public static final EntityType<CaveBasiliskEntity> CAVE_BASILISK = creature(CreatureKind.CAVE_BASILISK, CaveBasiliskEntity::new);
    public static final EntityType<CrystalSpiderEntity> CRYSTAL_SPIDER = creature(CreatureKind.CRYSTAL_SPIDER, CrystalSpiderEntity::new);
    public static final EntityType<ShadowWraithEntity> SHADOW_WRAITH = creature(CreatureKind.SHADOW_WRAITH, ShadowWraithEntity::new);
    public static final EntityType<GraveKnightEntity> GRAVE_KNIGHT = creature(CreatureKind.GRAVE_KNIGHT, GraveKnightEntity::new);
    public static final EntityType<FlameImpEntity> FLAME_IMP = creature(CreatureKind.FLAME_IMP, FlameImpEntity::new);
    public static final EntityType<FrostElementalEntity> FROST_ELEMENTAL = creature(CreatureKind.FROST_ELEMENTAL, FrostElementalEntity::new);
    public static final EntityType<MoonStagEntity> MOON_STAG = companion(CreatureKind.MOON_STAG, MoonStagEntity::new);
    public static final EntityType<SlimeMaidenEntity> SLIME_MAIDEN = companion(CreatureKind.SLIME_MAIDEN, SlimeMaidenEntity::new);
    public static final EntityType<HarpyEntity> HARPY = creature(CreatureKind.HARPY, HarpyEntity::new);
    public static final EntityType<DemonSorceressEntity> DEMON_SORCERESS = creature(CreatureKind.DEMON_SORCERESS, DemonSorceressEntity::new);
    public static final EntityType<EnderDragonGirlEntity> ENDER_DRAGON_GIRL = creature(CreatureKind.ENDER_DRAGON_GIRL, EnderDragonGirlEntity::new);
    public static final EntityType<VampireEntity> VAMPIRE = creature(CreatureKind.VAMPIRE, VampireEntity::new);
    public static final EntityType<HolstaurusEntity> HOLSTAURUS = companion(CreatureKind.HOLSTAURUS, HolstaurusEntity::new);
    public static final EntityType<CentaurEntity> CENTAUR = creature(CreatureKind.CENTAUR, CentaurEntity::new);
    public static final EntityType<SahuaginEntity> SAHUAGIN = creature(CreatureKind.SAHUAGIN, SahuaginEntity::new);
    public static final EntityType<ValkyrieEntity> VALKYRIE = creature(CreatureKind.VALKYRIE, ValkyrieEntity::new);
    public static final EntityType<FoxSpiritGirlEntity> FOX_SPIRIT_GIRL = creature(CreatureKind.FOX_SPIRIT_GIRL, FoxSpiritGirlEntity::new);
    public static final EntityType<AnubisEntity> ANUBIS = creature(CreatureKind.ANUBIS, AnubisEntity::new);
    public static final EntityType<KoboldEntity> KOBOLD = creature(CreatureKind.KOBOLD, KoboldEntity::new);
    public static final EntityType<CyclopsEntity> CYCLOPS = creature(CreatureKind.CYCLOPS, CyclopsEntity::new);
    public static final EntityType<DhampirEntity> DHAMPIR = creature(CreatureKind.DHAMPIR, DhampirEntity::new);
    public static final EntityType<SuccubusEntity> SUCCUBUS = creature(CreatureKind.SUCCUBUS, SuccubusEntity::new);
    public static final EntityType<WerecatEntity> WERECAT = creature(CreatureKind.WERECAT, WerecatEntity::new);
    public static final EntityType<CreatureProjectile> CRYSTAL_BOLT = projectile("crystal_bolt", .25f);
    public static final EntityType<CreatureProjectile> DARK_BOLT = projectile("dark_bolt", .3f);
    public static final EntityType<CreatureProjectile> FIRE_BOLT = projectile("fire_bolt", .25f);
    public static final EntityType<CreatureProjectile> ICE_SPIKE = projectile("ice_spike", .3f);
    public static final EntityType<CreatureProjectile> FEATHER_BOLT = projectile("feather_bolt", .2f);
    public static final EntityType<CreatureProjectile> SLIME_BUBBLE = projectile("slime_bubble", .35f);
    public static final EntityType<com.mythicrealms.creatures.magic.WebTrapEntity> WEB_TRAP = webTrap();
    public static final EntityType<CreatureProjectile> ROOT_SHARD = projectile("root_shard", .35f);
    public static final EntityType<CreatureProjectile> VINE_SEED = projectile("vine_seed", .2f);
    public static final EntityType<CreatureProjectile> POISON_BREATH = projectile("poison_breath", .4f);
    public static final EntityType<CreatureProjectile> SHAMAN_BOLT = projectile("shaman_bolt", .25f);
    public static final EntityType<CreatureProjectile> TROLL_BOULDER = projectile("troll_boulder", .55f);

    public static ResourceLocation id(String path) { return ResourceLocation.fromNamespaceAndPath(MythicRealmsCreatures.MOD_ID, path); }
    private static <T extends MythicHostileEntity> EntityType<T> creature(CreatureKind kind, EntityType.EntityFactory<T> factory) {
        var key = ResourceKey.create(Registries.ENTITY_TYPE, id(kind.id));
        var rule = CreatureConfig.INSTANCE.spawning.get(kind.id);
        var builder = FabricEntityType.Builder.createMob(factory, MobCategory.MONSTER, extra -> extra
            .defaultAttributes(() -> kind.attributes(CreatureConfig.INSTANCE.difficultyMultiplier*rule.difficultyMultiplier))
            .spawnRestriction(kind==CreatureKind.SAHUAGIN?SpawnPlacementTypes.IN_WATER:SpawnPlacementTypes.ON_GROUND, Heightmap.Types.MOTION_BLOCKING_NO_LEAVES,
                (type, level, reason, pos, random) -> allowedSpawnReason(kind,reason) && allowConfiguredSpawn(kind,level,pos) && random.nextInt(rule.frequency) == 0
                    && (kind!=CreatureKind.SAHUAGIN || level.getFluidState(pos).is(net.minecraft.tags.FluidTags.WATER))
                    && ((kind != CreatureKind.STONE_TROLL && kind != CreatureKind.CAVE_BASILISK && kind != CreatureKind.CRYSTAL_SPIDER) || pos.getY() < level.getLevel().getSeaLevel() - 8)
                    && ((kind==CreatureKind.FLAME_IMP || kind==CreatureKind.DEMON_SORCERESS || kind==CreatureKind.SUCCUBUS || kind==CreatureKind.ENDER_DRAGON_GIRL || kind==CreatureKind.SAHUAGIN) ? level.getDifficulty()!=Difficulty.PEACEFUL && (!kind.isExpansion() || level.getRawBrightness(pos,0)<=12) : Monster.checkMonsterSpawnRules(type, level, reason, pos, random))));
        if(kind==CreatureKind.FLAME_IMP || kind==CreatureKind.DEMON_SORCERESS || kind==CreatureKind.SUCCUBUS || kind==CreatureKind.ENDER_DRAGON_GIRL)builder.fireImmune();
        var type = Registry.register(BuiltInRegistries.ENTITY_TYPE, key,
            builder.sized(kind.width, kind.height).clientTrackingRange(8).build(key));
        finishCreature(kind,type,MobCategory.MONSTER);
        return type;
    }
    private static <T extends PathfinderMob & MythicCreature> EntityType<T> companion(CreatureKind kind,EntityType.EntityFactory<T> factory) {
        var key=ResourceKey.create(Registries.ENTITY_TYPE,id(kind.id));
        var rule=CreatureConfig.INSTANCE.spawning.get(kind.id);
        var category=kind==CreatureKind.WILD_WYVERN?MobCategory.MONSTER:MobCategory.CREATURE;
        var builder=FabricEntityType.Builder.createMob(factory,category,extra -> extra
            .defaultAttributes(() -> kind.attributes(CreatureConfig.INSTANCE.difficultyMultiplier*rule.difficultyMultiplier))
            .spawnRestriction(SpawnPlacementTypes.ON_GROUND,Heightmap.Types.MOTION_BLOCKING_NO_LEAVES,
                (type,level,reason,pos,random) -> allowedSpawnReason(kind,reason) && allowConfiguredSpawn(kind,level,pos) && random.nextInt(rule.frequency)==0
                    && (kind==CreatureKind.WILD_WYVERN
                        ? level.getDifficulty()!=Difficulty.PEACEFUL && Monster.isDarkEnoughToSpawn(level,pos,random)
                        : level.getRawBrightness(pos,0)>8 && (level.getBlockState(pos.below()).is(BlockTags.DIRT)
                            || kind==CreatureKind.GRIFFIN && level.getBlockState(pos.below()).is(BlockTags.BASE_STONE_OVERWORLD)))));
        var type=Registry.register(BuiltInRegistries.ENTITY_TYPE,key,builder.sized(kind.width,kind.height).clientTrackingRange(8).build(key));
        finishCreature(kind,type,category);return type;
    }
    private static void finishCreature(CreatureKind kind,EntityType<?> type,MobCategory category) {
        var rule=CreatureConfig.INSTANCE.spawning.get(kind.id);
        var itemKey = ResourceKey.create(Registries.ITEM, id(kind.id + "_spawn_egg"));
        Item egg = Registry.register(BuiltInRegistries.ITEM, itemKey,
            new SpawnEggItem(new Item.Properties().setId(itemKey).spawnEgg(type)));
        ItemGroupEvents.modifyEntriesEvent(CreativeModeTabs.SPAWN_EGGS).register(entries -> entries.accept(egg));
        if (kind.allowsNaturalSpawning() && rule.enabled && rule.weight > 0) {
            TagKey<Biome> tag = TagKey.create(Registries.BIOME, id("spawns/" + kind.id));
            BiomeModifications.addSpawn(BiomeSelectors.tag(tag), category, type,
                rule.weight, rule.minGroup, rule.maxGroup);
        }
    }
    private static boolean allowedSpawnReason(CreatureKind kind,EntitySpawnReason reason) {
        return kind.allowsNaturalSpawning() || reason!=EntitySpawnReason.NATURAL && reason!=EntitySpawnReason.CHUNK_GENERATION;
    }
    private static boolean allowConfiguredSpawn(CreatureKind kind,net.minecraft.world.level.ServerLevelAccessor level,net.minecraft.core.BlockPos pos){
        var rule=CreatureConfig.INSTANCE.spawning.get(kind.id);
        if(!rule.enabled || !rule.dimensions.contains(level.getLevel().dimension().location().toString()))return false;
        if(rule.biomes.isEmpty())return true;
        var biome=level.getBiome(pos);
        return rule.biomes.stream().anyMatch(value -> value.startsWith("#")
            ? biome.is(TagKey.create(Registries.BIOME,ResourceLocation.parse(value.substring(1))))
            : biome.is(ResourceKey.create(Registries.BIOME,ResourceLocation.parse(value))));
    }
    private static EntityType<com.mythicrealms.creatures.magic.WebTrapEntity> webTrap(){
        var key=ResourceKey.create(Registries.ENTITY_TYPE,id("web_trap"));
        return Registry.register(BuiltInRegistries.ENTITY_TYPE,key,
            EntityType.Builder.of(com.mythicrealms.creatures.magic.WebTrapEntity::new,MobCategory.MISC).sized(1.5f,.2f).clientTrackingRange(6).updateInterval(10).build(key));
    }
    private static EntityType<CreatureProjectile> projectile(String name, float size) {
        var key = ResourceKey.create(Registries.ENTITY_TYPE, id(name));
        return Registry.register(BuiltInRegistries.ENTITY_TYPE, key,
            EntityType.Builder.<CreatureProjectile>of(CreatureProjectile::new, MobCategory.MISC)
                .sized(size, size).clientTrackingRange(6).updateInterval(2).build(key));
    }
    public static void initialize() { }
}
