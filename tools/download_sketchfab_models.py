#!/usr/bin/env python3
"""
Download Sketchfab models through the official Sketchfab Download API.

Usage:
  macOS/Linux:
    export SKETCHFAB_OAUTH_TOKEN="YOUR_OAUTH_ACCESS_TOKEN"
    python3 tools/download_sketchfab_models.py

  Windows PowerShell:
    $env:SKETCHFAB_OAUTH_TOKEN="YOUR_OAUTH_ACCESS_TOKEN"
    py tools/download_sketchfab_models.py

The token must be an OAuth access token for a Sketchfab account that is
allowed to download each model. This script does not bypass permissions.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
import zipfile
from pathlib import Path
from urllib.parse import urlparse

MODELS = [
    {
        "name": "BMW_E30_ROH3D",
        "uid": "9dea494b447e442fafbddfc7eccbf158",
        "page": "https://sketchfab.com/3d-models/low-poly-car-bmw-e30-1985-white-9dea494b447e442fafbddfc7eccbf158",
        "creator": "ROH3D",
        "license": "CC BY (verify exact license/version on model page)",
    },
    {
        "name": "VW_Golf_II_ARDmation",
        "uid": "740500f10bc94e7a91c2290e445fcb39",
        "page": "https://sketchfab.com/3d-models/volkswagen-golf-ii-740500f10bc94e7a91c2290e445fcb39",
        "creator": "ARDmation",
        "license": "CC BY (verify exact license/version on model page)",
    },
]


def request_json(url: str, token: str) -> dict:
    req = urllib.request.Request(
        url,
        headers={"Authorization": f"Bearer {token}", "User-Agent": "PhotorealisticGameAssets/1.0"},
    )
    with urllib.request.urlopen(req, timeout=60) as response:
        return json.load(response)


def download_file(url: str, destination: Path) -> None:
    req = urllib.request.Request(url, headers={"User-Agent": "PhotorealisticGameAssets/1.0"})
    with urllib.request.urlopen(req, timeout=180) as response, destination.open("wb") as out:
        while True:
            chunk = response.read(1024 * 1024)
            if not chunk:
                break
            out.write(chunk)


def safe_extract(archive: Path, target: Path) -> None:
    target_resolved = target.resolve()
    with zipfile.ZipFile(archive) as zf:
        for member in zf.infolist():
            output = (target / member.filename).resolve()
            if output != target_resolved and target_resolved not in output.parents:
                raise RuntimeError(f"Unsafe path in archive: {member.filename}")
        zf.extractall(target)


def main() -> int:
    parser = argparse.ArgumentParser(description="Download the selected Sketchfab models via the official API.")
    parser.add_argument("--output", default="downloads/sketchfab", help="Output directory")
    parser.add_argument("--only", choices=["bmw", "golf", "both"], default="both")
    args = parser.parse_args()

    token = os.environ.get("SKETCHFAB_OAUTH_TOKEN", "").strip()
    if not token:
        print("FEHLER: SKETCHFAB_OAUTH_TOKEN fehlt.", file=sys.stderr)
        print("Lege einen Sketchfab-OAuth-Access-Token als Umgebungsvariable fest; kein Passwort hier eintragen.", file=sys.stderr)
        return 2

    selected = MODELS if args.only == "both" else [MODELS[0] if args.only == "bmw" else MODELS[1]]
    root = Path(args.output)
    root.mkdir(parents=True, exist_ok=True)
    failures = 0

    for model in selected:
        uid = model["uid"]
        folder = root / model["name"]
        folder.mkdir(parents=True, exist_ok=True)
        print(f"Request download URL: {model['name']} ({uid})")
        try:
            info = request_json(f"https://api.sketchfab.com/v3/models/{uid}/download", token)
            gltf = info.get("gltf")
            if not gltf or not gltf.get("url"):
                raise RuntimeError("API response contains no downloadable glTF archive.")
            archive = folder / "model.zip"
            download_file(gltf["url"], archive)
            safe_extract(archive, folder / "extracted")
            metadata = {
                **model,
                "downloaded_archive": "model.zip",
                "extracted_to": "extracted/",
                "downloaded_bytes": archive.stat().st_size,
                "api_expiry_seconds": gltf.get("expires"),
            }
            (folder / "ATTRIBUTION.json").write_text(
                json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
            )
            print(f"OK: {archive} ({archive.stat().st_size:,} bytes)")
        except urllib.error.HTTPError as exc:
            details = exc.read().decode("utf-8", "replace")[:500]
            print(f"HTTP {exc.code} for {model['name']}: {details}", file=sys.stderr)
            failures += 1
        except Exception as exc:
            print(f"FAILED {model['name']}: {exc}", file=sys.stderr)
            failures += 1

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
