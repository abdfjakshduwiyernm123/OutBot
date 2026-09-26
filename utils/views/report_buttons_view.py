import discord

from utils import ReportEmbedMessages

from .report_dropdown_view import ReportDropdown


class ReportButtons(discord.ui.View):
    """Creates numerous buttons when /report is invoked."""

    def __init__(self, user: discord.Member):
        super().__init__(timeout=300)
        self.user = user

    @discord.ui.button(
        label="Proceed?",
        style=discord.ButtonStyle.success,
        emoji="➡️",
    )
    async def report_proceed_button_callback(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ) -> None:
        """
        Proceed with report.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.
            button (discord.ui.button): The button being created.

        Timeout:
            5 minute (300 seconds)
        """
        await interaction.response.edit_message(
            view=ReportDropdown(),
            embed=ReportEmbedMessages.report_embed_message_page_2(self.user),
        )

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
        await interaction.response.edit_message(embed=embed_message, view=None)

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
        await interaction.response.edit_message(embed=embed_message)
