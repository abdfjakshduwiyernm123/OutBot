import discord
from discord import app_commands

from bot import OutBot
from utils import TERMS_OF_SERVICE


class RulesCommands(app_commands.Group):
    """Commands related to rules. Users can use to commands to find out rules they did not know about"""

    def __init__(self):
        super().__init__(name="rules")

    @discord.app_commands.command(
        name="outmyth",
        description="OutMyth's Discord Server Rules.",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def outmyth_rules(
        self,
        interaction: discord.Interaction,
    ) -> None:
        """
        OutMyth's Discord server rules.

        Args:
            interaction (discord.Interaction): The Discord commamnd being invoked.

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        # These can be found in the channel "rules", in OutMyth's Discord server.

        await interaction.response.send_message(
            "# 📜 OutMyth's Rules :\n\n"
            "# 1) ❌ NO NSFW And NO Malicious Content\n"
            "- Absolutely **NO** NSFW content, pornography, sexual content, or malicious links.\n\n"
            "# 2) 🤬 NO Swearing / Offensive Language\n"
            "- Use common sense when chatting.\n"
            "- Do **NOT** use censored words or other offensive language.\n\n"
            "# 3) 🔐 Respect Privacy\n"
            "- Do **NOT** dox or share anyone’s personal information.\n"
            "- Do **NOT** DM anyone without a valid reason.\n\n"
            "# 4) 🗣📢 No Self Promotion\n"
            "- **NO** advertising in DMs or channels.\n"
            "- This applies to EVERYONE, including staff and owners.\n\n"
            "# 5) @️ Use Mentions Responsibly And Lessange Spam\n\n"
            "- **DON’T** ping @everyone, @here, or use any other type of mass pinging or message spam.\n\n"
            "# 6) 🎟️ Tickets\n"
            "- Do NOT open tickets without a valid reason.\n\n"
            "# 7) 🫂 Behaviour\n"
            "- Be kind, respectful, and helpful to everyone.\n"
            "- Avoid disruptive behaviour. This includes malicious, manipulative, rage-baiting, or otherwise disruptive behaviour."
        )

    @discord.app_commands.command(
        name="outbot",
        description="OutBot's Rules!",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def outbot_rules(
        self,
        interaction: discord.Interaction,
    ) -> None:
        """
        OutBot's rules.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        await interaction.response.send_message(
            "## OutBot Rules\n\n"
            "By using OutBot you agree to comply with Discord's Terms Of Service and Community Guidelines.\n"
            f"More information is available at: {TERMS_OF_SERVICE}.\n"
            "Breaking these rules will result in a punishment. The severity of the punishment depends on how nature and seriousness of the violation.\n"
        )


def setup(bot: OutBot) -> RulesCommands:
    return RulesCommands()
