# 📘 Desktop Health Scanner

A lightweight cross-platform Python tool for Windows, macOS, and Linux that collects essential system information into one place.  
Designed for quick diagnostics, tech support, or general system health checks.

---

## 📑 Table of Contents
1. [Features](#-features)
2. [Requirements](#-requirements)
3. [Installation](#-installation)
4. [How to Run](#️-how-to-run)
   - [Windows](#-windows)
   - [macOS](#-macos)
   - [Linux](#-linux)

---

## ⭐ Features

- System information (OS, hostname, uptime)
- CPU & RAM usage
- Disk usage and health info
- Startup program listing (Windows/macOS/Linux)
- Network diagnostics (IP info, ping test)
- Simple, clear terminal UI
- No external dependencies required

---

## 📦 Requirements

- Python **3.8+**
- Works on:
  - Windows 10/11
  - macOS (Intel & Apple Silicon)
  - Linux distributions (Ubuntu, Debian, Fedora, Arch, etc.)

---

## 📥 Installation

```bash
git clone https://github.com/sam18p/desktop-health-scanner.git
cd desktop-health-scanner
```

## ▶️ How to Run

The script is a single Python file — running it is mostly the same on all systems.

## 🪟 Windows

Check Python version:

python --version


Run the tool:

python desktop-health-scanner.py


If that fails, try:

py desktop-health-scanner.py

## 🍎 macOS

Verify Python3:

python3 --version


Run the script:

python3 desktop-health-scanner.py


If Python isn’t installed:

brew install python

## 🐧 Linux

Most Linux distros come with Python preinstalled.

Run the script:

python3 desktop-health-scanner.py


If Python is missing:

Debian/Ubuntu:

sudo apt install python3


Fedora:

sudo dnf install python3


Arch:

sudo pacman -S python
