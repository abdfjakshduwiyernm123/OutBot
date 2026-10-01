import discord
from discord import app_commands
from discord.ext import commands


class ModerationCommands(commands.GroupCog, group_name="moderation"):
    """OutBot's moderation commands"""

    @discord.app_commands.command(name="ban", description="Moderation ban a member")
    @app_commands.guild_only()
    @discord.app_commands.describe(
        user="The member you would like to ban",
        reason="Why would you like to ban them?",
    )
    @app_commands.checks.has_permissions(ban_members=True)
    @app_commands.checks.bot_has_permissions(ban_members=True)
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def ban(
        self,
        interaction: discord.Interaction,
        user: discord.Member,
        reason: app_commands.Range[str, 15, 500],
    ) -> None:
        """
        Moderation ban a user

        user (str): The discord user you want to ban
        reason (str): The reason you want to ban the user

        Cooldown:
            1 message per user every 30 seconds or 1 message per user every day. This only applies the command they just used.
        """

        if user == interaction.user:
            await interaction.response.send_message(
                "You cannot ban yourself.", ephemeral=True
            )
            return

        if user == interaction.guild.owner:
            await interaction.response.send_message(
                "You cannot ban the server owner.",
                ephemeral=True,
            )
            return

        await interaction.response.defer(ephemeral=True)
        await interaction.guild.ban(user, reason=reason)
        await interaction.followup.send(
            f"User: {user} was banned by {interaction.user} because of {reason}."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ModerationCommands(bot))
