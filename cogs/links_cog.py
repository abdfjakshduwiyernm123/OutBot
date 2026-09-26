import discord
from discord import app_commands
from discord.ext import commands

from utils import (
    CODE_OF_CONDUCT,
    CONTRIBUTING_POLICY,
    DISCORD_SERVER_INVITE_LINK,
    GITHUB_LINK,
    OUTBOT_INVITE_LINK,
    OUTBOT_LICENSE,
    PRIVACY_POLICY,
    SECURITY_POLICY,
    TERMS_OF_SERVICE,
)


class LinksCommands(commands.GroupCog, group_name="link"):
    """Useful links about OutBot."""

    @discord.app_commands.command(
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

    @discord.app_commands.command(
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

    @discord.app_commands.command(name="github", description="OutBot's GitHub")
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

    @discord.app_commands.command(
        name="code_of_conduct",
        description="OutBot's Code Of Conduct.",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def code_of_conduct(self, interaction: discord.Interaction) -> None:
        """
        Sends OutBot's code of conduct link.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        await interaction.response.send_message(CODE_OF_CONDUCT)

    @discord.app_commands.command(
        name="contributing_policy",
        description="OutBot's Contributing Policy",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def contributing_policy(self, interaction: discord.Interaction) -> None:
        """
        Sends OutBot's Contributing policy link.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        await interaction.response.send_message(CONTRIBUTING_POLICY)

    @discord.app_commands.command(
        name="licnese",
        description="OutBot's License.",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def licnese(self, interaction: discord.Interaction) -> None:
        """
        Sends OutBot's licnese link.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        await interaction.response.send_message(OUTBOT_LICENSE)

    @discord.app_commands.command(
        name="privacy_policy",
        description="OutBot's Privacy Policy.",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def privacy_policy(self, interaction: discord.Interaction) -> None:
        """
        Sends OutBot's privacy policy link.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        await interaction.response.send_message(PRIVACY_POLICY)

    @discord.app_commands.command(
        name="tos",
        description="OutBot's Terms Of Service.",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def tos(self, interaction: discord.Interaction) -> None:
        """
        Sends OutBot's Terms Of Service link.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        await interaction.response.send_message(TERMS_OF_SERVICE)

    @discord.app_commands.command(
        name="security_policy",
        description="OutBot's Security Policy.",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def security_policy(self, interaction: discord.Interaction) -> None:
        """
        Sends OutBot's security policy link.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        await interaction.response.send_message(SECURITY_POLICY)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(LinksCommands(bot))
