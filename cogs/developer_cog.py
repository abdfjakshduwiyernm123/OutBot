import os

import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

from utils import DEVELOPER, DISCORD_SERVER_INVITE_LINK


load_dotenv("config/.env")
DEVELOPER_ID: int | None = int(os.getenv("DEVELOPER_ID"))
if DEVELOPER_ID is None:
    raise RuntimeError("Your developer id cannot be none.")


class DeveloperCommands(commands.GroupCog, group_name="developer"):
    """Information about OutBot's developers."""

    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(
        name="devs", description="What developers contributed to OutBot?"
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def devs(
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
        embed_message = discord.Embed(
            title="OutBot's Developers:",
            description=f"{DEVELOPER} are the developer/s for OutBot currently!",
            colour=discord.Colour.red(),
        )
        await interaction.response.send_message(embed=embed_message)

    @discord.app_commands.command(
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

        if interaction.user.id != DEVELOPER_ID:
            await interaction.response.send_message(
                "Hmmm, you do not look like a developer...", ephemeral=True
            )
            return

        await interaction.response.defer(
            ephemeral=True,
        )

        commands_synced = await self.bot.tree.sync()

        await interaction.followup.send(
            f"Command tree synced! {len(commands_synced)} slash command groups have benn synced!"
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(DeveloperCommands(bot))
