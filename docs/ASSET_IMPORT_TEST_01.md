# Asset import test 01 – vehicle and pedestrian

Status: candidate selection only. No third-party binary has been downloaded, imported into the game, or approved for release yet.

The existing Poly Haven surface textures remain unchanged. This test is deliberately limited to one vehicle and one humanoid so that import problems are found before building a larger asset set.

## Test A – vehicle

Candidate: [Low-Poly Sedan car by scailman on Sketchfab](https://sketchfab.com/3d-models/low-poly-sedan-car-aeb2699532b4402e8b75ec8888b800b9)

Publisher listing states:
- 6.3k triangles and 3.9k vertices.
- Wheels are separate elements; doors, steering wheel and lights are also separate.
- Licence shown on the model page: Creative Commons Attribution (CC BY).
- The model page offers a downloadable model. Confirm the actual downloaded format and file size before integration.

Checks required after download:
1. Confirm the four wheel objects are individually addressable and their origins/pivots are at the hubs. Separate meshes alone do not guarantee correct pivots.
2. Confirm front-wheel steering and wheel rotation in the game.
3. Confirm the paint is a separate material slot and can be recoloured at runtime.
4. Check scale, forward axis, normals, UVs, texture dimensions, draw calls and final GLB size.
5. Check the visual style against the game's existing traffic. This candidate is explicitly low-poly and may be rejected if it looks too stylised.
6. Record creator and exact attribution in `LICENSES.md` and `CREDITS.md` before any public release.

Decision: candidate for a technical import test only; not approved as a final visual-quality vehicle.

## Test B – humanoid

Primary candidate: [Mixamo](https://www.mixamo.com/), using one of its standard humanoid sample characters (for example Y Bot) and a small animation set.

Adobe's official FAQ says Mixamo is free with an Adobe ID, does not require a Creative Cloud subscription, and permits use of characters and animations in commercial projects including video games:
[Adobe Mixamo FAQ](https://helpx.adobe.com/creative-cloud/faq/mixamo-faq.html)

Adobe's instructions confirm FBX upload/download and animation application:
[Adobe – Upload and rig characters with Mixamo](https://helpx.adobe.com/creative-cloud/help/mixamo-rigging-animation.html)

Important:
- The first test should be one character with idle, walk, run, jump, crouch and one combat animation.
- Download FBX with skin and embedded textures; then convert to GLB and validate in the target engine.
- Verify identical skeleton hierarchy, bone names, rest pose and scale for every animation clip.
- Verify root motion vs in-place behaviour, looping, foot contact and controller integration.
- Do not commit raw Mixamo downloads to this public repository until the applicable redistribution terms have been checked. Commercial use in a game and redistribution of source files as a standalone asset pack are not the same question.
- The standard Mixamo sample characters are only a rig/animation pipeline test. They do not yet satisfy the final requirement for 6–10 varied, realistic pedestrians with everyday clothing.

Alternative for a fully CC0 pipeline: [Quaternius Universal Base Characters](https://quaternius.com/packs/universalbasecharacters.html) plus [Universal Animation Library](https://quaternius.com/packs/universalanimationlibrary.html). The publisher lists six humanoid bases, average 13k triangles, a compatible humanoid rig and 120+ animations under CC0. However, the style is stylised/low-poly, so this is a technical fallback, not the preferred photoreal pedestrian solution.

## Acceptance checklist

| Check | Vehicle | Humanoid |
|---|---|---|
| Downloaded source file recorded | pending | pending |
| Licence and redistribution checked | pending | pending |
| Imports without errors | pending | pending |
| Correct scale and orientation | pending | pending |
| Runtime size within target | pending | pending |
| Geometry / triangle count checked | pending | pending |
| Materials and textures checked | pending | pending |
| Animation / wheel behaviour tested | pending | pending |
| In-game visual review passed | pending | pending |
| Approved for production | no | no |

## Important scope

This document records candidate selection and the test procedure only. It does not claim that the candidate files have been downloaded, converted, or tested. Keep the existing placeholder models out of production use. Do not alter the already integrated Poly Haven textures as part of this test.
