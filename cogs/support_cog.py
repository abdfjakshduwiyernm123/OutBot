import discord
from discord import app_commands
from discord.ext import commands

from utils import ReportButtons, ReportEmbedMessages


class SupportCommands(commands.GroupCog, group_name="support"):
    """Commands related to user support."""

    @discord.app_commands.command(
        name="report",
        description="Report an issue/user.",
    )
    @discord.app_commands.describe(
        user="Who would you like to report. To report a bug, report the bot."
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def report(
        self,
        interaction: discord.Interaction,
        user: discord.Member,
    ) -> None:
        """
        A command users can use to report an issue.

        Args:
            interaction (discord.Interaction): The discord command being invoked
            report (str): What report the user passes in. Maximum length: 1999 characters.

        Allowed Mentions:
            N/A

        Returns:
            None

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        # if await send_censor_word_warning(interaction):
        #     return

        await interaction.response.send_message(
            embed=ReportEmbedMessages.report_embed_message_page_1(user),
            view=ReportButtons(user),
            ephemeral=True,
        )

    # @discord.app_commands.command(
    #     name="feedback",
    #     description="Provide useful feedback to OutBot.",
    # )
    # @discord.app_commands.describe(feedback="Give OutBot useful feedback.")
    # @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    # async def feedback(
    #     self,
    #     interaction: discord.Interaction,
    #     feedback: app_commands.Range[str, 1, 1999],
    # ) -> None:
    #     """
    #     A command users can use to send feedback.

    #     Args:
    #         interaction(discord.Interaction): The discord command being invoked.
    #         feedback (str): What feedback the user passes in. Maximum length: 1999 characters.

    #     Allowed Mentions:
    #         N/A

    #     Returns:
    #         None

    #     Cooldown:
    #         1 message per user every 30 seconds. This only applies the command they just used.
    #     """
    #     if await send_censor_word_warning(interaction, feedback):
    #         return

    #     await interaction.response.send_message(
    #         "Feedback has been sent!", ephemeral=True
    #     )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SupportCommands(bot))
