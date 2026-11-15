# Asset pack 01 — original procedural European city kit

The following model files are now stored in this repository. They are original procedural starter geometry created for this project, not downloaded photogrammetry or finished photorealistic scans.

## Included models

| Asset | File | Companion material | Contents |
|---|---|---|---|
| Urban block 01 | [city/urban_block_01.obj](city/urban_block_01.obj) | [MTL](city/urban_block_01.mtl) | Three buildings, road, sidewalks, crossings, lamps, trees and parked cars |
| Residential module 01 | [city/residential_block_module_01.obj](city/residential_block_module_01.obj) | [MTL](city/residential_block_module_01.mtl) | Reusable 12 × 9 m residential facade module |
| Road intersection 01 | [roads/road_intersection_01.obj](roads/road_intersection_01.obj) | [MTL](roads/road_intersection_01.mtl) | Four-way intersection, sidewalks, road markings and crossings |
| Street tree 01 | [nature/street_tree_01.obj](nature/street_tree_01.obj) | [MTL](nature/street_tree_01.mtl) | Procedural trunk and layered foliage |
| European hatchback 01 | [vehicles/european_hatchback_01.obj](vehicles/european_hatchback_01.obj) | [MTL](vehicles/european_hatchback_01.mtl) | Generic unbranded car blockout with glass and wheels |

| Pedestrian mannequin 01 | [people/pedestrian_mannequin_01.obj](people/pedestrian_mannequin_01.obj) | [MTL](people/pedestrian_mannequin_01.mtl) | Basic unrigged pedestrian blockout |
| City pigeon 01 | [animals/city_pigeon_01.obj](animals/city_pigeon_01.obj) | [MTL](animals/city_pigeon_01.mtl) | Simple urban bird blockout |

## Import

These are Wavefront OBJ files. Keep each MTL file beside its matching OBJ. In Three.js, use OBJLoader and MTLLoader; in Blender, use File → Import → Wavefront (.obj).

A Blender conversion helper is provided at [tools/convert_obj_to_glb.py](tools/convert_obj_to_glb.py).

## Important quality note

These are useful editable 3D starter meshes with approximate material colours and roughness. They are not yet photorealistic production assets: they do not include scanned surface textures, detailed interiors, proper vehicle wheel geometry, rigged characters, or high-quality vegetation. The next pass should add verified CC0 texture sets/HDRIs and replace the simplified models with higher-detail assets where available.

## Rights

The meshes in this pack were generated procedurally for this repository and contain no third-party model files. Third-party downloads are tracked separately with source and licence evidence.
