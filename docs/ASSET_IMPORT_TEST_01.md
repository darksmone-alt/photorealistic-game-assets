# Asset import test 01 – vehicle and pedestrian

Status: candidate selection only. No third-party binary has been downloaded, imported into the game, or approved for release yet.

The existing Poly Haven surface textures remain unchanged. This test is deliberately limited to one vehicle and one humanoid so that import problems are found before building a larger asset set.

## Test A – branded vehicle candidates

The following Sketchfab pages currently list downloadable models under **CC Attribution (CC BY)**. The triangle counts are taken from the publisher pages. These are candidates, not approved assets. A Sketchfab download option does not by itself prove that the downloaded archive contains a GLB; check the actual available export formats and file size after download.

| Priority | Candidate | Publisher-reported geometry | Licence | Assessment |
|---|---|---:|---|---|
| 1 | [BMW E30 1985 White – ROH3D](https://sketchfab.com/3d-models/low-poly-car-bmw-e30-1985-white-9dea494b447e442fafbddfc7eccbf158) | 13.1k triangles / 7k vertices | CC BY | First BMW candidate to inspect; reasonable polygon budget. |
| 2 | [Volkswagen Golf II – ARDmation](https://sketchfab.com/3d-models/volkswagen-golf-ii-740500f10bc94e7a91c2290e445fcb39) | 15.2k triangles / 8.9k vertices | CC BY | Textures reportedly authored in Substance Painter; inspect material quality and style. |
| 3 | [Mercedes-Benz 190E – KidBi-Gaming](https://sketchfab.com/3d-models/mercedes-benz-190e-low-poly-game-ready-3d-car-f2b6bf0fb04e426286f0043267d71980) | 21.8k triangles / 10.6k vertices | CC BY | Publisher describes it as game-ready, with UVs, textures, configured materials and separate wheels; still inspect actual pivots and geometry. |
| 4 | [BMW E30 – D_U](https://sketchfab.com/3d-models/low-poly-bmw-e30-fc6fb3a940b14615b87362edcdd5f221) | 13.7k triangles / 7.5k vertices | CC BY | Backup BMW candidate; creator describes the appearance modestly, so visual review is important. |

Source listing checks: ROH3D BMW E30 (13.1k triangles, CC BY); ARDmation Golf II (15.2k, CC BY); KidBi-Gaming Mercedes 190E (21.8k, separate wheels stated, CC BY); D_U BMW E30 (13.7k, CC BY). These listings establish the stated counts and page licences only, not successful downloads or in-game compatibility.

Checks required for each downloaded model:
1. Confirm that the four wheel objects are individually addressable and their origins/pivots are at the hubs. Separate meshes alone do not guarantee correct pivots.
2. Confirm front-wheel steering and wheel rotation in the game.
3. Confirm the body paint is a separate material slot and can be recoloured at runtime.
4. Check scale, forward axis, normals, UVs, texture dimensions, draw calls and final GLB size against the project limits (30k triangles, 3 MB including runtime textures, textures no larger than 1K).
5. Check visual fidelity against the game's existing traffic. Reject models that look too stylised or inconsistent with the target city.
6. Record creator, source URL and exact attribution in `LICENSES.md` and `CREDITS.md` before any public release.

**Legal note:** CC BY is the model creator's stated copyright licence; it does not necessarily grant rights to use a vehicle manufacturer's protected trademarks, logos or vehicle design in every commercial context. Keep logos and badges out and obtain a separate legal review before commercial release of recognisable branded vehicles.

Decision: candidates for inspection and a technical import test only; none is approved as a final production vehicle.

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
