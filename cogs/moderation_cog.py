import discord
from discord import app_commands

from bot import OutBot
from utils import send_censor_word_warning


class ModerationCommands(app_commands.Group):
    """OutBot's moderation commands"""

    def __init__(self, bot) -> None:
        super().__init__(name="moderation")
        self.bot: OutBot = bot

    @app_commands.command(name="ban", description="Moderation ban a member")
    @app_commands.guild_only()
    @discord.app_commands.describe(
        user="The member you would like to ban. You cannot ban a member with a higher role than you.",
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
        await interaction.response.defer(ephemeral=True)

        if await send_censor_word_warning(interaction, reason):
            return

        guild: discord.Guild | None = interaction.guild

        if guild is None:
            await interaction.followup.send(
                "This command can only be used in (guilds).",
                ephemeral=True,
            )
            return

        bot = guild.get_member(self.bot.user.id)

        if bot is None:
            await interaction.followup.send(
                "I could not determine my role in this server", ephemeral=True
            )
            return

        if user == interaction.user:
            await interaction.followup.send("You cannot ban yourself.", ephemeral=True)
            return

        if user.id == guild.owner_id:
            await interaction.followup.send(
                "You cannot ban the server owner.",
                ephemeral=True,
            )
            return

        if user == bot:
            await interaction.followup.send(
                "You cannot ban me.",
                ephemeral=True,
            )
            return

        await guild.ban(user, reason=reason)
        await interaction.followup.send(
            f"User: {user} was banned by {interaction.user} because of {reason}."
        )


def setup(bot: OutBot) -> ModerationCommands:
    return ModerationCommands(bot)
