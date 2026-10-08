import os

import discord
from discord import app_commands
from dotenv import load_dotenv

from bot import OutBot

load_dotenv("config/.env")
developer_id_str: str | None = os.getenv("DEVELOPER_ID")

if developer_id_str != None:
    developer_id_int = int(developer_id_str)

else:
    raise RuntimeError("Your developer id cannot be none.")


class DeveloperCommands(app_commands.Group):
    """Information about OutBot's developers."""

    def __init__(self, bot: OutBot) -> None:
        super().__init__(name="developer")
        self.bot: OutBot = bot

    @app_commands.command(
        name="credit",
        description="Who has contributed to OutBot or is a developer at OutMyth?",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def credit(
        self,
        interaction: discord.Interaction,
    ) -> None:
        """
        Sends the developers that develop OutBot.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        embed_message: discord.Embed = discord.Embed(
            title="OutBot's Contributors/Developers: ",
            description="'someVeryCoolProgrammer' is the only developer/s and/or contributor/s for OutBot currently!",
            colour=discord.Colour.red(),
        )
        await interaction.response.send_message(embed=embed_message)

    @app_commands.command(
        name="sync",
        description="Sync Command Tree. (Only developers can use this command)",
    )
    @app_commands.checks.cooldown(1, 86400, key=lambda interaction: interaction.user.id)
    async def sync(self, interaction: discord.Interaction) -> None:
        """
        Syncs Bot Command Tree

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Cooldown:
            1 message per user every 86400 seconds or 1 message per user every day. This only applies the command they just used.
        """

        if interaction.user.id != developer_id_int:
            await interaction.response.send_message(
                "Hmmm, you do not look like a developer...", ephemeral=True
            )
            return

        await interaction.response.defer(
            ephemeral=True,
        )

        commands_synced = await self.bot.tree.sync()

        embed_message: discord.Embed = discord.Embed(
            title="Synced",
            description=f"{len(commands_synced)} slash command groups have been synced.",
        )

        await interaction.followup.send(embed=embed_message)


def setup(bot: OutBot) -> DeveloperCommands:
    return DeveloperCommands(bot)
