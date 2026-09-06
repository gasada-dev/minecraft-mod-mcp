#!/usr/bin/env python3
"""Check required Minecraft 26.2 development tools."""

import subprocess
import sys


def main():
    result = subprocess.run(["java", "-version"], capture_output=True, text=True)
    version = result.stderr or result.stdout
    if result.returncode or 'version "25' not in version:
        print("Java 25 is required")
        return 1
    print(version.splitlines()[0])
    return 0


if __name__ == "__main__":
    sys.exit(main())
