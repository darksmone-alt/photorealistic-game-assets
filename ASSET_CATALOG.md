# Asset catalogue and acquisition plan

Target: photorealistic European metropolis inspired by Frankfurt am Main. This file is the source of truth for approved assets and candidates.

## Approval checklist
For each asset, record:
- Asset name and category
- Creator / publisher
- Original source page and direct download page
- Exact licence name and version
- Attribution text required by the licence
- Permitted use: commercial game, modification, redistribution in project
- Original format, runtime format, texture resolution
- Polygon / texture optimisation notes
- Date checked and reviewer

Do not mark an asset approved based only on a search-result snippet or collection-level licence statement. Check the individual asset page and any separate texture, model or animation terms.

## Verified first-pack assets

| Asset | Category | Creator / publisher | Licence | Use in project | Source |
|---|---|---|---|---|---|
| Urban Street 01 | HDRI / overcast urban light | Andreas Mischok / Poly Haven | CC0 | City street diffuse lighting and reflections | https://polyhaven.com/a/urban_street_01 |
| Urban Street 03 | HDRI / overcast residential light | Andreas Mischok / Poly Haven | CC0 | Residential streets, soft daylight | https://polyhaven.com/a/urban_street_03 |
| Modern Buildings | HDRI / golden-hour city light | Greg Zaal / Poly Haven | CC0 | Glass/concrete riverfront and warm sunrise | https://polyhaven.com/a/modern_buildings |
| Modern Evening Street | HDRI / dusk city light | Grzegorz Wronkowski / Poly Haven | CC0 | European office street, mixed artificial and natural light | https://polyhaven.com/a/modern_evening_street |
| Concrete 049 | PBR material | ambientCG | CC0 1.0 | Candidate for concrete/stone aggregate surfaces; verify visual fit before use | https://ambientcg.com/view?id=Concrete049 |

Poly Haven states that all HDRIs, textures and models on its platform are CC0, including commercial use and redistribution: https://polyhaven.com/license
ambientCG states that downloadable assets are CC0 1.0, including commercial use and inclusion of raw files in games: https://docs.ambientcg.com/license/

The source pages are verified, but the binary files have not yet been downloaded into this repository. See [STARTER_PACK_01.md](STARTER_PACK_01.md).

## Original procedural models now in repository

| Asset | Category | Format | Rights | File |
|---|---|---|---|---|
| Urban block 01 | City block scene | OBJ + MTL | Original procedural geometry | [Model](city/urban_block_01.obj) |
| Residential block module 01 | Building facade | OBJ + MTL | Original procedural geometry | [Model](city/residential_block_module_01.obj) |
| Road intersection 01 | Roads | OBJ + MTL | Original procedural geometry | [Model](roads/road_intersection_01.obj) |
| Street tree 01 | Nature | OBJ + MTL | Original procedural geometry | [Model](nature/street_tree_01.obj) |
| European hatchback 01 | Vehicle | OBJ + MTL | Original procedural geometry | [Model](vehicles/european_hatchback_01.obj) |
| Pedestrian mannequin 01 | People | OBJ + MTL | Original procedural geometry; unrigged blockout | [Model](people/pedestrian_mannequin_01.obj) |
| City pigeon 01 | Animals | OBJ + MTL | Original procedural geometry; blockout | [Model](animals/city_pigeon_01.obj) |

These are editable starter meshes, not photorealistic scans. See [ASSET_PACK_01.md](ASSET_PACK_01.md) for contents, import notes and quality limitations.

## Pending source collections

| Category | Source collection | Status |
|---|---|---|
| Trees | https://polyhaven.com/models/nature/trees | Individual model selection pending |
| Architecture | https://polyhaven.com/models/architecture | Individual model selection pending |
| Urban HDRIs | https://polyhaven.com/hdris/streets-town | Additional daylight/night presets pending |
| Community models | https://sketchfab.com/ | Individual CC0/CC BY licence checks required |

## Target environment packs

| Pack | Required contents | Initial target |
|---|---|---:|
| City core | Historic blocks, mixed-use perimeter blocks, shop fronts, roof details | 12–20 |
| High-rise district | Office towers, glass facades, podiums, roof equipment | 6–10 |
| Residential | Post-war blocks, modern apartments, balconies, entrances | 10–15 |
| Roads | Straight roads, curves, junctions, roundabouts, crossings, kerbs | 10–15 |
| Street props | Lamps, signs, bollards, benches, bins, traffic lights | 20–30 |
| Nature | Deciduous/conifer trees, shrubs, grass, park props | 20–30 |
| Vehicles | Unbranded cars, vans, buses, bicycles | 8–12 |
| People | Pedestrians with varied clothing, body types and walk cycles | 5–10 |
| Animals | Dogs, birds, cats and common urban wildlife | 5–8 |
| Materials | Asphalt, concrete, brick, plaster, glass, stone, paving | 15–25 |
| Lighting | Clear noon, overcast, golden hour, blue hour, night | 5 profiles |

These are collection targets, not claims that assets have already been sourced.

## Technical acceptance
- Preferred exchange/runtime format: glTF 2.0 / GLB.
- Textures: PBR metallic-roughness workflow.
- Keep original downloads unchanged in source archives where redistribution is allowed.
- Provide optimised GLB variants for runtime; document any decimation, texture resizing or atlas baking.
- Avoid brand logos, identifiable trademarks and real-person likenesses unless rights are clear.
- Do not scrape proprietary 3D map data or convert services whose terms prohibit reuse.
