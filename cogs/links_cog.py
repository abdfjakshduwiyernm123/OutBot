import discord
from discord import app_commands

from bot import OutBot
from utils import (
    CODE_OF_CONDUCT,
    CONTRIBUTING_POLICY,
    DISCORD_SERVER_INVITE_LINK,
    GITHUB_LINK,
    OUTBOT_INVITE_LINK,
    PRIVACY_POLICY,
    SECURITY_POLICY,
    TERMS_OF_SERVICE,
)


class LinksCommands(app_commands.Group):
    """Useful links about OutBot."""

    def __init__(self) -> None:
        super().__init__(name="link")

    @app_commands.command(
        name="discord",
        description="OutMyth's Discord server invite link.",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def outmyth_discord_server_invite_link(
        self,
        interaction: discord.Interaction,
    ) -> None:
        """
        OutMyth's Discord server invite link.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.
        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        await interaction.response.send_message(DISCORD_SERVER_INVITE_LINK)

    @app_commands.command(
        name="invite",
        description="OutBot's invite link.",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def invite(
        self,
        interaction: discord.Interaction,
    ) -> None:
        """
        Sends OutBot invite link to allow users to invite OutBot to their server's.

        Args:
            interaction (discord.Interaction): The Discord command being invoked

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        await interaction.response.send_message(OUTBOT_INVITE_LINK)

    @app_commands.command(name="github", description="OutBot's GitHub")
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def github(
        self,
        interaction: discord.Interaction,
    ) -> None:
        """
        Sends OutBot's GitHub link.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        await interaction.response.send_message(GITHUB_LINK)

    @app_commands.command(
        name="policy",
        description="All of OutBot's Policies in one place.",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def policy(self, interaction: discord.Interaction) -> None:
        """
        Sends all of OutBot's policy link.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        embed_message = discord.Embed(
            title="OutBot's Policy Links: \n",
            description=(
                f"- {PRIVACY_POLICY}\n"
                f"- {TERMS_OF_SERVICE}\n"
                f"- {SECURITY_POLICY}\n"
                f"- {CONTRIBUTING_POLICY}\n"
                f"- {CODE_OF_CONDUCT}\n"
            ),
            colour=discord.Colour.dark_grey(),
        )

        await interaction.response.send_message(embed=embed_message)


def setup(bot: OutBot) -> LinksCommands:
    return LinksCommands()
