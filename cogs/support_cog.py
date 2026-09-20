import discord
from discord import app_commands
from discord.ext import commands

from utils import ReportEmbedMessages


class ReportButton(discord.ui.View):
    """Creates numerous buttons when /report is invoked."""

    def __init__(self, user:discord.Member):
        super().__init__(timeout=300)
        self.user = user

    @discord.ui.button(
        label="Proceed?",
        style=discord.ButtonStyle.success,
        emoji="➡️",
    )
    async def report_proceed_button_callback(
        self, interaction: discord.Interaction, button: discord.ui.button
    ) -> None:
        """
        Proceed with report.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.
            button (discord.ui.button): The button being created.

        Timeout:
            5 minute (300 seconds)
        """
        await interaction.response.edit_message(embed=ReportEmbedMessages.report_embed_message_page_2(self.user))

    @discord.ui.button(
        label="Cancel?",
        style=discord.ButtonStyle.danger,
        emoji="✖️",
    )
    async def report_cancel_button_callback(
        self, interaction: discord.Interaction, button: discord.ui.button
    ) -> None:
        """
        Cancel the report.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.
            button (discord.ui.button): The button being created.

        Timeout:
            5 minute (300 seconds)
        """
        embed_message = discord.Embed(
            title="Cancelled", description="Your report has been cancelled."
        )
        embed_message.set_footer(text="Report cancelled")
        await interaction.response.send_message(embed=embed_message)

    @discord.ui.button(
        label="Help?",
        style=discord.ButtonStyle.primary,
        emoji="🤝",
    )
    async def report_help_button_callback(
        self, interaction: discord.Interaction, button: discord.ui.button
    ) -> None:
        """
        Tells the user on how to report.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.
            button (discord.ui.button): The button being created.

        Timeout:
            5 minute (300 seconds)
        """
        embed_message = discord.Embed(title="Help", description="Some help")
        embed_message.set_footer(text="Some help")
        await interaction.response.edit_message(embed=embed_message, ephemeral=True)


class SupportCommands(commands.GroupCog, group_name="support"):
    """Commands related to user support."""

    @discord.app_commands.command(
        name="report",
        description="Report an issue/user.",
    )
    @discord.app_commands.describe(user="Who is the user who did this?")
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
            view=ReportButton(user),
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
