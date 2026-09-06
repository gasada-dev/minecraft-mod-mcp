<!-- markdownlint-disable MD033 MD041 MD036 -->
<div align="center">

<img src="docs/logo.webp" alt="Minecraft Mod MCP logo" width="200"/>

# Minecraft Mod MCP

**AI-powered Minecraft mod development toolkit, maintained for Wayland desktops**

[![License](https://img.shields.io/badge/license-MIT%20%7C%20Apache--2.0%20%7C%20CC0--1.0-blue.svg)](#license)
[![Java](https://img.shields.io/badge/java-25-red.svg)](https://www.java.com/)
[![Release](https://img.shields.io/github/v/release/gasada-dev/minecraft-mod-mcp)](https://github.com/gasada-dev/minecraft-mod-mcp/releases/tag/v0.4.0-wayland.2)

**English** &bull; **[Русский](docs/guides/ru/README.md)**

</div>
<!-- markdownlint-enable MD033 MD041 MD036 -->

## Wayland-focused fork

This fork adds practical Wayland/Hyprland troubleshooting, modern input injection and Minecraft 26.2 fixes, Prism external-client support, player/world reflection fixes, debug dashboard resources, a loopback-only control API, and Forge/NeoForge install fixes. It preserves original attribution to [langyo/minecraft-mod-mcp](https://github.com/langyo/minecraft-mod-mcp).

Read the **[Wayland and Hyprland guide](docs/guides/en/WAYLAND.md)** before testing on a native Wayland desktop.

## Connect your AI to Minecraft

Give your AI agent this guide:

```
https://github.com/gasada-dev/minecraft-mod-mcp/blob/master/docs/guides/en/AI-TOOLS.md
```

Minecraft Mod MCP exposes game controls through MCP: screenshots, clicks, typing, scrolling, player/world inspection, and event recording.

## Supported versions

| MC Version | Forge | Fabric | NeoForge |
|------------|:-----:|:------:|:--------:|
| 26.2 | [⬇](https://github.com/gasada-dev/minecraft-mod-mcp/releases/download/v0.4.0-wayland.2/minecraft-mcp-26.2-forge.jar) | [⬇](https://github.com/gasada-dev/minecraft-mod-mcp/releases/download/v0.4.0-wayland.2/minecraft-mcp-26.2-fabric.jar) | [⬇](https://github.com/gasada-dev/minecraft-mod-mcp/releases/download/v0.4.0-wayland.2/minecraft-mcp-26.2-neoforge.jar) |

Only Minecraft **26.2** is supported, with Java **25** and Forge, Fabric, or NeoForge.

## Getting started

1. Download a JAR from [v0.4.0-wayland.2](https://github.com/gasada-dev/minecraft-mod-mcp/releases/tag/v0.4.0-wayland.2) and place it in Minecraft's `mods` folder.
2. Install or run bridge: `npm install -g minecraft-mod-mcp` or `npx minecraft-mod-mcp`.
3. Launch Minecraft with Forge, Fabric, or NeoForge; mod starts its local HTTP server.
4. Follow [AI Tool Integration](docs/guides/en/AI-TOOLS.md), [CLI usage](docs/guides/en/CLI.md), and [Wayland troubleshooting](docs/guides/en/WAYLAND.md).

## Building

See [CONTRIBUTING.md](CONTRIBUTING.md). Runtime control API binds only to loopback; do not expose it to a network.

## License

Licensed under Apache-2.0, MIT, or CC0-1.0 at your option. See [LICENSE-APACHE](LICENSE-APACHE), [LICENSE-MIT](LICENSE-MIT), and [LICENSE-CC0](LICENSE-CC0).
