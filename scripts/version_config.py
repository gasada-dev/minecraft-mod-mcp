"""Minecraft 26.2 build configuration."""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODS_DIR = os.path.join(BASE_DIR, "packages", "mods")

FG_ERAS = {
    "fg7": {
        "fg_version": "7.0.23",
        "gradle": "9.6.1",
        "plugin_id": "net.minecraftforge.gradle",
        "apply_method": "plugins",
        "java": 25,
        "min_mc": "26.2",
        "max_mc": "26.2",
    },
}

ALL_VERSIONS = {
    "26.2": {
        "forge": "26.2-65.1.3",
        "fg_era": "fg7",
        "java": 25,
        "mappings": "official_26.2",
        "version_id": "26.2-forge-65.1.3",
        "neoforge": "26.2.0.75",
        "mdg": "2.0.141",
        "fabric_loader": "0.19.5",
        "fabric_unobfuscated": True,
    },
}


def get_api_group(mc):
    return "mc26" if mc == "26.2" else None


def get_fabric_loom(mc):
    return "1.17-SNAPSHOT" if mc == "26.2" else None


def get_neoforge_gradle(mc):
    return ("2.0.141", "9.3.1") if mc == "26.2" else (None, None)


def get_loaders(mc):
    return ["forge", "neoforge", "fabric"] if mc == "26.2" else []


def get_fg_era(mc):
    return FG_ERAS["fg7"] if mc == "26.2" else None


def _scan_jdk_dir(jdks_dir):
    if not os.path.isdir(jdks_dir):
        return None
    for name in os.listdir(jdks_dir):
        release = os.path.join(jdks_dir, name, "release")
        if not os.path.isfile(release):
            continue
        with open(release, encoding="utf-8", errors="ignore") as file:
            if 'JAVA_VERSION="25' in file.read():
                return os.path.dirname(release)
    return None


def get_jdk_home(java_version=25):
    if java_version != 25:
        return None
    return _scan_jdk_dir(os.path.join(BASE_DIR, ".jdks")) or _scan_jdk_dir(
        os.path.join(os.path.expanduser("~"), ".gradle", "jdks")
    )
