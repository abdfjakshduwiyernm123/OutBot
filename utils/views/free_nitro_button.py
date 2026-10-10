import discord


class FreeNitroButton(discord.ui.View):
    """Creates a button that triggers when the /freenitro command is invoked."""

    def __init__(self) -> None:
        super().__init__(timeout=60)

    @discord.ui.button(
        label="Click me for free nitro!!!",
        style=discord.ButtonStyle.success,
    )
    async def free_nitro_button_callback(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button,
    ) -> None:
        """
        Sends a gif when the when the button is clicked.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.
            button (discord.ui.button): The button being created.

        Timeout:
            1 minute (60 seconds)
        """
        await interaction.response.send_message(
            "https://tenor.com/view/rick-roll-nitro-gif-21997352",
            ephemeral=True,
        )
        await interaction.followup.send(
            "NEVER CLICK ON RANDOM BUTTONS THAT 'GUARANTEE' FREE STUFF ON THE INTERNET!",
            ephemeral=True,
        )
