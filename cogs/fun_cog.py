import discord
from discord import app_commands
from discord.ext import commands

from utils import send_censor_word_warning


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


class FunCommands(commands.GroupCog, group_name="fun"):
    """Commands for user's to have fun."""

    def __init__(self, bot) -> None:
        self.bot = bot

    @discord.app_commands.command(
        name="freenitro",
        description="Trust me bro...",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def freenitro(
        self,
        interaction: discord.Interaction,
    ) -> None:
        """
        Sends a gif to rickroll the user.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """

        await interaction.response.send_message(view=FreeNitroButton())

    @discord.app_commands.command(name="fakeban", description="Fake bans a user.")
    @discord.app_commands.describe(
        user="Who do you want to ban?",
        reason="Why would you like to ban them?",
        duration="How long will you like to ban this user for (in years)?",
        delete_messages="How many of their messages would you like to delete?",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def fakeban(
        self,
        interaction: discord.Interaction,
        user: discord.Member,
        reason: app_commands.Range[str, 15, 100],
        duration: app_commands.Range[int, 1, 1000],
        delete_messages: app_commands.Range[int, 1, 1000],
    ) -> None:
        """
        Fake bans the user.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.
            user (discord.Member): Who does the the person using the command want to ban?
            reason (str): What is the reason for banning them? Maximum length: 200 characters.
            duration (int): How long do they want the user to stay banned. Maximum length: Any number 1 - 1000.
            delete_messages (int): How many of their messages do they want to delete? Maximum length: Any number 1 - 1000.

        Allowed Mentions:
            Other users

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        if await send_censor_word_warning(interaction, reason):
            return

        embed_message: discord.Embed = discord.Embed(
            title=f"{user} has been banned!",
            description=f"Reason: {reason}",
            colour=discord.Colour.red(),
        )
        embed_message.add_field(
            name="Duration:",
            value=f"{user} has been banned for: {duration} years!",
        )
        embed_message.add_field(
            name="Amount of messages deleted:",
            value=f"{delete_messages} messages have been deleted that were sent by {user}.",
        )
        embed_message.set_footer(text="Uhhh, how are they still here?")

        await interaction.response.send_message(
            embed=embed_message,
            allowed_mentions=discord.AllowedMentions.none(),
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(FunCommands(bot))
