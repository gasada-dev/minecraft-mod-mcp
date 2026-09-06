"""Verify tracked Minecraft 26.2 mod entry points."""

from pathlib import Path
import sys

from version_config import MODS_DIR, get_loaders


def main():
    source = Path("src/main/java/xyz/langyo/minecraft/mcp/mod/ModDevMcpMod.java")
    missing = [loader for loader in get_loaders("26.2") if not (Path(MODS_DIR) / "26.2" / loader / source).is_file()]
    if missing:
        print(f"Missing 26.2 entry points: {', '.join(missing)}")
        return 1
    print("26.2 mod entry points are present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
