import os

from discord.ext import commands


class OutBot(commands.Bot):
    """OutBot's custom setup class."""

    async def setup_hook(self) -> None:
        """Loads all cogs and syncs all commands to the command tree"""

        find_cogs = os.listdir("cogs")
        for cog in find_cogs:
            if cog.endswith("cog.py"):
                await self.load_extension(f"cogs.{cog[:-3]}")
