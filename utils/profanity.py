import discord

from config import CENSOR_WORDS


async def send_censor_word_warning(
    interaction: discord.Interaction, user_input: str
) -> bool:
    """
    Checks if any word in in that the user passed in contains any words from the tuple of Censor words.

    args:
        interaction (discord.Interaction): Any command that OutBot has that accepts user input.
        user_input (str): Checks what the user inputted.

    Returns:
        bool
    """

    contains_censor_word = any(word in user_input.lower() for word in CENSOR_WORDS)

    if contains_censor_word:
        await interaction.response.send_message(
            "Your message cannot contain swear words/other offensive words. To report an issue, please open a ticket.",
            ephemeral=True,
        )
        return contains_censor_word
    return False
