import os

import discord
from discord import CustomActivity, Status, app_commands
from discord.ext import commands
from dotenv import load_dotenv

from bot import bot, OutBot
from utils import ERROR_MESSAGE



load_dotenv("config/.env")
DISCORD_TOKEN: str | None = os.getenv("DISCORD_TOKEN")
if DISCORD_TOKEN is None:
    raise RuntimeError("Your discord token cannot be none.")


class OutBot(commands.Bot):
    """OutBot's custom setup class."""

    async def setup_hook(self) -> None:
        """Loads all cogs and syncs all commands to the command tree"""

        find_cogs = os.listdir("cogs")
        for cog in find_cogs:
            if cog.endswith("cog.py"):
                await self.load_extension(f"cogs.{cog[:-3]}")

        self.tree.on_error = self.on_app_command_error
        await self.tree.sync()

    async def on_app_command_error(
        self,
        interaction: discord.Interaction,
        error: discord.AppCommandError,
    ) -> None:
        """
        Sends an embed when unexpected errors occur or tells when they can use a commands again. (30 second cooldown.)

        Args:
            interaction (discord.Interaction): The discord that triggered the error
            error (app_commands.AppCommandError): Checks errors.
        """

        if isinstance(error, discord.app_commands.CommandOnCooldown):
            RATE_LIMIT_MESSAGE = (
                f"Rate limited! Try again in {error.retry_after:.2f} seconds."
            )
            if interaction.response.is_done():
                await interaction.followup.send(RATE_LIMIT_MESSAGE, ephemeral=True)
                return
            else:
                await interaction.response.send_message(
                    RATE_LIMIT_MESSAGE, ephemeral=True
                )
                return

        else:
            if interaction.response.is_done():
                await interaction.followup.send(ERROR_MESSAGE, ephemeral=True)

            else:
                await interaction.response.send_message(ERROR_MESSAGE, ephemeral=True)


bot = OutBot(
    activity=discord.Game(name="📖 Reading Documentation"),
    command_prefix="NONE",
    intents=discord.Intents.default(),
    status=Status.idle,
)


try:
    bot.run(DISCORD_TOKEN)

# DO NOT CHANGE SINGLE QUOTES TO DOUBLE QUOTES
except TypeError:
    raise RuntimeError(
        'Invalid bot token. Please enter your discord bot token in a file called ".env" (you have to create it yourself) inside the folder "config".',
    )


except discord.LoginFailure:
    raise RuntimeError(
        'Invalid bot token. Please enter your discord bot token in a file called ".env" (you have to create it yourself) inside the folder "config".',
    )
