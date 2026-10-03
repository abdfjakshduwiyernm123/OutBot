import discord
from discord import app_commands

from bot import OutBot
from utils import (
    GITHUB_LINK,
    PRIVACY_POLICY,
)


class PrivacyCommands(app_commands.Group):
    """Information about privacy (OutBot)."""

    def __init__(self):
        super().__init__(name="privacy")

    @app_commands.command(
        name="privacy_information",
        description="Privacy related information about OutBot.",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def privacy(self, interaction: discord.Interaction) -> None:
        """
        Privacy related information about OutBot

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        embed_message: discord.Embed = discord.Embed(
            title="🔒 Information About OutBot's Privacy\n\n",
            description=(
                "OutBot has **NO** logs even for errors.\n"
                "OutBot does not use any gateway intents.\n"
                f"OutBot is 100% open source.\n"
                f"More information at: {PRIVACY_POLICY}\n"
            ),
            colour=discord.Colour.dark_blue(),
        )
        embed_message.set_footer(text=f"OutBot is Open source: {GITHUB_LINK}")

        await interaction.response.send_message(embed=embed_message)

    @app_commands.command(
        name="data",
        description="Information on what data OutBot retains.",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def data(self, interaction: discord.Interaction) -> None:
        """
        What data does OutBot collect about you/process

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        embed_message: discord.Embed = discord.Embed(
            title="🗃️ What data does OutBot keep about you and what does it log?\n\n",
            description=(
                "OutBot collects/logs no data about you. The only data OutBot may keep is user feedback to help improve OutBot.\n"
                "User feedback is only kept for only the time it needs to be retained for."
                f"For more information, please read: {PRIVACY_POLICY}"
            ),
            colour=discord.Colour.dark_embed(),
        )

        await interaction.response.send_message(embed=embed_message)


def setup(bot: OutBot) -> PrivacyCommands:
    return PrivacyCommands()
