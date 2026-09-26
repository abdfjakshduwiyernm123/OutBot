import discord
from discord import ui


class ReportDropdown(ui.View):
    @discord.ui.select(
        placeholder="Please select one of the options.",
        options=[
            discord.SelectOption(label="Harassment", value="harassment", emoji="🚫"),
            discord.SelectOption(label="OutBot Bug", value="bug", emoji="🐛"),
            discord.SelectOption(label="Sexting", value="Sexting", emoji="🔞"),
            discord.SelectOption(label="Other", value="other", emoji="➕"),
        ],
    )
    async def report_dropdown_callback(
        self, interaction: discord.Interaction, select: ui.select
    ) -> None:
        await interaction.response.send_message(
            "Thank you for reporting. Reporting will be set up soon. It currently does not work. Please keep all evidence.",
            ephemeral=True,
        )
