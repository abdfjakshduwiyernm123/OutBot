import discord
from discord.ext import commands


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
