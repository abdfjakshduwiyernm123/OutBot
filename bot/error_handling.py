import discord

from utils import ERROR_MESSAGE


async def on_app_command_error(
    interaction: discord.Interaction, error: discord.AppCommandError
) -> None:
    """
    Sends an error message to the user when an error occurs.

    Args:
        interaction (discord.Interaction): The discord command that triggered the error
        error (app_commands.AppCommandError): Checks errors.
    """

    if isinstance(error, discord.app_commands.CommandOnCooldown):
        RATE_LIMIT_MESSAGE = (
            f"Rate limited! Try again in {error.retry_after:.2f} seconds."
        )
        if interaction.response.is_done():
            await interaction.followup.send(RATE_LIMIT_MESSAGE, ephemeral=True)
            return
        else:
            await interaction.response.send_message(RATE_LIMIT_MESSAGE, ephemeral=True)
            return

    else:
        if interaction.response.is_done():
            await interaction.followup.send(ERROR_MESSAGE, ephemeral=True)

        else:
            await interaction.response.send_message(ERROR_MESSAGE, ephemeral=True)
