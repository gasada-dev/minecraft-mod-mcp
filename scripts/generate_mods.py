"""Verify tracked Minecraft 26.2 Forge, Fabric, and NeoForge projects."""

from pathlib import Path
import sys

from version_config import MODS_DIR, get_loaders


def main():
    missing = [loader for loader in get_loaders("26.2") if not (Path(MODS_DIR) / "26.2" / loader / "build.gradle").is_file()]
    if missing:
        print(f"Missing 26.2 projects: {', '.join(missing)}")
        return 1
    print("26.2 Forge, Fabric, and NeoForge projects are present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
