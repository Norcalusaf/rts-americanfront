# Briar County — Phase 1 design specification

Status: first reviewable design, 28 October 2026. Unreal Engine 5 and inland Georgia, autumn 1948 are confirmed by the user. Hardware, installed engine version, purchased assets and plugins must be inventoried on the Windows PC. No playable level has been built yet. All timings, counts and distances below are design targets pending playtesting.

## Mission premise

Working mission title: **Operation Homeground**. Liberate the southern approach to the fictional regional city of Briar, Georgia, secure the agricultural settlements, silence an artillery battery and capture the courthouse command district. Intended first successful playthrough: 28–35 minutes, centered on 30 minutes. Single player against sector-based AI; no base building or resource economy in this mission. Unlimited ammunition and fuel, but reloads, aiming, recovery, weapon handling and support cooldowns remain.

Historical divergence: Operation Dynamo at Dunkirk fails in 1940. Britain subsequently falls in this fictional timeline. Pearl Harbor still brings America into the Pacific war; later defeats allow Japanese lodgments on the western mainland. German forces establish Gulf Coast lodgments and advance inland. Canada remains an Allied partner. This mission is a local American counterattack, so the player's south-to-north movement does not imply that the entire invasion front faces that direction.

Dunkirk's failure alone does not explain a successful invasion of Britain or transoceanic invasions of America. Before campaign writing, establish additional fictional outcomes for the Royal Navy, Soviet front, Atlantic shipping and basing, Pacific naval balance, and atomic weapons development. Keep those as explicit alternate-history assumptions, not historical claims. No futuristic weapons are necessary for this mission; initially retain a late-WWII equipment vocabulary into 1948.

American Nazi collaborators are a fictional revived Bund-inspired occupation militia. The actual German American Bund disbanded in December 1941. Klan auxiliaries fighting alongside this invasion are also fictional, not a claim about an actual WWII battle. US regulars and civilian resistance fight alongside Canadian troops. Civilian resistance includes Black and white local residents; their cooperative resistance and any integrated regular units must be explained within the alternate timeline rather than presented as a typical wartime US Army organization.

## Engine and asset pipeline

Use Unreal Engine 5, retaining the existing project's compatible installed version until an isolated copy passes plugin/import tests. C++ for persistent simulation and core systems, Blueprints and data assets for mission assembly and tuning, UMG for interface, Niagara for effects, Chaos for suitable destructible assets. These are proposed implementation choices, not existing functionality.

Reuse order is mandatory: existing Unreal project assets → owned KitBash3D/Cargo library → other owned assets → kitbash/edit in Blender → Tripo for genuinely missing geometry → custom modeling. Inventory existing soldiers before generating any character. Record source, entitlement, scale, rig, materials, collision, LODs and destruction readiness. Keep the paid source library out of public repositories.

Cargo has a direct Unreal workflow; avoid unnecessary round-trips through Blender. Use Blender for modifications, rig corrections, variants and preparation. Tripo is a mesh starting point, not an assumption of production-ready topology, rigging or collision. 8K refers to texture resolution, not inherent gameplay readiness. Reserve large textures for assets that benefit at the chosen camera range; use streaming, instancing and appropriate LODs for repetition.

World Partition/One File Per Actor are candidate map-authoring tools. RTS units must continue simulating when the camera moves away: do not make actor persistence or AI depend solely on camera-distance streaming. Keep mission state independent of streamed visual cells. Profile before selecting a large-crowd framework or adding plugins.

## Authoritative map layout

Revision 2 expands the playable map to **3,200 m east-west × 2,800 m north-south** (8.96 km², about 2.26 times the original area). The expansion emphasizes lateral maneuver and local approach loops, not merely longer travel between objectives. The city continues past the north edge. Use `References/frontline-plan-v2.svg` for current placements and `map-layout.json` for coordinates. The original blockout and painted map are superseded for geometry; original environment and faction boards remain art references.

Origin: southwest, X east, Y north, Z up; meters convert to Unreal centimeters at 100:1. Ridge height remains approximately 35–45 m above lowland. All coordinates are provisional design targets.

| ID | POI | Center X,Y (m) | Footprint (m) |
|---|---|---|---|
| 01 | Allied staging | 1600, 220 | 500×220 |
| 02 | Miller Farm | 950, 850 | 500×380 |
| 03 | Bell Crossroads | 2250, 900 | 480×380 |
| 04 | Central bridge | 1600, 1300 | 160×120 |
| 05 | East ford | 2700, 1320 | 200×160 |
| 06 | Artillery ridge | 1650, 1700 | 700×360 |
| 07 | Pine woods | 500, 1600 | 600×700 |
| 08 | South suburbs | 1400, 2150 | 1200×350 |
| 09 | Rail yard | 2600, 2260 | 650×650 |
| 10 | Courthouse | 1600, 2530 | 700×400 |
| 11 | West bridge | 550, 1280 | 160×120 |

Creek crosses the map near Y=1,300 with three vehicle-capable crossings: west bridge, central bridge and east ford. Crossing choice must not force every approach back through the same checkpoint. Main road plus western logging and eastern agricultural loops connect through lateral roads south of the farms, north of the farms, south of the ridge and behind the ridge. City blocks have multiple entrances and rear streets. Keep enough separation between approaches that one defending position cannot dominate all entrances.

| Objective | Direct approach | Alternate approach | Deep flank / rear connection |
|---|---|---|---|
| Miller Farm | Southern road and farmyard | Western fields and tree belts | Northern gin service lane reached by outer loop |
| Bell Crossroads | Southern village road | Eastern orchards/gardens | Western drainage lane linking north of village |
| Central bridge | Southern road | Either bank for supporting infantry | Cross at west bridge or east ford and approach north bank |
| East ford | Farm track | Creek-bank infantry approach | Eastern perimeter track to north exit |
| West bridge | Logging road | Woodland infantry approach | Central crossing and north-bank connecting track |
| Artillery ridge | Southern access road | Western wooded approach | Eastern service road and rear cross-link |
| Suburbs | Main avenue | Western bungalow/garden lanes | Eastern mill workers' streets |
| Rail yard | Southern service entrance | Western loading streets | Eastern/northern rail-service loop |
| Courthouse | Southern civic avenue | Western commercial blocks | Eastern alleys and northern rear street |

Pine woods is maneuver terrain, not a mandatory capture point. Allied staging is friendly rear area. Provide at least three usable approaches to each combat objective, including at least two practical vehicle approaches where terrain allows. A longer route should offer a meaningful change in cover, observation or attack angle. No mandatory single bridge, one-door capture compound or funnel shared by all paths. Road widths start at 7–9 m for two-way rural roads, 12–16 m city clearances, and 4–5 m tracks with passing spaces; validate against vehicle assets.

## Active American front and initial placements

The attack starts from an existing American defensive line, not an empty deployment zone. US rifle squads U1–U4 occupy broken zigzag trench segments south of the farm settlements. Communication trenches connect to rear shelters; Canadians C1/C2 are local supporting reserves. AT1/AT2 cover road approaches; S is a forward observation/scout team; M is the rear mortar detachment. T1/T2 are Shermans staged behind the line; TR1–TR3 are transports. Use map-layout.json for each icon's center. Squad icons represent full units, not single soldiers.

Between US trenches around Y=600–660 and occupation positions around Y=1,000–1,100 is contested farmland, with irregular cover and patrol gaps. Do not render an uninterrupted trench wall across the entire map: access gaps, shallow sections and vehicle crossings preserve maneuver. US line includes dugouts, aid point, sandbag positions, disturbed soil, stored equipment and abandoned civilian structures. Defensive earthworks must alter cover and traversal, not just decorate the ground. Exact depths, meshes and firing positions are deferred to scale/collision tests.

E1–E4 are farm rifle groups; E5–E7 are ridge groups; E8–E12 defend the city. E4, E7 and E12 are their respective local reserve groups, included in those totals rather than extra forces. G1–G3 are the battery guns. AX1/AX2 are enemy tanks and AC a light armored vehicle. F1/F2/F3 are fictional collaborator groups, K1 the Klan auxiliary group. Resistance groups unlock at the farms and are therefore not initial Allied deployment icons. Red dotted loops show provisional sector patrols; blue dashed loops illustrate alternative player routes, not prescribed orders. This is an all-revealed designer map; gameplay retains fog of war.

Keep fields irregular and bounded by drainage ditches, hedges, timber fences or tracks. Cotton is the main crop; add harvested plots, pasture and kitchen gardens. Pine/oak woodland is clustered, not evenly scattered. Country buildings are timber and corrugated metal; downtown is mostly 2–4-story brick with a few 6–8-story hotels/offices, a courthouse, mill chimney and water tower. No modern highways, glass office towers, modern strip malls or contemporary vehicles.

Approximate land allocation: 30% farmland, 25% woods/creek, 15% farm settlements and ridge, 25% urban/suburban/industrial, 5% staging and transitions. These are visual composition targets, not zoning restrictions.

## Mission beats and pacing

| Time target | Beat | Player task | Completion / consequence |
|---|---|---|---|
| 0–3 min | Deployment | Read frontline, select squads, choose routes | First contact visible ahead; no long empty march |
| 3–10 min | Farms | Secure Miller Farm and Bell Crossroads in either order | Local resistance joins; secured roads admit reinforcements |
| 10–18 min | Ridge | Cross creek, reach battery, disable all three guns | Enemy battery shelling stops; city assault becomes safer |
| 18–27 min | City | Enter suburbs; capture courthouse command district | Rail yard is optional flank/support opportunity |
| 27–30 min | Consolidation | Hold courthouse against a finite local reserve | Victory after reserve defeated or 3-minute hold completed |

Capture requires at least one non-routed infantry squad inside the defined POI and no enemy combatant contesting it, followed by a short visible capture timer (initially 30 seconds). Tanks support but do not capture alone. Gun objectives complete when crews are driven off and the weapons disabled or secured through a clearly shown interaction. No pixel hunting for a hidden last soldier: show contested areas and allow routed defenders to withdraw.

Players may physically bypass earlier objectives. Such objectives remain required for mission completion, and bypassed defenders retain local influence. Do not enforce progression with invisible walls. Early scouting of the city should reveal threats without activating every enemy on the map. Optional rail-yard capture removes one scheduled enemy armored reinforcement and gives a local approach advantage; destroying the mill is not mandatory.

Failure: all controllable combat forces lost or routed with no recoverable reserve. No mandatory hard 30-minute timer. Include checkpoints at farm and battery completion. Support a speed reduction/tactical pause option provisionally for accessibility and squad management. Reinforcements are finite, signaled, and enter along physical roads rather than appearing beside the player.

Calibrate pacing in graybox: the larger map can exceed 30 minutes if every route must be cleared or infantry only walk. The wider flanks are optional; begin squads on the forward trench line and allow transport use on secured roads. Do not add mandatory captures merely to fill the larger area. Use forward initial deployment, transports and overlapping objectives. Measure real travel time, congestion and combat duration; move initial deployments or objective centers closer while retaining lateral maneuver space before artificially increasing soldier speed. Three first-time playtests should cluster near 30 minutes before art lock.

## Initial player force and historical organization

Historical baseline is 1944–45 equipment and organizations deliberately retained into this fictional 1948 war. US rifle squads use the documented 12-man WWII establishment. Postwar organizations changed, so do not describe this as the universal real 1948 establishment. Canadian sections provisionally use the late-war 10-man establishment; verify the selected unit/date in a primary establishment source during Phase 2. German rifle groups provisionally use 9 men, with specialist formations handled separately.

| Controllable formation | Count | People / vehicles | Design role |
|---|---|---|---|
| US rifle squad | 4 | 12 each | Main maneuver and capture force, BAR support |
| Canadian rifle section | 2 | 10 each, provisional | Allied rifle/Bren support |
| Local resistance group | 2 | 8 each, fictional | Local reconnaissance and light infantry; earned at farms |
| Antitank team | 2 | 3 each, game grouping | Bazooka team plus security rifleman |
| Scout/sniper team | 1 | 2, game grouping | Observation and precision support |
| Mortar detachment | 1 | 5, game grouping | Indirect fire and smoke; exact equipment/crew pending |
| Sherman tank section | 1 | 2 tanks, 5 crew each | Armored support; selectable individually or together |
| Transport vehicles | 3 initially | Truck/half-track mix; drivers and seats audited | Shuttle troops; not enough to motorize everyone at once |
| Artillery support | 1 off-map battery | Abstracted crew | Cooldown-based support; no ammo economy |
| Air support | 2 abilities | Strafing and bombing runs | Limited by cooldown/availability and clear approach UI |

At full unlock: 97 infantry/support personnel plus 10 tank crew and transport drivers. This is an initial force proposal, not a historically complete company TO&E. Antitank/sniper/mortar teams are not inflated into 12-person rifle squads. Crewed artillery can be added after battery capture if controls and pacing justify it. Most infantry are selectable as a squad, with individual bodies and casualties represented.

Use recognizable doctrine at game-system level: suppression, morale, sight lines, concealment versus ballistic cover, weapon handling, leaders and communication. Avoid presenting modern four-person fireteams as the default WWII US organization. Squad-level microbehavior handles cover seeking and local repositioning; deliberate suppress-and-maneuver also operates between squads. Germans emphasize their squad machine gun; Canadian sections use a Bren-based support component. These are broad design influences, not universal behavior claims for every unit.

Orders: Move, Attack Move, Attack Target, Defend Facing, Suppress Area, Flank Left/Right, Stop, Retreat, Embark and Disembark. Flank orders preview a valid route and fail clearly if no suitable route exists. Automatic grenades require a valid target, clear trajectory, safe friendly separation and a per-unit cooldown. Infinite ammunition does not mean infinite firing rate or grenade spam. Cover selection must not override a clear move order indefinitely.

## Enemy sectors and encounter framework

Three response sectors: A Farms (Y<1380), B Ridge (1380–1950), C City (Y>1950). Sector boundaries follow terrain/roads where useful rather than acting as invisible perception walls. A unit can shoot a visible enemy across a boundary; the boundary limits dispatch of reserves. Enemy knowledge is based on sightings, sound uncertainty and communicated reports, not player cursor position or omniscience.

Initial encounter budget: A has four German rifle groups and two 6-person collaborator groups; B has three German groups, three artillery crews (provisional 6 each) and one light armored vehicle; C has five German groups, two 6-person collaborator groups and two tanks. One of the small collaborator groups may be Klan auxiliaries. Approx. 150–180 defenders including crews, distributed across the entire mission. Budget is for tuning, not a guaranteed performance result.

Patrol loops: A links farm lane, store and field-edge post; B links battery service track, observation position and woods entrance; C links rail yard, suburban junction and command square. Each loop needs at least three authored points, cover-aware stops and a fallback destination. Place static guards separately so every defense does not vacate during a patrol.

AI state chain: unaware → suspicious → investigating → engaged → regrouping/retreating. Sightings produce timestamped last-known positions with confidence. A valid radio report can request one reserve group from its sector; neighboring sectors only send an explicitly authorized contingent after a mission event and delay. Killing a radio operator does not erase information already transmitted. Reserve travel occurs physically, with cooldowns and finite pools. No map-wide aggro and no endless reinforcement spawning.

Phase 4 will author individual cover positions and exact routes after map traversal tests. The above is the encounter contract needed to build the right spaces now.

## Vehicles, violence and destruction contract

Vehicles need steering and acceleration, hull/turret separation, terrain response, crew states, boarding reservations and collision recovery. Preserve crew seat identity through embark/disembark, injury and vehicle loss. Tank riders sit at authored attachment points, dismount before combat when ordered/AI conditions allow, and are exposed to danger; they are not additional protected internal seats. Interior visibility can use simplified crew representations without modeling every interior immediately.

Target gritty combat: consequential wounds and deaths, blood effects, casualty persistence within a budget, authored death animations blended into ragdolls, impact reactions and suppression audio. Do not equate every bullet hit with extreme dismemberment. Camera-distance readability and credible force take priority over repetitive spectacle. Separate gore intensity from core combat simulation.

Destruction tiers:

1. Cosmetics: bullet impacts, glass fracture, dust, material-specific debris, track marks.
2. Traversable destruction: fences, small trees, poles, light sheds and walls change state and collision; tanks can open paths.
3. Structural destruction: selected buildings have authored fracture/support behavior, damaged states, rubble and updated cover/navigation.
4. Terrain deformation: visible depressions must also affect collision, pathing and cover where gameplay-relevant. A decal alone does not fulfill this goal.

Chaos supports fractured geometry; it does not by itself prove arbitrary persistent cratered terrain for this project. Prototype a deformation solution before committing the final terrain architecture. Store crater/debris state for save/load, bound physics fragment lifetime, and rebuild only affected navigation/cover regions. Full destruction is the final target, not something all imported assets possess.

Tank crushing policy: fences and light obstacles yield readily; small trees topple; larger trees and substantial masonry resist, slow or require damage before passage. Large rocks block. A Sherman driving effortlessly through any solid building would conflict with the realism goal. If the user prefers a more arcade-like crushing rule, expose it as an explicit design choice. No authored objective should become permanently unreachable after destruction.

## Camera and UI

Six selectable presets; values are starting targets for height above the sampled ground, not spring-arm length:

| Preset | Height | Pitch downward | Purpose |
|---|---:|---:|---|
| 1 Close | 18 m | 45° | Inspect soldiers and vehicle boarding |
| 2 Squad | 35 m | 50° | Detailed local combat |
| 3 Tactical | 65 m | 55° | Default candidate |
| 4 Platoon | 110 m | 60° | Several squads and armor |
| 5 Battlefield | 180 m | 65° | Broad coordination |
| 6 Overview | 300 m | 75° | Sector overview; separate full-map overlay |

Use one initial perspective FOV of 50°, smooth interpolation, free pan/rotate, terrain-aware collision, and roof/tree fading where necessary. Measure at the actual display aspect ratio. At high zoom, use squad icons and readable team-color cues rather than expecting uniform detail to remain distinguishable.

UI: objectives top left, support abilities top right, minimap bottom left, selection panel bottom center, contextual orders bottom right. Show squad name, remaining strength, morale/suppression, role, stance and current order; multi-selection summarizes and supports control groups. No fuel or ammo supply bar. Communicate reload/support cooldowns. Preview movement, facing, dangerous routes and blocked orders without filling the screen with permanent clutter. Colored outline/icons supplement clothing; avoid reliance on red/green alone.

## Four-phase production plan and gates

**Phase 1 — design and reference package (this delivery).** Map concept, POI layout, environmental and faction boards, mission flow, initial force/sector plan, engine choice, historical/source notes and PC handoff. User reviews geography and overall identity before high-cost art assembly.

**Phase 2 — characters, squads and vehicles.** Inventory and reuse existing soldiers. Build a small test arena first: one US squad, one enemy squad, one transport and one Sherman. Prove animation/rig compatibility, weapons, cover/suppression, casualty states, transport seats, tank riders, camera presets and command UI. Stress-test several full squads and navigation around wrecks before cosmetic polishing. Then expand factions and equipment. Gate: reliable boarding, coherent squad control, readable combat, no duplicate crew or stuck units, and measured performance on the PC.

**Phase 3 — map build, parallel with Phase 2 after shared contracts exist.** User requests an Astra agent at ultra effort for this work. Start that agent when building begins on the PC; do not start a detailed map build before asset access and design review. Share scale, faction IDs, vehicle clearance, cover markers, collision channels, destruction states and POI IDs. Graybox the complete routes first, validate 30-minute pacing, then replace with owned assets. Stage art by sector and test streaming/navigation/destruction continuously. Gate: a traversable and visually coherent complete map with stable routes after expected damage.

**Phase 4 — encounters and final mission.** Place forces, authored patrols, local alerts, reserves, support abilities and objective scripts. Tune battle difficulty, telegraph artillery/air attacks, fix pathing bottlenecks, complete saves/checkpoints, effects/audio, destruction persistence and performance. Gate: repeatable 28–35 minute first-play clear, both flanks viable, no map-wide AI alerts, no objective softlocks and a sustained agreed framerate during the busiest battle.

Performance target to validate: 60 fps at an agreed resolution on the 5090 PC, with 200–300 total battlefield personnel and a smaller active physics/animation workload near combat. This is not a hardware promise. Measure game-thread, rendering, animation, navigation, effects, memory and debris independently; hardware inventory determines final budgets. Test the destruction slice early in Phases 2/3 rather than discovering terrain limitations in Phase 4.

## Visual reference package

Generated images: overhead map, six-scene environment board, six-faction silhouette board. These are art-direction proposals rather than surveyed plans, verified uniform plates or ready-to-import 3D content. Building silhouettes and the map specification take precedence over accidental details in generation. Costume approval requires a closer equipment reference pass during Phase 2.

American regulars: olive drab, M1 helmets, canvas equipment. Canadian: khaki battledress, period helmet/webbing and CANADA shoulder title; avoid a modern national flag patch. Resistance: period workwear and civilian gear with a small consistent identification cue. German: field gray, steel helmets, military equipment. Collaborators: explicitly fictional brown/charcoal uniform distinct from German regulars. Klan: recognizable shabby off-white robe/hood silhouette; present them as hostile auxiliaries, not glamorous elite soldiers. Uniform clothes alone must not drive friend-or-foe identification.

## Research and reference links

- [National Army Museum: Defeat in the West, 1940](https://www.nam.ac.uk/explore/defeat-west) — historical Dunkirk context; subsequent campaign events are fiction.
- [US Army University Press: Infantry Squad, Part 1](https://www.armyupress.army.mil/Journals/NCO-Journal/Archives/2018/March/Infantry-Squad-Part-1/link/) — 12-man WWII US squad and later doctrinal assessment. Use this as the initial organization baseline, with unit-specific primary tables in Phase 2.
- [Canadian WWII rifle sections: bibliography and overview](https://en.wikipedia.org/wiki/Organization_of_Canadian_Army_rifle_sections_during_World_War_II) — provisional secondary cross-check, not final primary validation.
- [Wartime Canada: 1944 infantry training manual catalog](https://wartimecanada.ca/document/second-world-war/training-manuals/infantry-training-part-vii-section-and-platoon-tactics) — located primary manual for the Phase 2 equipment/tactics validation pass; the full scan has not yet been reviewed.
- [USHMM: German American Bund](https://encyclopedia.ushmm.org/content/en/article/german-american-bund) — historical organization and its 1941 dissolution; a 1948 combat revival is invented.
- [Library of Congress: Greensboro main street, 1939](https://www.loc.gov/item/2017801105/) — brick storefronts, street proportions, period vehicles.
- [Library of Congress: cotton gin reference, Greene County, 1941](https://www.loc.gov/item/2017750940/) — agricultural context; catalog notes possible identification.
- [Amon Carter Museum: Bennie's Grocery, Sylvania](https://www.cartermuseum.org/collection/bennies-grocery-store-sylvania-georgia-p19833514) — rural storefront/pump reference.
- [Georgia crop reports, 1940–41](https://dlg.usg.edu/record/dlg_ggpd_i-ga-ba400-pc7-bp1-bc7-b1940-h41-bfolio) — period cotton cultivation.
- [Epic: Chaos destruction overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/destruction-overview) — geometry collections/fracture capabilities; not proof of terrain deformation.
- [Epic: World Partition](https://dev.epicgames.com/documentation/unreal-engine/world-partition-in-unreal-engine) — streaming and authoring options.
- [KitBash3D: Cargo supported software](https://help.kitbash3d.com/en/articles/7833635-cargo-supported-3d-software-and-render-engines) — verify locally installed compatibility.
- [KitBash3D: Unreal workflow](https://help.kitbash3d.com/en/articles/7833653-using-unreal-engine-with-cargo-workflows-and-integration) — direct asset pipeline.

## Review points remaining

On PC: discover CPU/RAM, Unreal version, project path, asset kits, soldier rigs, plugins, available storage and target monitor resolution. Confirm whether the initial proposed force size and pause option feel right. Review generated map composition and destruction tradeoff before committing detailed art. The present workspace contains no Unreal project or asset inventory, so no claim of asset inspection or PC access is made.
