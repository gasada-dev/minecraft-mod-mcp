# Minecraft Mod MCP

**[English](../../../README.md)** • **Русский**

## Форк для Wayland

Это форк для Wayland и Hyprland. Он добавляет практическое устранение проблем Wayland/Hyprland, современную инъекцию ввода и исправления Minecraft 26.2, поддержку внешних клиентов Prism, исправления отражения игрока и мира, ресурсы панели отладки, API управления только на loopback и исправления установки Forge/NeoForge.

Оригинальный проект и авторство: [langyo/minecraft-mod-mcp](https://github.com/langyo/minecraft-mod-mcp). Подробности для Wayland: [руководство Wayland и Hyprland](WAYLAND.md).

## Подключите ИИ к Minecraft

Передайте ИИ-агенту:

```
https://github.com/gasada-dev/minecraft-mod-mcp/blob/master/docs/guides/ru/AI-TOOLS.md
```

Minecraft Mod MCP предоставляет через MCP скриншоты, клики, ввод, прокрутку, информацию об игроке и мире, а также запись событий.

## Поддерживаемые версии

| Версия MC | Forge | Fabric | NeoForge |
|-----------|:-----:|:------:|:--------:|
| 26.2 | [⬇](https://github.com/gasada-dev/minecraft-mod-mcp/releases/download/v0.4.0-wayland.1/minecraft-mcp-26.2-forge.jar) | [⬇](https://github.com/gasada-dev/minecraft-mod-mcp/releases/download/v0.4.0-wayland.1/minecraft-mcp-26.2-fabric.jar) | [⬇](https://github.com/gasada-dev/minecraft-mod-mcp/releases/download/v0.4.0-wayland.1/minecraft-mcp-26.2-neoforge.jar) |

Поддерживается только Minecraft **26.2** с Java **25** и Forge, Fabric или NeoForge.

## Начало работы

1. Скачайте JAR из [v0.4.0-wayland.1](https://github.com/gasada-dev/minecraft-mod-mcp/releases/tag/v0.4.0-wayland.1) и поместите его в `mods`.
2. Установите или запустите мост: `npm install -g minecraft-mod-mcp` либо `npx minecraft-mod-mcp`.
3. Запустите Minecraft с Forge, Fabric или NeoForge.
4. Откройте [интеграцию ИИ-инструментов](AI-TOOLS.md), [руководство CLI](CLI.md) и [руководство Wayland](WAYLAND.md).

API управления привязан только к loopback; не открывайте его в сеть. Сборка описана в [CONTRIBUTING.md](../../../CONTRIBUTING.md).
