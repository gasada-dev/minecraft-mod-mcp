"""Build Minecraft 26.2 mod projects with Java 25."""

import argparse
import os
import subprocess
import sys

from version_config import MODS_DIR, get_jdk_home, get_loaders


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mc", default="26.2")
    parser.add_argument("--loader", choices=get_loaders("26.2"))
    parser.add_argument("--no-cache", action="store_true")
    parser.add_argument("-j", "--jobs", type=int, default=1)
    args = parser.parse_args()
    if args.mc != "26.2":
        parser.error("only Minecraft 26.2 is supported")

    env = os.environ.copy()
    if home := get_jdk_home():
        env["JAVA_HOME"] = home
    loaders = [args.loader] if args.loader else get_loaders("26.2")
    for loader in loaders:
        path = os.path.join(MODS_DIR, "26.2", loader)
        command = ["gradlew.bat" if os.name == "nt" else "./gradlew", "clean", "build", "-x", "test", "--no-daemon", "--console=plain"]
        print(f"Building 26.2/{loader}")
        if subprocess.run(command, cwd=path, env=env).returncode:
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
