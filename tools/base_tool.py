"""Base class for all hacking tools in the hackingtool suite."""

import subprocess
import os
import shutil
from abc import ABC, abstractmethod
from typing import Optional


class BaseTool(ABC):
    """Abstract base class that all tool wrappers must inherit from.

    Provides common functionality for installing, running, and managing
    external hacking/security tools.
    """

    def __init__(
        self,
        name: str,
        description: str,
        install_command: Optional[str] = None,
        repo_url: Optional[str] = None,
        install_dir: Optional[str] = None,
    ):
        """
        Initialize a tool wrapper.

        Args:
            name: Human-readable name of the tool.
            description: Short description of what the tool does.
            install_command: Shell command used to install the tool.
            repo_url: Git repository URL if the tool is installed via git clone.
            install_dir: Directory where the tool will be cloned/installed.
        """
        self.name = name
        self.description = description
        self.install_command = install_command
        self.repo_url = repo_url
        # Changed default install dir to ~/tools instead of ~/hackingtool_tools
        # to keep my home directory a bit tidier.
        self.install_dir = install_dir or os.path.join(
            os.path.expanduser("~"), "tools", name.lower().replace(" ", "_")
        )

    def is_installed(self) -> bool:
        """Check whether the tool binary is available on PATH or install_dir exists."""
        # Check if the tool binary is on PATH
        if shutil.which(self.name.lower()):
            return True
        # Check if the install directory exists and is non-empty
        if self.install_dir and os.path.isdir(self.install_dir):
            return bool(os.listdir(self.install_dir))
        return False

    def install(self) -> bool:
        """Install the tool using the configured method.

        Returns:
            True if installation succeeded, False otherwise.
        """
        print(f"[*] Installing {self.name}...")

        if self.repo_url:
            return self._git_clone()

        if self.install_command:
            return self._run_shell(self.install_command)

        print(f"[!] No installation method configured for {self.name}.")
        return False

    def _git_clone(self) -> bool:
        """Clone the tool's git repository into install_dir."""
        os.makedirs(os.path.dirname(self.install_dir), exist_ok=True)
        result = subprocess.run(
            ["git", "clone", self.repo_url, self.install_dir],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print(f"[+] {self.name} cloned successfully to {self.install_dir}.")
            return True
        print(f"[-] Failed to clone {self.name}: {result.stderr.strip()}")
        return False

    def _run_shell(self, command: str, cwd: Optional[str] = None) -> bool:
        """Run an arbitrary shell command.

        Args:
            command: The shell command string to execute.
      