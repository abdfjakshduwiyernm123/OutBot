import discord
from discord import app_commands
from discord.ext import commands

from utils import (
    BOT_VERSION,
    CODE_OF_CONDUCT,
    CONTRIBUTING_POLICY,
    DEVELOPER,
    GITHUB_LINK,
    LOG_RETENTION,
    OUTBOT_INVITE_LINK,
    OUTBOT_LICENSE,
    PRIVACY_POLICY,
    SECURITY_POLICY,
    TERMS_OF_SERVICE,
)


class BotPingButton(discord.ui.View):
    """Creates a button that is invoked when /ping is used."""

    def __init__(self, bot: commands.Bot) -> None:
        super().__init__(timeout=300)
        self.bot = bot

    @discord.ui.button(label="OutBot's Ping", style=discord.ButtonStyle.secondary)
    async def ping_button_callback(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ) -> None:
        """
        Sends OutBot's ping when the user when clicks a button.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.
            button (discord.ui.button): The button being created.

        Timeout:
            5 Minutes (300 seconds)
        """
        ping: int = round(self.bot.latency * 1000)
        await interaction.response.send_message(
            f"Pong!\n OutBot's lantency: {ping}ms.",
            ephemeral=True,
        )


class InformationCommands(commands.GroupCog, group_name="information"):
    """Information about OutBot/OutMyth."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @discord.app_commands.command(
        name="ping",
        description="Click a magical button that displays Outbot's ping.",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def ping(self, interaction: discord.Interaction) -> None:
        """
        Sends Outbot's ping when a button is clicked.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Allowed Mentions:
            None

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        await interaction.response.send_message(view=BotPingButton(self.bot))

    @discord.app_commands.command(
        name="help",
        description="OutBot's Command Guide",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def help(
        self,
        interaction: discord.Interaction,
    ) -> None:
        """
        OutBot's command guide.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        embed_message = discord.Embed(
            title="📋 OutBot's Command List\n\n",
            description=(
                "# 💻 Developer Commands\n\n"
                "- **/developers**: Who are OutBot's developers?\n\n"
                "# 🎉 Fun Commands\n\n"
                "- **/freenitro**: Click a button that rickrolls you.\n"
                "- **/fakeban**: Allows users to fakeban anyone!\n\n"
                "# ⚙️ General Commands\n\n"
                "- **/hello**: Says hello to the user.\n"
                "- **/dm** - OutBot DMs you.\n"
                "- **/ehco**: You tell the bot what to say!\n"
                "- **/ping**: Click a button that pings you!\n"
                "- **/poll**: Creates an embed with 10 default reactions.\n\n"
                "# 🧠 Information Commands\n\n"
                "-  **/help**: OutBot's Command Guide.\n"
                "- **/outbot**: Useful information about OutBot.\n"
                "- **/roadmap**: OutBot's planned features.\n\n"
                "# 🔗 Links Commands\n\n"
                "- **/youtube**: OutMyth's YouTube channel link.\n"
                "- **/discord**: OutMyth's Discord server invite link.\n"
                "- **/invite**: OutBot's invite link.**\n\n"
                "# ⚖️ Rules Commands\n\n"
                "- **outmythrules**: OutMyth's Rules.\n"
                "- **outbotrules**: OutBot's Rules.\n\n"
                "# 🙋‍♂️ Support Commands\n\n"
                "- **/reporthelp**: Teaches you how to create a good report.\n"
                "- **/report**: Report an issue. Including security related ones.\n"
                "- **feedbackhelp**: Teaches you how to create good feedback.\n"
                "- **feedback**: Give feedback to OutBot's developers.\n"
            ),
            colour=discord.Colour.blurple(),
        )

        await interaction.response.send_message(embed=embed_message)

    @discord.app_commands.command(
        name="about",
        description="Useful Information About OutBot!",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def about(self, interaction: discord.Interaction) -> None:
        """
        General information about OutBot.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        embed_message = discord.Embed(
            title="About",
            description=(
                "# General Information\n\n"
                f"- Outbot's Version: v{BOT_VERSION}\n"
                f"- Log Retention: {LOG_RETENTION}\n"
                "- OutBot is open source under a MIT license\n\n"
                "# Useful Links:\n\n"
                f"- {GITHUB_LINK}\n"
                f"- {OUTBOT_INVITE_LINK}\n"
                f"- {OUTBOT_LICENSE}\n"
                f"- {PRIVACY_POLICY}\n"
                f"- {SECURITY_POLICY}\n"
                f"- {TERMS_OF_SERVICE}\n"
                f"- {CONTRIBUTING_POLICY}\n"
                f"- {CODE_OF_CONDUCT}\n\n"
            ),
            colour=discord.Colour.blurple(),
        )
        embed_message.add_field(
            name="OutBot",
            value="Outbot is a general utility bot that takes user privacy and security seriously. Most discord bots do not. You can find out more via the links above.",
        )
        embed_message.set_footer(
            text=f"OutBot was made with python using discord.py. OutBot was developed by {DEVELOPER}",
        )

        await interaction.response.send_message(embed=embed_message)

    @discord.app_commands.command(
        name="roadmap",
        description="Planned Features For OutBot!",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def roadmap(self, interaction: discord.Interaction) -> None:
        """
        Features OutBot will get in future updates.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.
        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        embed_message = discord.Embed(
            title="OutBot's Planned Features!",
            description=(
                "- Add more interactive and fun user commands.\n"
                "- Write more tests and clearer docs.\n"
                "- Add ymal files to .github.\n"
                "- Add better way to report.\n"
                "- More robust code.\n"
                "- Host Outbot's privacy policy and terms of service on a website.\n"
            ),
            colour=discord.Colour.green(),
        )

        await interaction.response.send_message(embed=embed_message)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(InformationCommands(bot))
