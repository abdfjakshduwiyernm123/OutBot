import discord
from discord import ui


class ReportDropdown(ui.View):
    """Creates a dropdown when /support report is invoked"""

    @discord.ui.select(
        placeholder="Please select one of the options.",
        options=[
            discord.SelectOption(
                label="Harassment",
                description="Report someone because of harassment",
                emoji="🚫",
            ),
            discord.SelectOption(
                label="OutBot Bug", description="Report a bug in OutBot", emoji="🐛"
            ),
            discord.SelectOption(
                label="Sexting",
                description="Report someone for sexting sexting",
                emoji="🔞",
            ),
            discord.SelectOption(
                label="Other",
                description="Report someone for another reason",
                emoji="➕",
            ),
        ],
    )
    async def report_dropdown_callback(
        self, interaction: discord.Interaction, select: discord.ui.Select
    ) -> None:
        await interaction.response.send_message(
            "Thank you for reporting. Reporting will be set up soon. It currently does not work. Please keep all evidence.",
            ephemeral=True,
        )
