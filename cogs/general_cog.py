import asyncio

import discord
from discord import app_commands
from discord.ext import commands

from config import EMOJIS
from utils import send_censor_word_warning


class GeneralCommands(commands.GroupCog, group_name="utility"):
    """Commands that do not fit any other category."""

    @discord.app_commands.command(
        name="greet",
        description="OutBot greets you!",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def greet(
        self,
        interaction: discord.Interaction,
    ) -> None:
        """
        OutBot greets you.

        Args:
            interaction (discord.Interaction): The discord command being invoked.

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        await interaction.response.send_message(
            f"Hello, {interaction.user.mention}! How are you?",
        )

    @discord.app_commands.command(
        name="dm",
        description="OutBot DMs you. This command requires your DMs to be turned on.",
    )
    @discord.app_commands.describe(message="What would you like OutBot to DM you?")
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def dm(
        self,
        interaction: discord.Interaction,
        message: app_commands.Range[str, 1, 1000],
    ) -> None:
        """
        DM the user who invoked the command.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.
            message (str): The message the user wants to be DMed by OutBot. Maximum length: 1000 characters.

        Allowed Mentions:
            None

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        if await send_censor_word_warning(interaction, message):
            return

        try:
            await interaction.user.send(
                f"||{message}||", allowed_mentions=discord.AllowedMentions.none()
            )

            await interaction.response.send_message(
                "DM has been sent!",
                ephemeral=True,
            )

        except discord.Forbidden:
            await interaction.response.send_message(
                "I could not send you a DM. This may be because you have them turned off. Please try turning them on and try again. If the issue persists, please open a ticket or use /report.",
                ephemeral=True,
            )

    @discord.app_commands.command(
        name="echo",
        description="Make OutBot say a specific message!",
    )
    @discord.app_commands.describe(message="What would you like OutBot to say?")
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def echo(
        self,
        interaction: discord.Interaction,
        message: app_commands.Range[str, 1, 750],
    ) -> None:
        """
        Says what the user passed in.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.
            message (str): What the user wants OutBot to say. Maximum length: 750 characters.

        Allowed Mention:
            None

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        if await send_censor_word_warning(interaction, message):
            return

        embed_message: discord.Embed = discord.Embed(
            title=f"{interaction.user} has said: ",
            description=f"{message}",
            colour=discord.Colour.green(),
        )
        embed_message.set_footer(
            text="You may report the user if anything inappropriate was said."
        )
        await interaction.response.send_message(
            embed=embed_message,
            allowed_mentions=discord.AllowedMentions.none(),
        )

    @discord.app_commands.command(
        name="poll",
        description="Create a poll.",
    )
    @discord.app_commands.describe(
        title="What is your poll's title?",
        question="What is the question you would like to ask?",
    )
    async def poll(
        self,
        interaction: discord.Interaction,
        title: app_commands.Range[str, 5, 100],
        question: app_commands.Range[str, 10, 150],
    ) -> None:
        """
        Creates an embed with a title and a question that users can add reactions to.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.
            title (str): The title the user wants their embed to have. Maximum length: 100 characters.
            question (str): The question of their poll (description). Maximum length: 150 characters.

        Allowed Mentions:
            None

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        if await send_censor_word_warning(
            interaction, title
        ) or await send_censor_word_warning(interaction, question):
            return

        embed_message: discord.Embed = discord.Embed(
            title=title,
            description=question,
        )

        await interaction.response.defer()

        await interaction.followup.send(
            embed=embed_message,
            allowed_mentions=discord.AllowedMentions.none(),
        )

        poll_message = await interaction.original_response()

        asyncio.gather(*(poll_message.add_reaction(emoji) for emoji in EMOJIS))


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GeneralCommands(bot))
