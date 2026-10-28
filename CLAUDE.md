# American Front — project instructions and agreed direction

Read this file before working. Repository: Norcalusaf/rts-americanfront.

## Current state and source of truth

This repository contains a Phase 1 design package, NOT a playable game or an Unreal project. Development will continue on the user's Windows PC with an RTX 5090. CPU, RAM, installed Unreal version, asset project path and kit inventory must be discovered there; do not claim they have already been inspected.

Read `Design/PHASE_1_BRIAR_COUNTY.md` for the complete mission and production specification, `Design/PC_HANDOFF_PROMPT.md` for continuation, and `Design/map-layout.json` for coordinates and initial placements. The current map is revision 2: `Design/References/frontline-plan-v2.svg` and its PNG preview. Earlier blockout and overhead painting are superseded for layout. Environment and faction paintings remain art-direction references, not verified equipment plates. User corrections take precedence over these documents.

## Confirmed creative direction

- Engine: **Unreal Engine 5**, confirmed by the user. Match the existing asset project's compatible version before considering upgrades. Blender is for asset preparation; Tripo fills genuine asset gaps.
- One single-player top-down RTS mission targeting about **30 minutes**. Working title Operation Homeground, fictional Briar County in inland **Georgia, autumn 1948**.
- Alternate history: the Dunkirk evacuation fails and the Allied force is destroyed; Britain subsequently falls. Pearl Harbor still occurs, the US fares poorly in the Pacific, Japan establishes western mainland lodgments, and Germany invades through Gulf states by sea and air. Canada supports the Americans. These are fictional outcomes requiring additional campaign-world explanations, not claims that Dunkirk's failure alone makes them inevitable.
- Rural southern America: cotton farmland, pine/oak forest, rolling hills, two small farm settlements, then a larger regional city with substantial brick buildings, suburbs, textile mill and rail yard. No modern skyline or suburb styling.
- Americans include uniformed soldiers and local civilians in period workwear and equipment fighting for freedom. Canadians are distinct Allied units. Enemies include German occupiers, fictional American Nazi collaborators with a separate uniform, and Klan auxiliaries in recognizable shabby robes/hoods. Present the latter as hostile extremists, not glamorous elites. A revived 1948 Bund-like militia is fiction; the real Bund disbanded in 1941.

## Map revision 2 — essential user corrections

The user rejected the initial layout as too small/linear and explicitly requested multiple ways to assault each point. Use **3,200 × 2,800 meters**, about 2.26 times the original map area. Increase usable lateral maneuver space, not just travel distance.

- Each combat objective needs at least three distinct approaches: direct, covered flank, and rear/deeper loop. Connect routes before and after objectives; do not converge all routes into one chokepoint.
- Three vehicle-capable creek crossings: west bridge, central bridge, east ford. Keep an alternate armored route after bridge destruction.
- The mission starts at the **active American front**, not an empty staging zone. Show occupied zigzag US trenches south of the farm settlements, communication trenches, rear shelters, supporting positions and reserves. Contested farmland separates these from enemy defenses.
- Current design map shows American/Canadian squads, AT teams, scout/sniper team, mortars, two Shermans and transports; enemy rifle groups, trenches, guns, vehicles, local reserves and patrols. Unit icons represent whole formations. Consult JSON for exact provisional positions.
- Blue icons/zigzags are Allied, red are enemies; dashed blue routes show alternative approaches. The design map reveals all units; gameplay should use fog of war.
- Keep trenches discontinuous with traffic gaps and viable crossings. Test terrain, cover, vehicle traversal and sight lines rather than using trenches as decorative lines.
- Objective sequence: secure both farm settlements → silence ridge artillery → capture courthouse district → defeat/hold against a finite local counterattack. Rail yard is an optional advantage. Players may scout and flank ahead; no invisible progression walls.
- Keep roughly 30 minutes through forward deployment, transports and optional flanks, not by requiring a full map clear. Timings and force sizes are untested targets.

## Combat and controls

Full-size WWII rifle squads, individual soldiers and casualties. Initial US baseline is 12 men per rifle squad; provisionally 10 for Canadian sections and 9 for German rifle groups, with unit/date verification before implementation. Do not confuse smaller antitank, sniper or mortar teams with rifle squads. Preserve late-WWII organizations into fictional 1948 deliberately; do not claim they are universal actual postwar establishments.

Initial proposed Allied force: four US rifle squads, two Canadian sections, two resistance groups unlocked at farms, two antitank teams, one scout/sniper team, one mortar detachment, two five-crew Shermans, transports, artillery support and strafing/bombing support. Tune through playtesting.

Clean RTS interface: selection and multi-selection, control groups, strength/morale/current-order details, minimap and contextual actions. Orders include move, attack move, attack target, defend facing, suppress, flank left/right, retreat, embark and disembark. Units seek cover, reposition and use grenades automatically with trajectory/friendly-safety checks and cooldowns. Suppression, morale, observation, cover versus concealment, credible weapon handling and coordination between squads matter. Avoid modern fireteam assumptions or perfect AI knowledge.

Unlimited ammo and fuel for now: no gas/supply economy. Retain reloads, firing cadence and support cooldowns. Six selectable camera presets are specified in JSON; test readability and roof/tree occlusion on the actual display.

Enemies patrol and communicate locally. Use farm/ridge/city response sectors with finite reserves, last-known sightings and delays. A local contact must not activate the whole map. Cross-sector perception is possible; reserve dispatch is controlled. Reinforcements arrive on physical routes, not beside the player.

## Vehicles, casualties and destruction

Polish rigs, animations, weapon handling, deaths, boarding, crew seats and movement. Transports carry actual assigned occupants. Tanks have crews and support externally seated riders as seen on Shermans; riders are exposed and can dismount. Do not duplicate or lose occupants during seat transitions.

The user wants brutal, bloody combat with credible casualty animation and eventual extensive environment destruction: bullet marks, breaking glass, structures, trees and actual ground depressions from shell impacts. Cosmetic crater decals alone do not satisfy the final goal. Terrain changes must have appropriate collision, cover, navigation and persistence.

The user wants tanks to drive over nearly all obstacles except huge solid rocks. The current proposed realism compromise is easy crushing of fences/light structures/small trees, with substantial masonry/large trees requiring force, damage and slowing. This compromise has been explained but not explicitly approved; retain it as a review point, not an agreed restriction. Prototype before settling behavior.

Chaos fracture is a candidate for structures, not proof of arbitrary deformable terrain. Test the destruction/terrain architecture early, including rubble pathing, save/load and bounded physics debris. A 5090 does not eliminate CPU/AI/navigation costs. Profile before promising 60 fps or full-map simulation fidelity.

## Asset reuse is mandatory

Inventory the user's existing Unreal project, owned KitBash3D/Cargo kits, other owned assets and existing soldiers BEFORE creating replacements. Order: reuse → adapt/kitbash → Blender edits → Tripo for confirmed missing assets → custom creation. Keep source, license, scale, rig, collision, material, LOD and destruction-readiness records. Catalog availability is not proof of ownership.

Keep existing compatible assets in Unreal when possible; do not route everything unnecessarily through Blender. 8K textures do not make models game-ready. Use appropriate texture sizes, streaming, instancing and geometry budgets. Preserve original projects and source assets; test integration in a working copy.

## Four phases and delegation

1. **Map design:** concept/reference images, POIs, routes and design specification. Current package is reviewable, not final gameplay validation. Revision 2 supersedes the initial narrow layout.
2. **Characters and combat:** reuse existing soldiers, rigs, movement, squad behavior, weapons, death animations, transports, tanks/crews/riders. Start in a small test arena and polish functional behavior before expanding.
3. **Map build:** may run alongside Phase 2. User explicitly requested **another Astra agent at ultra effort**. Start that agent on the PC after project/asset discovery and shared contracts are established. Assign separate map/asset ownership; avoid simultaneous writes to the same binary Unreal packages. Build complete graybox routes first, then replace with owned assets and add detail.
4. **Placement and mission:** implement exact squad positions, patrols, local alerts, finite reserves, support and objective scripts; tune difficulty, pacing, destruction, performance and checkpoints. Initial placement planning already exists because the user asked to see it in Phase 1.

Do not skip graybox testing in favor of detailed art. Check full squad movement, tank clearance, alternate access after destruction, no mission softlocks and first-play pacing. Preserve the user's high-detail/lived-in environment goal while measuring performance.

## Working conventions

Keep design, JSON and diagrams consistent after changes. `Design/tools/revise_map.py` reproduces the v2 schematic/JSON but contains hardcoded layout data; update it when changing those sources. Generated imagery may contain incorrect insignia, weapons or scales. Verify before using it as modeling reference.

Use Git for source/config/design. Use Git LFS as appropriate once Unreal binary assets are introduced. Do not upload the full paid source library or credentials; verify licensing and repository visibility before licensed-content transfer. This initial repository contains project-authored design and concept images only.

Report actual results, tests and blockers. Do not say assets were inspected, a build ran or content reached the PC unless verified. Continue from the latest user correction rather than restarting the plan.
