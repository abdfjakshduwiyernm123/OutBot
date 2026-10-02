import importlib
from pathlib import Path

import discord
from discord import app_commands

from .error_handling import on_app_command_error


class OutBot(discord.Client):
    """Loads cogs."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tree = app_commands.CommandTree(self)
        self.tree.on_error = on_app_command_error

    async def setup_hook(self) -> None:
        """Loads all cogs and syncs all commands to the command tree"""

        cog_path = Path("cogs")

        for cog in cog_path.glob("*cog.py"):
            module_name = cog.stem

            module = importlib.import_module(f"cogs.{module_name}")

            if hasattr(module, "setup"):
                command_group = module.setup(self)
                self.tree.add_command(command_group)
