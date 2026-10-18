# Reusable initial AI profiles

The thirteen species use four shared profile classes in `entity.expansion`, each inheriting the original implementation. The original four entity IDs/classes remain intact. Their only source changes are removal of `final` and restricting scout recruitment to the same `CreatureKind`; this prevents newly added scout descendants from changing original goblin cooperation.

| Profile | Species | Inherited mechanics |
| --- | --- | --- |
| Scout | Vampire, Centaur, Sahuagin, Valkyrie, Anubis, Kobold, Cyclops, Dhampir | Timed melee, circling, same-species recruitment (four allies maximum every 40 ticks) |
| Shaman | Fox Spirit Girl, Werecat | Ranged fire bolts, original periodic allied healing, cast animation |
| Slime | Holstaurus | Defensive guardian targeting, slime bubbles, original 35-tick hops |
| Demon | Ender Dragon Girl, Succubus | Dark bolts, close-range teleport, original 100/30-tick teleport cooldowns |

Every concrete species returns a literal enum from `kind()`. This is intentional: Minecraft registers goals and combat timelines during superclass construction, before subclass fields are initialized. Do not replace these methods with a constructor-assigned kind field.

`CreatureKind` supplies movement speed, damage, range, windup/recovery and dimensions; vanilla attributes supply detection range (`FOLLOW_RANGE`). Inherited goals select players for hostile profiles and monsters for the guardian/slime profile. Override `registerGoals` when adding a distinct target policy or aggression mode. `AiProfile` centralizes projectile choice, projectile speed, combat particles and animation metadata. Override `aiProfile()` or `performAttack` for new behavior; override `attackRange()` for an attack-specific reach. Keep `CreatureKind.range` consistent because inherited navigation also uses it. All attack releases, recruitment, healing and particles execute on the server, with the existing synchronized GeckoLib triggers and combat timelines.

Sahuagin retains scout attacks and cooperation, but uses vanilla amphibious navigation, smooth swimming movement/look controls, unrestricted underwater breathing, and separate water/land wander goals. Removing the inherited float goal prevents forced surfacing during underwater fights. Its water travel applies server-authoritative acceleration and drag; ordinary land travel remains vanilla. Swimming state uses vanilla entity synchronization. The aquatic adaptation is confined to Sahuagin.

Winged species use their requested initial ground/magic profiles. Wings do not imply new flight, boss phases or aerial combat. The silver-haired creature is Werecat and has no invented wings. Visual rigs and assets are independent from this AI implementation.

Validation is coordinated by the integration agent: these files do not claim a successful compile, server run or client animation check until the corresponding integration checks run. Original code and no third-party AI source were used.
