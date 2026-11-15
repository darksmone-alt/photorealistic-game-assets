# European Sedan 01 – reference vehicle

Original procedural low-poly generic four-door sedan for prototyping. No real-world brand, badge, or logo.

## Technical details
- OBJ + MTL; metres; Y-up; forward +X; width on Z
- Separate wheel objects: `wheel_FL`, `wheel_FR`, `wheel_RL`, `wheel_RR`
- Wheel mesh origins are centred on their hubs; front wheels can be steered by rotating around Y
- Dedicated `paint` material slot; body panels use this slot
- Additional slots: `glass`, `rubber`, `hub`, `trim`, `lamp`, `red`
- No external textures; materials are editable placeholders

## Important limitations
This is a clean geometry prototype, not a photorealistic production vehicle. It intentionally has a simple body and wheel-arch approximation. It has not yet been imported into the game engine, converted to GLB, or tested with the game's vehicle physics, collision, LOD, or damage system. The geometry is original and procedural.

## Next validation
1. Import OBJ and verify Y-up/+X-forward convention.
2. Check wheel pivots and steering/rotation in the engine.
3. Replace placeholder materials with PBR paint, glass, rubber, and metal.
4. Refine wheel arches, mirrors, door seams, grille, bumpers, and light clusters before production use.
