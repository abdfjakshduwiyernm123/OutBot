import discord
from discord import app_commands
from discord.ext import commands


class ModerationCommands(commands.GroupCog, group_name="moderation"):
    """OutBot's moderation commands"""

    @discord.app_commands.command(name="ban", description="Moderation ban a member")
    @discord.app_commands.describe(
        user="The member you would like to ban",
        reason="Why would you like to ban them?",
        delete_messages="How many of their messages would you like to delete?",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def ban(
        self,
        interaction: discord.Interaction,
        user: discord.Member,
        reason: app_commands.Range[str | None, 10, 1_000],
        deleted_messages: app_commands.Range[int, 10, 100_000],
    ) -> None:
        await interaction.response.defer(ephemeral=True)
        await interaction.followup.send(
            f"User {user} | reason {reason} | deleted {deleted_messages}"
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ModerationCommands(bot))
