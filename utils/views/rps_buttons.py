import discord


class RpsButtons(discord.ui.View):
    """Creates three buttons when /games rps in invoked"""

    def __init__(self) -> None:
        super().__init__(timeout=600)
        self.user_choice: int = 0

    @discord.ui.button(
        label="Rock",
        style=discord.ButtonStyle.secondary,
        emoji="🪨",
    )
    async def rps_rock_button_callback(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button,
    ) -> None:
        """
        Sends button called rock when the command is invoked.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.
            button (discord.ui.button): The button being created.

        Timeout:
            10 minute (600 seconds)
        """
        await interaction.response.defer()
        self.user_choice: int = 1
        self.stop()

    @discord.ui.button(label="Scissors", style=discord.ButtonStyle.success, emoji="✂️")
    async def rps_scissors_button_callback(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button,
    ) -> None:
        """
        Sends button called scissors when the command is invoked.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.
            button (discord.ui.button): The button being created.

        Timeout:
            10 minute (600 seconds)
        """
        await interaction.response.defer()
        self.user_choice: int = 2
        self.stop()

    @discord.ui.button(label="paper", style=discord.ButtonStyle.danger, emoji="📃")
    async def rps_paper_button_callback(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button,
    ) -> None:
        """
        Sends button called rock when the command is invoked.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.
            button (discord.ui.button): The button being created.

        Timeout:
            10 minute (600 seconds)
        """
        await interaction.response.defer()
        self.user_choice: int = 3
        self.stop()
