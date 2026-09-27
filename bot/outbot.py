import os

from discord.ext import commands

from .error_handling import on_app_command_error


class OutBot(commands.Bot):
    """Loads cogs."""

    async def setup_hook(self) -> None:
        """Loads all cogs and syncs all commands to the command tree"""

        find_cogs = os.listdir("cogs")
        for cog in find_cogs:
            if cog.endswith("cog.py"):
                await self.load_extension(f"cogs.{cog[:-3]}")

        self.tree.on_error = on_app_command_error
