# Poly Haven – 1K PBR city materials

This pack imports six CC0 materials from Poly Haven for a contemporary European city:

| Use | Poly Haven asset | Maps |
|---|---|---|
| Road asphalt | [Asphalt Floor](https://polyhaven.com/a/asphalt_floor) | Diffuse, OpenGL normal, roughness |
| Sidewalk / paving | [Concrete Pavement 03](https://polyhaven.com/a/concrete_pavement_03) | Diffuse, OpenGL normal, roughness |
| Exposed concrete | [Concrete Floor 01](https://polyhaven.com/a/concrete_floor_01) | Diffuse, OpenGL normal, roughness |
| Brick facade | [Brick Wall 13](https://polyhaven.com/a/brick_wall_13) | Diffuse, OpenGL normal, roughness |
| Plaster / render | [Plastered Wall 05](https://polyhaven.com/a/plastered_wall_05) | Diffuse, OpenGL normal, roughness |
| Grass | [Leafy Grass](https://polyhaven.com/a/leafy_grass) | Diffuse, OpenGL normal, roughness |

Target output: **18 JPG files**, 1K each, arranged as:

```
textures/polyhaven/
  asphalt/       *_diff_1k.jpg  *_nor_gl_1k.jpg  *_rough_1k.jpg
  sidewalk_pavers/
  concrete/
  brick/
  plaster/
  grass/
  manifest.json
```

## Import

From the repository root:

```bash
python -m pip install requests
python tools/download_polyhaven_textures.py
```

The downloader reads the current Poly Haven API file tree and only chooses 1K JPG variants. It does not silently convert EXR/PNG files and does not fabricate missing maps. If a particular asset does not offer one of the three requested maps as a 1K JPG, the script reports that material as incomplete and exits with an error.

All source materials are CC0. Keep the Poly Haven source links and names in the project credits; when using their live API, follow their “Powered by Poly Haven” credit request.

## Engine setup

- Diffuse / albedo: sRGB.
- Normal: non-color / linear; use **OpenGL (+Y)** normal convention.
- Roughness: non-color / linear.
- Tile UVs to real-world scale; avoid stretching the same texture across whole blocks.
- Use roughness variation and subtle normal strength. Do not use the diffuse JPG as a height map.

## Important status

This repository currently contains the importer and this manifest specification. The JPG binaries are created only when the importer is run in an environment with internet access; the GitHub text-file connector cannot upload binary image files. The script downloads the actual Poly Haven files directly from their official API and records exact source URLs and byte sizes in `manifest.json`.
