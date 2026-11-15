# Starter pack 01 — European city atmosphere

This first pack establishes real-world lighting and material references. It is a curated download list; the actual binary downloads remain hosted by their creators and are not copied into this repository yet.

## 1. Urban lighting HDRIs — Poly Haven (CC0)

All Poly Haven HDRIs are published under CC0. Commercial use and redistribution are permitted by the publisher. Choose 2K/4K for real-time preview and higher resolutions for offline reference or skybox baking.

| Asset | Intended use | Source |
|---|---|---|
| Urban Street 01 | Overcast urban street, asphalt, parked cars and trees; neutral daylight | https://polyhaven.com/a/urban_street_01 |
| Urban Street 03 | Overcast European residential street; soft diffuse daylight | https://polyhaven.com/a/urban_street_03 |
| Modern Buildings | Golden sunrise on modern glass/concrete riverfront; warm city reflections | https://polyhaven.com/a/modern_buildings |
| Modern Evening Street | European office street at dusk; mixed cool sky and warm street lighting | https://polyhaven.com/a/modern_evening_street |

Licence: https://polyhaven.com/license

## 2. Surface materials — ambientCG (CC0 1.0)

| Asset | Intended use | Source |
|---|---|---|
| Concrete 049 | Photogrammetry concrete/stone aggregate surface; test for sidewalk or exposed aggregate use | https://ambientcg.com/view?id=Concrete049 |

ambientCG states that its downloadable assets are CC0 1.0, including use in commercial games and redistribution of raw files. Licence: https://docs.ambientcg.com/license/

## 3. Vegetation model collection — Poly Haven (CC0)

Browse the Trees collection for suitable deciduous/conifer assets. Select individual models based on silhouette, season and polygon/LOD availability before adding a specific model to the approved asset register.

Source: https://polyhaven.com/models/nature/trees

## 4. Architecture model collection — Poly Haven (CC0)

Browse the Architecture collection and inspect modular facade/building assets. The collection is currently small, so it will be supplemented with individually licensed community models and procedural building modules.

Source: https://polyhaven.com/models/architecture

## Runtime notes

- HDRIs: download EXR for lighting workflows; use a lower-resolution runtime environment map or prefiltered PMREM for the game.
- PBR materials: start with 2K maps for hero surfaces and 1K for distant/repeated surfaces; verify map channels and normal-map convention.
- Models: prefer GLB/glTF; if a source offers only Blender/FBX, convert and validate materials, scale, pivots and LODs before integration.
- Keep original source files and licences in a separate source archive if redistribution is permitted.
- This list is not a claim that every item has already been downloaded or integrated into the game.
