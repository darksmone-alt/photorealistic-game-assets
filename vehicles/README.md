# Vehicles

Target: generic, unbranded European passenger cars, delivery vans, buses, taxis without real operator marks, bicycles and service vehicles.

Check model licence and trademark/design restrictions individually. Prefer game-ready GLB assets with wheel pivots, sensible scale, collision proxy and optional interior. No manufacturer logos unless explicitly licensed.

## Approved game-ready cars: Collect Cars (CC BY 4.0)

Original concept designs (no real makes or logos). glTF 2.0, metres, Y-up, nose along +Z, centred on the origin with wheels on the ground. Each wheel is a separate group of nodes named `*_Wheel_FL|FR|RL|RR_*`, so wheels can spin and steer. Body paint uses materials named `Paint_*` (Streamliner: `*LiquidGraphite*`), which can be swapped for a recolourable material at runtime. PBR materials with clearcoat, no textures.

| Model | File | Size | Triangles (original → game) | L × W × H (m) | SHA-256 |
|---|---|---|---|---|---|
| Hypercar | [vehicles/collect/collect_hypercar.glb](vehicles/collect/collect_hypercar.glb) | 478 KB | 196,500 → 30,204 | 4.72 × 2.05 × 1.25 | `ffd06a3edef6f977…` |
| Endurance (LMP-style) | [vehicles/collect/collect_endurance.glb](vehicles/collect/collect_endurance.glb) | 603 KB | 247,752 → 34,057 | 4.91 × 1.97 × 1.32 | `b0ecf5912b2aee9a…` |
| Streamliner | [vehicles/collect/collect_streamliner.glb](vehicles/collect/collect_streamliner.glb) | 454 KB | 389,520 → 31,217 | 5.22 × 1.63 × 1.29 | `2ff0384b43e4472a…` |
| 80s Wedge | [vehicles/collect/collect_wedge.glb](vehicles/collect/collect_wedge.glb) | 594 KB | 71,240 → 31,755 | 4.43 × 2.07 × 1.20 | `978a57ad6f9dbe1d…` |
| Rally | [vehicles/collect/collect_rally.glb](vehicles/collect/collect_rally.glb) | 1174 KB | 127,812 → 38,330 | 4.65 × 2.10 × 1.80 | `9c4be1c5961b3c80…` |

### Provenance and licence
Source: https://github.com/drcollect/collect-cars (models/full/*.glb), by drcollect. Licence: Creative Commons Attribution 4.0 International (CC BY 4.0), https://creativecommons.org/licenses/by/4.0/ — commercial use and modification allowed, **credit required**.

Required credit: *"Collect Cars" by drcollect (https://github.com/drcollect/collect-cars), licensed under CC BY 4.0. Changes: simplified to about 30,000 triangles (meshoptimizer), vertex data quantized.*

Changes made here: welded, simplified with meshoptimizer (target ≈30k triangles), deduplicated, quantized (KHR_mesh_quantization). Checked 2026-11-15.

