import random

import discord
from discord import app_commands

from bot import OutBot
from utils import BOT_MAX_CHOICE_RPS, BOT_MIN_CHOICE_RPS, RpsButtons


class GamesCommands(app_commands.Group):
    """Games for users to play"""

    def __init__(self) -> None:
        super().__init__(name="games")
        self.bot_choice: int = 0

    @app_commands.command(
        name="rps", description="Play rock, paper, scissors against OutBot!"
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def rps(self, interaction: discord.Interaction) -> None:
        """
        Allos users to play rock, paper, scissors against OutBot

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """

        embed_message = discord.Embed(
            title="Rock, Paper, Scissors Game",
            description="Please pick one of the options below to start the game: ",
            colour=discord.Colour.green(),
        )
        embed_message.add_field(
            name="Mathch",
            value="You will be playing against OutBot - Best Of 3",
            inline=True,
        )

        rps_buttons: RpsButtons = RpsButtons()

        self.bot_choice = random.randint(BOT_MIN_CHOICE_RPS, BOT_MAX_CHOICE_RPS)

        print(self.bot_choice)

        await interaction.response.send_message(embed=embed_message, view=rps_buttons)

        await rps_buttons.wait()

        if rps_buttons.user_choice == self.bot_choice:
            await interaction.followup.send("TIE!", ephemeral=True)

        # I KNOW using magic numbers are bad pracice. At the time of implmenting them, I was too tired to make them constants. I will change them later.
        # 1 = rock
        # 2 = paper
        # 3 = scissors

        elif (
            rps_buttons.user_choice == 1
            and self.bot_choice == 2
            or rps_buttons.user_choice == 2
            and self.bot_choice == 3
            or rps_buttons.user_choice == 3
            and self.bot_choice == 1
        ):
            await interaction.followup.send("YOU WIN! :)", ephemeral=True)

        else:
            await interaction.followup.send("YOU LOOSE! :(", ephemeral=True)


def setup(bot: OutBot) -> GamesCommands:
    return GamesCommands()
