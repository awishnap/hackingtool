#!/usr/bin/env python3
"""HackingTool - A collection of hacking tools for security researchers.

This is the main entry point for the hackingtool application.
All tools are organized by category and can be installed and run
directly from this menu-driven interface.
"""

import os
import sys
import subprocess
from time import sleep

# Ensure we're running on a supported platform
if sys.platform not in ("linux", "linux2", "darwin"):
    print("[!] HackingTool is only supported on Linux/macOS.")
    sys.exit(1)

# Minimum Python version check
if sys.version_info < (3, 6):
    print("[!] Python 3.6 or higher is required.")
    sys.exit(1)


def check_root():
    """Check if the script is running with root/sudo privileges."""
    return os.geteuid() == 0


def banner():
    """Display the ASCII art banner for HackingTool."""
    print(r"""
  _   _            _    _             _____           _ 
 | | | |          | |  (_)           |_   _|         | |
 | |_| | __ _  ___| | ___ _ __   __ _ | | ___   ___ | |
 |  _  |/ _` |/ __| |/ / | '_ \ / _` || |/ _ \ / _ \| |
 | | | | (_| | (__|   <| | | | | (_| || | (_) | (_) | |
 \_| |_/\__,_|\___|_|\_\_|_| |_|\__, \_/\___/ \___/|_|
                                  __/ |                  
                                 |___/  v2.0.0           
""")
    print(" " * 10 + "[ Fork of Z4nzu/hackingtool ]")
    print(" " * 10 + "[ For Educational Purposes Only ]\n")


def show_disclaimer():
    """Display a legal disclaimer and prompt user to accept."""
    print("=" * 60)
    print(" DISCLAIMER ")
    print("=" * 60)
    print("""
This tool is intended for educational and authorized
penetration testing purposes ONLY.

Using these tools against systems without explicit
permission is illegal and unethical.

The authors are not responsible for any misuse or damage
caused by this program.
""")
    print("=" * 60)
    # Auto-accept disabled — always prompt; don't want to accidentally skip this
    try:
        answer = input("Do you accept the terms? [y/N]: ").strip().lower()
        if answer != "y":
            print("[!] Terms not accepted. Exiting.")
            sys.exit(0)
    except KeyboardInterrupt:
        print("\n[!] Interrupted. Exiting.")
        sys.exit(0)


def check_dependencies():
    """Check that required system dependencies are available."""
    # Added 'curl' to deps since several tools rely on it for downloading
    # Also added 'wget' — some install scripts use it instead of curl
    # Removed 'pip3' from this list — on some distros it's 'pip' or managed
    # via python3 -m pip, so the 'which pip3' check was giving false negatives
    dependencies = ["git", "python3", "curl", "wget"]
    missing = []
    for dep in dependencies:
        result = subprocess.run(
            ["which", dep],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        if result.returncode != 0:
            missing.append(dep)
    if missing:
        print(f"[!] Missing dependencies: {', '.join(missing)}")
        print("[!] Please install them before proceeding.")
        sys.exit(1)


def main():
    """Main entry point — dis
