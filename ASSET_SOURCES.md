# Free asset source portals and acquisition workflow

This is a source shortlist, not an approval of every file hosted by these platforms. Check the individual asset's licence and download terms before adding it to the game.

## Verified CC0 starting points

| Source | Best use | Licence | Website |
|---|---|---|---|
| Poly Haven | HDRIs, PBR materials, selected 3D models | Publisher states all its HDRIs, textures and 3D models are CC0; commercial use and redistribution are permitted | https://polyhaven.com/ |
| ambientCG | PBR surface materials, selected models/HDRIs | Downloadable assets are CC0 1.0; commercial use and bundling in a game are permitted | https://ambientcg.com/ |

Licence evidence:
- Poly Haven: https://polyhaven.com/license
- ambientCG: https://docs.ambientcg.com/license/

## Other sources requiring per-asset checks

| Source | Best use | Licence handling | Website |
|---|---|---|---|
| Sketchfab | Specific buildings, vehicles, people and props | Per-model licence varies; filter downloadable models and inspect exact licence. CC0/CC BY only unless separately cleared | https://sketchfab.com/ |
| OpenStreetMap | Road/building footprints and urban layout data | ODbL; attribution and share-alike obligations apply to database use. Not a library of photorealistic meshes | https://www.openstreetmap.org/ |
| MakeHuman | Generate human base meshes | Check current project and asset terms for generated model and add-ons | https://www.makehumancommunity.org/ |
| Mixamo | Character rigging and animation workflow | Adobe terms apply; do not assume animation/source files can be redistributed as a standalone asset pack | https://www.mixamo.com/ |

## Acquisition order

1. Build the city layout from openly licensed geodata or modular procedural geometry.
2. Source environment HDRIs and surface materials from CC0 libraries.
3. Add architecture and street props from individually verified downloadable models.
4. Add generic, unbranded vehicles and characters only after checking model, texture, rig and animation terms separately.
5. Convert approved runtime models to GLB/glTF, optimise, and document modifications.

## Not approved by default

- Search-result thumbnails or asset aggregators without the original asset page.
- Assets labelled only “free” without a clear licence.
- NonCommercial, NoDerivatives, editorial-only, personal-use-only or unclear terms.
- Proprietary 3D map captures or scraped content from mapping services.
- Branded vehicles or identifiable people without clear rights.

## Asset intake record

Use this template in ASSET_CATALOG.md for every approved file:

- Asset title:
- Category:
- Creator:
- Original asset page:
- Download URL:
- Licence and version:
- Commercial game use permitted:
- Modification permitted:
- Redistribution bundled in game permitted:
- Required attribution:
- Original file format:
- Runtime format:
- Texture maps and resolution:
- Optimisation performed:
- Date checked:
