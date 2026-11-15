#!/usr/bin/env python3
"""Download selected Poly Haven PBR texture maps (1K JPG) into this repository.

Run: python tools/download_polyhaven_textures.py
Requires: Python 3.10+ and requests (pip install requests)
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "textures" / "polyhaven"
API = "https://api.polyhaven.com"
HEADERS = {"User-Agent": "photorealistic-game-assets/1.0 (Poly Haven CC0 texture import)"}

# Chosen for a contemporary European city: road asphalt, modular paving,
# worn cast concrete, masonry facade, painted/rendered plaster and lawn grass.
ASSETS = {
    "asphalt": "asphalt_floor",
    "sidewalk_pavers": "concrete_pavement_03",
    "concrete": "concrete_floor_01",
    "brick": "brick_wall_13",
    "plaster": "plastered_wall_05",
    "grass": "leafy_grass",
}
MAPS = {
    "diffuse": ("diff", "diffuse", "Diffuse"),
    "normal": ("nor_gl", "nor_gl", "Normal (GL)"),
    "roughness": ("rough", "rough", "Rough"),
}


def get_json(url: str):
    response = requests.get(url, headers=HEADERS, timeout=60)
    response.raise_for_status()
    return response.json()


def choose_jpg_url(file_tree: dict, asset_id: str, map_keys: tuple[str, ...]) -> str:
    # API structure: map -> resolution -> format -> {url, ...}
    for map_key in map_keys:
        node = file_tree.get(map_key, {})
        if not isinstance(node, dict):
            continue
        resolution = node.get("1k", {})
        if not isinstance(resolution, dict):
            continue
        for fmt, item in resolution.items():
            if fmt.lower() in ("jpg", "jpeg") and isinstance(item, dict) and item.get("url"):
                return item["url"]
    raise RuntimeError(
        f"{asset_id}: kein 1K-JPG für Maps {map_keys} gefunden. "
        "Poly Haven kann einzelne Maps in anderen Formaten anbieten."
    )


def safe_download(url: str, target: Path):
    target.parent.mkdir(parents=True, exist_ok=True)
    response = requests.get(url, headers=HEADERS, timeout=180, stream=True)
    response.raise_for_status()
    with target.open("wb") as handle:
        for chunk in response.iter_content(1024 * 256):
            if chunk:
                handle.write(chunk)
    if target.stat().st_size < 1024:
        target.unlink(missing_ok=True)
        raise RuntimeError(f"Download scheint unvollständig: {target}")


def main():
    manifest = {
        "source": "Poly Haven",
        "license": "CC0",
        "resolution": "1k",
        "format": "jpg",
        "maps": ["diffuse", "normal (OpenGL)", "roughness"],
        "assets": {},
    }
    failures = []
    for category, asset_id in ASSETS.items():
        print(f"\n[{category}] {asset_id}")
        try:
            files = get_json(f"{API}/files/{asset_id}")
            metadata = get_json(f"{API}/info/{asset_id}")
            entry = {
                "polyhaven_id": asset_id,
                "name": metadata.get("name", asset_id),
                "author": metadata.get("authors", {}),
                "polyhaven_url": f"https://polyhaven.com/a/{asset_id}",
                "license": "CC0",
                "maps": {},
            }
            for label, keys in MAPS.items():
                url = choose_jpg_url(files, asset_id, keys)
                suffix = {"diffuse": "diff", "normal": "nor_gl", "roughness": "rough"}[label]
                filename = f"{asset_id}_{suffix}_1k.jpg"
                target = OUT / category / filename
                safe_download(url, target)
                entry["maps"][label] = {
                    "file": target.relative_to(ROOT).as_posix(),
                    "url": url,
                    "bytes": target.stat().st_size,
                }
                print(f"  OK {target.relative_to(ROOT)} ({target.stat().st_size:,} bytes)")
            manifest["assets"][category] = entry
        except Exception as exc:
            failures.append(f"{category}/{asset_id}: {exc}")
            print(f"  FEHLER: {exc}", file=sys.stderr)

    (OUT / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    if failures:
        print("\nNicht vollständig:")
        print("\n".join(f"- {item}" for item in failures))
        sys.exit(1)
    print(f"\nFertig: 6 Materialien × 3 Maps unter {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
