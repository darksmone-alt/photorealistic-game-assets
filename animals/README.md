# Animals

Target urban and peri-urban species: dogs, cats, pigeons, sparrows, crows, ducks, squirrels and foxes.

Prefer game-ready models with simple locomotion/idle animation, correct scale and LODs. Record model, texture and animation licences independently.

## Approved models (game-ready, animated)

| Model | File | Size | Triangles | Animations | Real-world height | SHA-256 |
|---|---|---|---|---|---|---|
| Husky (Hund) | [animals/quaternius_husky.glb](animals/quaternius_husky.glb) | 446 KB | 1920 | Idle, Walk, Gallop, Eating, Death, Attack | ca. 0.85 m | `4fce8838f048fac4…` |
| Shiba Inu (Hund) | [animals/quaternius_shiba.glb](animals/quaternius_shiba.glb) | 366 KB | 1950 | Idle, Walk, Gallop, Eating, Death, Attack | ca. 0.62 m | `584f95870b78a41e…` |
| Cat (Katze) | [animals/quaternius_cat.glb](animals/quaternius_cat.glb) | 113 KB | 2448 | Idle, Walk, Gallop (aus Run), Eating, Death | ca. 0.36 m | `5ea133c0dafc8500…` |
| Deer (Reh) | [animals/quaternius_deer.glb](animals/quaternius_deer.glb) | 387 KB | 2096 | Idle, Walk, Gallop, Eating, Death | ca. 1.55 m | `23b1edfee93a4025…` |
| Stag (Hirsch) | [animals/quaternius_stag.glb](animals/quaternius_stag.glb) | 380 KB | 3667 | Idle, Walk, Gallop, Eating, Death | ca. 1.95 m | `571f7595db6930b5…` |
| Fox (Fuchs) | [animals/quaternius_fox.glb](animals/quaternius_fox.glb) | 404 KB | 1848 | Idle, Walk, Gallop, Eating, Death | ca. 0.62 m | `11b391994e300f4a…` |
| Crab (Krabbe) | [animals/quaternius_crab.glb](animals/quaternius_crab.glb) | 94 KB | 3624 | Idle, Walk, Death | ca. 0.3 m | `47eaba2fbd07deb5…` |

Style: stylised low-poly (not photorealistic). Rigged and animated, one skinned mesh each, vertex colours, no textures. Forward axis +Z, scale must be set at runtime to the real-world height above.

### Provenance and licence
Quaternius (https://quaternius.com), **CC0 1.0** (public domain, commercial use, modification and redistribution allowed, no attribution required).
Obtained from the npm package `@netforge/asset-library-files` 0.2.0 (https://www.npmjs.com/package/@netforge/asset-library-files), whose NOTICE states that the Quaternius models are per-model GLBs uploaded by Quaternius on Poly Pizza (https://poly.pizza/u/Quaternius) marked Public Domain (CC0), and that models listed there as CC-BY are excluded.
Changes: meshopt compression removed, vertex data quantized (KHR_mesh_quantization), duplicate and unused animation clips removed, clips renamed to plain names. Checked 2026-11-15.
