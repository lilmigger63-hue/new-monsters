package com.mythicrealms.creatures.clienttest;

import com.google.gson.JsonParser;
import com.mythicrealms.creatures.entity.CreatureKind;
import com.mythicrealms.creatures.entity.mount.MythicMountEntity;
import com.mythicrealms.creatures.registry.ModEntities;
import net.fabricmc.fabric.api.client.gametest.v1.FabricClientGameTest;
import net.fabricmc.fabric.api.client.gametest.v1.context.ClientGameTestContext;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.world.entity.Entity;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import software.bernie.geckolib.animatable.GeoEntity;
import software.bernie.geckolib.cache.GeckoLibResources;
import software.bernie.geckolib.renderer.GeoEntityRenderer;

/** Exercises the real resource reload, renderers, singleplayer sync and animation playback. */
public final class CreatureClientSmokeTest implements FabricClientGameTest {
    private static final Logger LOG = LoggerFactory.getLogger("mythic-client-smoke");

    @Override public void runTest(ClientGameTestContext context) {
        context.getInput().resizeWindow(1280, 720);
        context.runOnClient(client -> {
            client.options.renderDistance().set(3);
            client.options.fov().set(50);
            client.options.pauseOnLostFocus = false;
            client.options.hideGui = true;
            for (CreatureKind kind : CreatureKind.values()) {
                var asset = ModEntities.id("entity/" + kind.id);
                require(GeckoLibResources.getBakedModels().containsKey(asset), "Baked geometry missing: " + asset);
                var animations = GeckoLibResources.getBakedAnimations().get(asset);
                require(animations != null, "Baked animations missing: " + asset);
                for (String animation : new String[]{"idle", "walk", "run", "hurt", "attack", "cast", "death"})
                    require(animations.getAnimation(animation) != null, "Animation missing: " + kind.id + "/" + animation);
                try (var reader = client.getResourceManager().getResourceOrThrow(
                        ModEntities.id("geckolib/animations/entity/" + kind.id + ".animation.json")).openAsReader()) {
                    var declared = JsonParser.parseReader(reader).getAsJsonObject().getAsJsonObject("animations");
                    for (String animation : declared.keySet())
                        require(animations.getAnimation(animation) != null, "Declared animation failed to bake: " + kind.id + "/" + animation);
                    LOG.info("CLIENT_SMOKE_ANIMATIONS {} {}", kind.id, declared.keySet());
                } catch (java.io.IOException exception) {
                    throw new AssertionError("Unable to read animation resource for " + kind.id, exception);
                }
                require(client.getResourceManager().getResource(ModEntities.id("textures/entity/" + kind.id + ".png")).isPresent(),
                        "Texture missing: " + kind.id);
            }
        });
        try (var world = context.worldBuilder().create()) {
            var server = world.getServer();
            server.runCommand("difficulty normal");
            server.runCommand("gamemode spectator @a");
            server.runCommand("time set noon");
            server.runCommand("weather clear");
            server.runCommand("tp @a 16 -59 30 180 8");
            int index = 0;
            for (CreatureKind kind : CreatureKind.values()) {
                int x = (index % 5) * 8;
                int z = (index++ / 5) * 16;
                server.runCommand("summon mythic_realms_creatures:" + kind.id + " " + x + " -60 " + z + " {NoAI:1b,PersistenceRequired:1b,Invulnerable:1b,Rotation:[0f,0f]}");
            }
            context.waitTicks(20);
            context.waitFor(client -> {
                int tracked = 0;
                for (Entity entity : client.level.entitiesForRendering())
                    if (BuiltInRegistries.ENTITY_TYPE.getKey(entity.getType()).getNamespace().equals("mythic_realms_creatures")) tracked++;
                return tracked == CreatureKind.values().length;
            }, 600);
            int count = context.computeOnClient(client -> {
                int found = 0;
                for (Entity entity : client.level.entitiesForRendering()) {
                    if (!BuiltInRegistries.ENTITY_TYPE.getKey(entity.getType()).getNamespace().equals("mythic_realms_creatures")) continue;
                    require(client.getEntityRenderDispatcher().getRenderer(entity) instanceof GeoEntityRenderer,
                            "Expected GeckoLib renderer for " + entity.getType());
                    found++;
                }
                return found;
            });
            require(count == CreatureKind.values().length, "Expected " + CreatureKind.values().length + " client entities, got " + count);
            index = 0;
            for (CreatureKind kind : CreatureKind.values()) {
                int x = (index % 5) * 8;
                int z = (index++ / 5) * 16;
                double distance = Math.max(4, kind.height * 1.8);
                double cameraFeetY = -60 + kind.height * .55 - 1.62;
                server.runCommand("tp @a " + x + " " + cameraFeetY + " " + (z + distance) + " 180 0");
                context.waitTicks(10);
                world.getClientWorld().waitForChunksRender();
                context.takeScreenshot("creature-" + kind.id + "-idle");
                server.runOnServer(mcServer -> {
                    for (Entity entity : mcServer.overworld().getAllEntities()) {
                        if (BuiltInRegistries.ENTITY_TYPE.getKey(entity.getType()).equals(ModEntities.id(kind.id)))
                            ((GeoEntity)entity).triggerAnim("action", "attack");
                    }
                });
                context.waitTicks(8);
                context.takeScreenshot("creature-" + kind.id + "-attack");
                LOG.info("CLIENT_SMOKE_ENTITY_PASS {} geometry, animation bake, texture, renderer, entity sync, idle/attack frames", kind.id);
            }
            server.runCommand("gamemode creative @a");
            var start = server.computeOnServer(mcServer -> {
                var rider = mcServer.getPlayerList().getPlayers().getFirst();
                for (Entity entity : mcServer.overworld().getAllEntities()) {
                    if (entity.getType() != ModEntities.GRIFFIN) continue;
                    var griffin = (MythicMountEntity)entity;
                    griffin.setNoAi(false);
                    griffin.setOwner(rider);
                    griffin.setTame(true, true);
                    griffin.setSaddled(true);
                    griffin.setOrderedToSit(false);
                    require(rider.startRiding(griffin), "Real integrated player could not mount tamed saddled griffin");
                    return griffin.position();
                }
                throw new AssertionError("Griffin not found for real player flight test");
            });
            context.waitFor(client -> client.player.getVehicle() != null && client.player.getVehicle().getType() == ModEntities.GRIFFIN, 600);
            context.getInput().holdKey(options -> options.keyJump);
            context.getInput().holdKey(options -> options.keyUp);
            context.waitTicks(30);
            var end = server.computeOnServer(mcServer -> {
                var rider = mcServer.getPlayerList().getPlayers().getFirst();
                require(rider.getLastClientInput().jump() && rider.getLastClientInput().forward(), "Real keyboard input did not reach authoritative server");
                var griffin = (MythicMountEntity)rider.getVehicle();
                require(griffin != null && griffin.isFlying(), "Authoritative griffin did not enter flight");
                return griffin.position();
            });
            context.getInput().releaseKey(options -> options.keyJump);
            context.getInput().releaseKey(options -> options.keyUp);
            require(end.y > start.y + 1, "Real player jump input did not raise server mount: " + start + " -> " + end);
            require(end.subtract(start).horizontalDistance() > 2, "Real player forward input did not move server mount: " + start + " -> " + end);
            context.waitTicks(2);
            context.takeScreenshot("griffin-real-player-flight");
            LOG.info("CLIENT_SMOKE_MOUNT_PASS real integrated player keyboard packets moved authoritative griffin {} -> {}", start, end);
            LOG.info("CLIENT_SMOKE_PASS {} creature types in a real singleplayer world", count);
        }
    }

    private static void require(boolean condition, String message) {
        if (!condition) throw new AssertionError(message);
    }
}
