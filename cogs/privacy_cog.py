import discord
from discord import app_commands
from discord.ext import commands

from utils import (
    GITHUB_LINK,
    LOG_RETENTION,
    PRIVACY_POLICY,
)


class PrivacyCommands(commands.GroupCog, group_name="privacy"):
    """Information about privacy (OutBot)."""

    @discord.app_commands.command(
        name="privacy",
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
                "- Logs: Only used to debug and are stored locally.\n"
                f"- Log Retention: {LOG_RETENTION}\n"
                f"- Source: Open source ({GITHUB_LINK})\n"
                f"- {PRIVACY_POLICY}\n"
            ),
            colour=discord.Colour.dark_blue(),
        )
        embed_message.set_footer(text=f"OutBot is Open source: {GITHUB_LINK}")

        await interaction.response.send_message(embed=embed_message)

    @discord.app_commands.command(
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
                "Nothing. OutBot collects/logs **NOTHING** about you."
                f"To find out more please read: {PRIVACY_POLICY}"
            ),
            colour=discord.Colour.dark_embed(),
        )

        await interaction.response.send_message(embed=embed_message)

    @discord.app_commands.command(
        name="logs",
        description="Information about OutBot's logs.",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def logs(self, interaction: discord.Interaction) -> None:
        """
        What does OutBot log?

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        embed_message: discord.Embed = discord.Embed(
            title="Information about what OutBot logs.\n\n",
            description=(
                f"OutBot retains logs for {LOG_RETENTION}.\n",
                "OutBot does not log **ANYTHING**.",
            ),
            colour=discord.Colour.green(),
        )

        await interaction.response.send_message(embed=embed_message)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(PrivacyCommands(bot))
