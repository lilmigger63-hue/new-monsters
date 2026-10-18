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
import software.bernie.geckolib.animation.RawAnimation;
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
            if(Boolean.getBoolean("mythic.clientSmoke.measureFrames")) {
                client.options.enableVsync().set(false);
                client.options.inactivityFpsLimit().set(net.minecraft.client.InactivityFpsLimit.MINIMIZED);
                client.options.framerateLimit().set(260);
            }
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
            server.runCommand("gamerule doMobSpawning false");
            server.runCommand("difficulty normal");
            server.runCommand("gamemode spectator @a");
            server.runCommand("time set noon");
            server.runCommand("weather clear");
            server.runCommand("tp @a 20 -59 30 180 8");
            int index = 0;
            for (CreatureKind kind : CreatureKind.values()) {
                int x = (index % 6) * 8;
                int z = (index++ / 6) * 12;
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
            int presented=0;
            for (CreatureKind kind : CreatureKind.values()) {
                int x = (index % 6) * 8;
                int z = (index++ / 6) * 12;
                String selectedSpecies=System.getProperty("mythic.clientSmoke.species");
                if(selectedSpecies!=null && !selectedSpecies.equals(kind.id))continue;
                if(Boolean.getBoolean("mythic.clientSmoke.expansionOnly") && !kind.isExpansion()
                        && kind!=CreatureKind.HARPY && kind!=CreatureKind.MINOTAUR
                        && kind!=CreatureKind.SLIME_MAIDEN && kind!=CreatureKind.FOREST_DRYAD)continue;
                boolean stanceOnly=Boolean.getBoolean("mythic.clientSmoke.mountStanceOnly");
                if(stanceOnly && kind!=CreatureKind.DIRE_WOLF && kind!=CreatureKind.MOON_STAG)continue;
                if(Boolean.getBoolean("mythic.clientSmoke.referenceOnly")
                        && kind!=CreatureKind.WILD_WYVERN && kind!=CreatureKind.HARPY
                        && kind!=CreatureKind.GRIFFIN && kind!=CreatureKind.MOON_STAG)continue;
                presented++;
                if(selectedSpecies!=null) {
                    server.runOnServer(mcServer -> {
                        for(Entity entity:mcServer.overworld().getAllEntities()) {
                            var id=BuiltInRegistries.ENTITY_TYPE.getKey(entity.getType());
                            if(id.getNamespace().equals("mythic_realms_creatures"))entity.setInvisible(!id.equals(ModEntities.id(kind.id)));
                        }
                    });
                    context.waitTicks(3);
                }
                if(Boolean.getBoolean("mythic.clientSmoke.groundedReference"))context.runOnClient(client -> {
                    for(Entity entity:client.level.entitiesForRendering()) {
                        if(!BuiltInRegistries.ENTITY_TYPE.getKey(entity.getType()).equals(ModEntities.id(kind.id)))continue;
                        GeoEntity geo=(GeoEntity)entity;
                        var controller=geo.getAnimatableInstanceCache().getManagerForId(entity.getId()).getAnimationControllers().get("locomotion");
                        controller.triggerableAnim("reference_idle",RawAnimation.begin().thenLoop("idle"));
                        controller.tryTriggerAnimation("reference_idle");
                    }
                });
                double distance = Math.max(kind==CreatureKind.WILD_WYVERN || kind==CreatureKind.CENTAUR
                        || kind==CreatureKind.MOON_STAG && Boolean.getBoolean("mythic.clientSmoke.referenceOnly")
                        ? 6 : 4, kind.height * 1.8);
                double cameraFeetY = -60 + kind.height * .55 - 1.62;
                server.runCommand("tp @a " + x + " " + cameraFeetY + " " + (z + distance) + " 180 0");
                context.waitTicks(10);
                world.getClientWorld().waitForChunksRender();
                if(stanceOnly)context.runOnClient(client -> {
                    for(Entity entity:client.level.entitiesForRendering()){
                        if(!BuiltInRegistries.ENTITY_TYPE.getKey(entity.getType()).equals(ModEntities.id(kind.id)))continue;
                        GeoEntity geo=(GeoEntity)entity;
                        var raw=geo.getAnimatableInstanceCache().getManagerForId(entity.getId()).getAnimationControllers().get("locomotion").getCurrentRawAnimation();
                        require(raw!=null && raw.getAnimationStages().getFirst().animationName().equals("idle"),
                            "Stationary remote mount must idle: "+kind.id+" ground="+entity.onGround()+" velocity="+entity.getDeltaMovement()+" clip="+raw);
                    }
                });
                context.takeScreenshot("creature-" + kind.id + "-idle");
                if(Boolean.getBoolean("mythic.clientSmoke.measureFrames")) {
                    context.waitTicks(20);
                    for(int sample=0;sample<Math.max(1,Math.min(120,Integer.getInteger("mythic.clientSmoke.performanceSamples",5)));sample++) {
                        context.waitTicks(5);
                        context.runOnClient(client -> {
                            require(client.getFramerateLimitTracker().getThrottleReason().name().equals("NONE"),
                                    "Performance sample must not be AFK/window throttled");
                            LOG.info("CLIENT_FRAME_SAMPLE {} fps={} frame_ns={} throttle={}",
                                    kind.id,client.getFps(),client.getFrameTimeNs(),
                                    client.getFramerateLimitTracker().getThrottleReason());
                        });
                    }
                }
                if(Boolean.getBoolean("mythic.clientSmoke.performanceOnly"))continue;
                for (String view : kind==CreatureKind.FOX_SPIRIT_GIRL
                        ? new String[]{"side", "three-quarter", "back", "rear-quarter", "distant"}
                        : new String[]{"side", "three-quarter", "back", "distant"}) {
                    double d = view.equals("distant") ? Math.max(12, kind.height * 4) : distance;
                    double cameraX = x + (view.equals("side") ? d : (view.equals("rear-quarter") || view.equals("three-quarter")) ? d*.707 : 0);
                    double cameraZ = z + (view.equals("side") ? 0 : view.equals("back") ? -d : view.equals("rear-quarter") ? -d*.707 : view.equals("three-quarter") ? d*.707 : d);
                    int yaw = view.equals("side") ? 90 : view.equals("back") ? 0 : view.equals("rear-quarter") ? 45 : view.equals("three-quarter") ? 135 : 180;
                    server.runCommand("tp @a " + cameraX + " " + (cameraFeetY+(view.equals("three-quarter")?kind.height*.18:0)) + " " + cameraZ + " " + yaw + (view.equals("three-quarter")?" 8":" 0"));
                    context.waitTicks(4);
                    world.getClientWorld().waitForChunksRender();
                    context.takeScreenshot("creature-" + kind.id + "-" + view);
                }
                if(Boolean.getBoolean("mythic.clientSmoke.groundedReference"))context.runOnClient(client -> {
                    for(Entity entity:client.level.entitiesForRendering())
                        if(BuiltInRegistries.ENTITY_TYPE.getKey(entity.getType()).equals(ModEntities.id(kind.id)))
                            ((GeoEntity)entity).stopTriggeredAnim("locomotion","reference_idle");
                });
                server.runCommand("tp @a " + x + " " + cameraFeetY + " " + (z + distance) + " 180 0");
                context.waitTicks(4);
                server.runOnServer(mcServer -> {
                    for (Entity entity : mcServer.overworld().getAllEntities()) {
                        if (BuiltInRegistries.ENTITY_TYPE.getKey(entity.getType()).equals(ModEntities.id(kind.id)))
                            ((GeoEntity)entity).triggerAnim("action", "attack");
                    }
                });
                context.waitTicks(8);
                context.takeScreenshot("creature-" + kind.id + "-attack");
                context.waitTicks(Math.max(1, kind.windup - 8));
                context.takeScreenshot("creature-" + kind.id + "-attack-impact");
                String[] probes = kind==CreatureKind.WILD_WYVERN || kind==CreatureKind.HARPY || kind==CreatureKind.GRIFFIN
                        || kind==CreatureKind.ENDER_DRAGON_GIRL || kind==CreatureKind.SUCCUBUS || kind==CreatureKind.VALKYRIE
                        ? new String[]{"walk", "run", "heavy", "cast", "hurt", "death", "fly", "hover"}
                        : new String[]{"walk", "run", "heavy", "cast", "hurt", "death"};
                for (String clip : probes) {
                    context.runOnClient(client -> {
                        for (Entity entity : client.level.entitiesForRendering()) {
                            if (!BuiltInRegistries.ENTITY_TYPE.getKey(entity.getType()).equals(ModEntities.id(kind.id))) continue;
                            GeoEntity geo = (GeoEntity)entity;
                            var action = geo.getAnimatableInstanceCache().getManagerForId(entity.getId()).getAnimationControllers().get("action");
                            action.triggerableAnim("visual_probe", clip.equals("walk") || clip.equals("run") || clip.equals("fly") || clip.equals("hover") ? RawAnimation.begin().thenLoop(clip) : RawAnimation.begin().thenPlayAndHold(clip));
                            action.tryTriggerAnimation("visual_probe");
                        }
                    });
                    if (clip.equals("cast")) server.runOnServer(mcServer -> {
                        for (Entity entity : mcServer.overworld().getAllEntities())
                            if (BuiltInRegistries.ENTITY_TYPE.getKey(entity.getType()).equals(ModEntities.id(kind.id)))
                                com.mythicrealms.creatures.magic.SpellEffects.telegraph(mcServer.overworld(),
                                    (net.minecraft.world.entity.Mob)entity,kind,(net.minecraft.world.entity.LivingEntity)entity);
                    });
                    context.waitTicks(clip.equals("cast") ? Math.max(8, kind.windup) : clip.equals("death") ? 22 : 8);
                    context.takeScreenshot("creature-" + kind.id + "-probe-" + clip);
                    if(clip.equals("heavy")) {
                        context.waitTicks(Math.max(1, kind.windup - 8));
                        context.takeScreenshot("creature-" + kind.id + "-probe-heavy-impact");
                    }
                    if(clip.equals("death") && kind==CreatureKind.HARPY) {
                        context.waitTicks(18);
                        context.takeScreenshot("creature-harpy-probe-death-held");
                    }
                    if(clip.equals("fly")) for(int phase=1;phase<=3;phase++) {
                        context.waitTicks(3);
                        context.takeScreenshot("creature-"+kind.id+"-probe-fly-phase-"+phase);
                    }
                    context.runOnClient(client -> {
                        for (Entity entity : client.level.entitiesForRendering())
                            if (BuiltInRegistries.ENTITY_TYPE.getKey(entity.getType()).equals(ModEntities.id(kind.id)))
                                ((GeoEntity)entity).stopTriggeredAnim("action", "visual_probe");
                    });
                }
                if(kind==CreatureKind.SAHUAGIN) {
                    server.runCommand("fill 76 -62 76 84 -54 84 glass");
                    server.runCommand("fill 77 -61 77 83 -55 83 water");
                    server.runCommand("tp @e[type=mythic_realms_creatures:sahuagin] 80 -59 80");
                    server.runCommand("data merge entity @e[type=mythic_realms_creatures:sahuagin,limit=1] {NoGravity:1b}");
                    server.runCommand("tp @a 80 -60 82.8 180 0");
                    server.runCommand("effect give @a minecraft:night_vision 999 0 true");
                    context.waitTicks(15);
                    context.runOnClient(client -> {
                        for(Entity entity:client.level.entitiesForRendering())
                            if(entity.getType()==ModEntities.SAHUAGIN)require(entity.isInWater(),"Sahuagin is actually submerged");
                    });
                    for(String swimClip:new String[]{"idle_swim","swim"}) {
                        context.runOnClient(client -> {
                            for(Entity entity:client.level.entitiesForRendering())if(entity.getType()==ModEntities.SAHUAGIN) {
                                var action=((GeoEntity)entity).getAnimatableInstanceCache().getManagerForId(entity.getId()).getAnimationControllers().get("action");
                                action.triggerableAnim("swim_probe",RawAnimation.begin().thenLoop(swimClip));
                                action.tryTriggerAnimation("swim_probe");
                            }
                        });
                        context.waitTicks(10);
                        context.takeScreenshot("creature-sahuagin-water-"+swimClip);
                        server.runCommand("tp @a 82.8 -60 80 90 0");
                        context.waitTicks(4);
                        context.takeScreenshot("creature-sahuagin-water-"+swimClip+"-side");
                        server.runCommand("tp @a 80 -60 82.8 180 0");
                        context.waitTicks(4);
                        context.runOnClient(client -> {
                            for(Entity entity:client.level.entitiesForRendering())if(entity.getType()==ModEntities.SAHUAGIN)
                                ((GeoEntity)entity).stopTriggeredAnim("action","swim_probe");
                        });
                    }
                    server.runCommand("effect clear @a minecraft:night_vision");
                    LOG.info("CLIENT_SMOKE_SWIM_PASS sahuagin submerged idle/swim playback");
                }
                LOG.info("CLIENT_SMOKE_ENTITY_PASS {} geometry, animation bake, texture, renderer, entity sync, four views, server attack, {} animation probes", kind.id, probes.length);
            }
            if(System.getProperty("mythic.clientSmoke.species")!=null)server.runOnServer(mcServer -> {
                for(Entity entity:mcServer.overworld().getAllEntities())
                    if(BuiltInRegistries.ENTITY_TYPE.getKey(entity.getType()).getNamespace().equals("mythic_realms_creatures"))entity.setInvisible(false);
            });
            // Real authoritative death alongside held playback probes: retain vanilla corpse lifetime.
            server.runCommand("summon mythic_realms_creatures:grave_knight 64 -60 72 {NoAI:1b,Tags:[overhaul_death_probe]}");
            server.runCommand("tp @a 64.5 -60.45 76 180 0");
            context.waitTicks(10);
            server.runCommand("kill @e[tag=overhaul_death_probe]");
            context.waitTicks(18);
            context.takeScreenshot("grave-knight-real-server-death");
            context.waitTicks(8);
            require(server.computeOnServer(mcServer -> {
                for (Entity entity : mcServer.overworld().getAllEntities())
                    if (entity.getTags().contains("overhaul_death_probe")) return false;
                return true;
            }),"Death animation must preserve vanilla corpse removal");
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
            LOG.info("CLIENT_SMOKE_PASS {} resource sets and synced entities; {} species presented in a real singleplayer world", count,presented);
        }
    }

    private static void require(boolean condition, String message) {
        if (!condition) throw new AssertionError(message);
    }
}
