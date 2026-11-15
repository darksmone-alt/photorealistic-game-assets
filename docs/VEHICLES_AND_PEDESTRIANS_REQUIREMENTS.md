# Vehicle and pedestrian asset requirements

This specification is mandatory for any third-party asset added to the project. Do not treat a search result, model title, or collection-level licence as approval.

## Vehicles

### Required variants
- Generic unbranded sedan
- Generic unbranded sports car
- Generic unbranded SUV
- Generic unbranded pickup
- Generic unbranded van / transporter
- Emergency variants where suitable: police, ambulance, fire engine

### Runtime requirements
- Target: <= 30,000 triangles per vehicle; hard reject above this without explicit approval.
- Target package size: <= 3 MB per vehicle including runtime textures.
- Texture maps: <= 1K; prefer one compact atlas or a small set of materials.
- Four wheels must be separate mesh nodes/objects, each with its pivot at the wheel hub:
  - wheel_FL
  - wheel_FR
  - wheel_RL
  - wheel_RR
- Front wheels must support steering; all wheels must support rotation.
- Body paint must be a separate material slot / material instance so runtime paint colour can change without duplicating the mesh.
- No high-detail interior; simple dark cabin/glass is enough for traffic vehicles.
- No real manufacturer badges, logos, trademarks or copied game assets.
- Prefer GLB/glTF 2.0; FBX may be accepted as source only if conversion is tested and documented.

### Damage compatibility
The current procedural vehicle damage system deforms project-authored body geometry. Imported cars cannot be assumed to support equivalent vertex-level deformation. For imported vehicles, use coarse damage states (intact / dented panels / heavily damaged) or detachable/replaced body panels. Keep the existing procedural vehicle as the damage-system reference implementation until imported deformation is proven.

## People

### Required variants
- 6–10 complete pedestrian characters with varied masculine/feminine presentation, body proportions and everyday clothing.
- Avoid identifiable real-person likenesses and branded clothing.
- Keep the existing modular character creator available; imported complete characters are an additional preset route, not a replacement for the customisable modular system.

### Rig and animation
- All imported characters must use the exact same skeleton hierarchy, bone names, rest pose and scale.
- Preferred common humanoid target: Mixamo-compatible skeleton, after validating retargeting against the project's animation controller.
- Required clips: idle/standing, walk, run, jump, climb, crouch, swim, melee strike and firearm aim/fire.
- Each clip must be checked for root motion vs in-place behaviour, loop points, foot sliding, hand contact and weapon alignment.
- Do not assume that an animation name guarantees compatibility. Test all clips on the same reference rig before accepting the pack.

### Runtime limits
- Target: <= 15,000 triangles per character; hard reject above this without explicit approval.
- Target package size: <= 2 MB per character including runtime textures.
- Prefer 1K or smaller textures, atlases, shared materials and compressed runtime textures.
- No unnecessary facial microdetail or separate high-poly clothing layers.

## Licence and repository rules

- CC0 preferred.
- CC-BY is acceptable only when the exact asset page confirms the licence and the creator + required attribution are added to `LICENSES.md` and `CREDITS.md`.
- Exclude NC / Non-Commercial, Editorial-only, standard All Rights Reserved, unclear licences, and assets whose redistribution terms are incompatible with the repository.
- Do not include ripped or extracted assets from commercial games.
- Check model, textures, embedded decals, and animations separately where applicable.
- Preserve source URL, author, exact licence, download date, original filename, format, triangle count, texture dimensions and optimisation changes in the asset manifest.

## Candidate source notes (not yet approved/imported)

### Vehicles
- [Sketchfab – downloadable low-poly vehicle search](https://sketchfab.com/search?features=downloadable&type=models&q=low%20poly%20car%20game%20ready): inspect each individual model page. Confirm the per-model licence, wheel separation, paint material slot, triangle count and actual downloadable format. A Sketchfab search result is not licence approval.
- [Cosmo – Low Poly Cars (itch.io)](https://cosmo-art.itch.io/low-poly-cars): publisher describes 12 free models, approximately 3,000 triangles each, a small atlas and CC0 for the free pack. Candidate only; download and inspect wheel pivots, material slots, visual style and package size before acceptance.
- [RgsDev – Free Low Poly Vehicles Pack (Sketchfab)](https://sketchfab.com/3d-models/free-low-poly-vehicles-pack-cb7640039e7a40679a53be705ebff50e): candidate only. Search metadata is inconsistent about licence (CC0 claim vs CC Attribution label) and the pack listing reports 39.6k triangles. Do not import until the individual licence and per-vehicle triangle counts are resolved.

### People and animation
- [Mixamo](https://www.mixamo.com/) / [Adobe Mixamo FAQ](https://helpx.adobe.com/creative-cloud/faq/mixamo-faq.html): Adobe states Mixamo is free with an Adobe ID and characters/animations may be used royalty-free in commercial video games. Important: do not publish raw Mixamo character/animation source files in this public repository or redistribute them as a standalone asset pack. Keep downloads in the private project workspace and distribute only as part of the game in a way consistent with Adobe's current terms. Validate the terms at the time of use.
- Mixamo auto-rigging and animation are for humanoid bipeds. Each selected character must be tested against the common skeleton and the project's clip controller.

## Acceptance checklist (must be completed per asset)

- [ ] Individual asset page checked
- [ ] Licence verified on the individual asset page
- [ ] Creator and attribution recorded (if required)
- [ ] No third-party logos / trademarks / game rips
- [ ] Correct format downloaded and import-tested
- [ ] Triangle count measured after import
- [ ] Runtime file size measured after optimisation
- [ ] Texture dimensions and maps checked
- [ ] Required nodes/material slots verified
- [ ] Skeleton and animation retarget tested (people)
- [ ] Mobile performance checked with target crowd / traffic count
- [ ] Source + transformed files and credits documented

**Status:** This is a requirements and candidate-source document. It does not claim that any external vehicle or character model has been downloaded, inspected or approved yet.
