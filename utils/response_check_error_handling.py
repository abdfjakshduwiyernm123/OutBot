import discord


async def response_check(
    interaction: discord.Interaction, *, error_message: str, ephemeral: bool = True
) -> None:
    """
    Util for checking if an interaction has been responded to

       Args:
                error_message (str): Error message the bot is going to send to the user
            ephemeral (bool): If the message is ephemeral
    """
    if interaction.response.is_done():
        await interaction.followup.send(
            error_message,
            ephemeral=ephemeral,
        )
        return
    else:
        await interaction.response.send_message(
            error_message,
            ephemeral=ephemeral,
        )
        return
