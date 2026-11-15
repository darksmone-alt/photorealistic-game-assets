# European Sedan 01 – reference vehicle

This folder contains two levels of the same original, unbranded generic sedan:
- `european_sedan_01.obj` + `.mtl`: lightweight OBJ reference/blockout.
- `tools/build_european_sedan.py`: Blender generator for a more detailed version.
- Running the generator creates `european_sedan_01_detailed.glb` in this folder.

## Detailed generator

Run from the repository root with Blender 3.6 or newer:

```bash
blender --background --python tools/build_european_sedan.py
```

The generator creates sculpted lower body panels, cabin glass and pillars, door seams and handles, mirrors, grille, lights, bumper details, wheel arches, alloy wheels and material slots. It uses procedural geometry and materials; no external textures, logos or branded design references are included.

## Technical targets and structure

- Dimensions approx. 4.6 m long; Y-up in source OBJ; vehicle forward +X; width on Z.
- Separate wheel assemblies named `wheel_FL`, `wheel_FR`, `wheel_RL`, `wheel_RR`.
- Each wheel assembly has a hub pivot at its centre and includes tire, rim, spokes and centre cap.
- Dedicated paint material plus glass, rubber, alloy, trim, chrome, LED and tail-lamp materials.
- Geometry is procedural; intended as a generic traffic vehicle, not a replica of a real make/model.

## Important limitations

The detailed GLB is generated locally by Blender and is not committed as a binary asset by this text-only repository workflow. The generator has been committed, but it has not been executed in Blender or imported into the game engine in this session. Polygon count, final GLB size, wheel pivot behaviour, collision, LOD and damage compatibility therefore remain to be measured in the target engine. This is an upgraded prototype, not yet a photorealistic production vehicle.

## Next validation

1. Run the Blender generator and inspect the resulting GLB visually.
2. Confirm wheel pivots, steering and rolling axes in the game engine.
3. Measure triangle count and GLB size against the 30,000-triangle / 3 MB limits.
4. Test material response under daylight, overcast and night lighting.
5. Tune collision, LOD and damage states before duplicating the approach for SUV, sports car, pickup and van.
