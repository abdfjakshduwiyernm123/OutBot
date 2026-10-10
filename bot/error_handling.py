import discord
from discord import app_commands

from utils import GITHUB_LINK, response_check


async def on_app_command_error(
    interaction: discord.Interaction, error: app_commands.AppCommandError
) -> None:
    """
    Sends an error message to the user when an error occurs.

    Args:
        interaction (discord.Interaction): The discord command that triggered the error
        error (app_commands.AppCommandError): Checks errors.
    """

    if isinstance(error, app_commands.CommandOnCooldown):
        await response_check(
            interaction,
            f"Rate limited! Try again in {error.retry_after:.2f} seconds.",
            ephemeral=True,
        )

    elif isinstance(error, app_commands.MissingPermissions):
        await response_check(
            interaction,
            "You do not have the permissions to use that command.",
            ephemeral=True,
        )

    elif isinstance(error, app_commands.BotMissingPermissions):
        permissions = ", ".join(error.missing_permissions)
        await response_check(
            interaction,
            f"I'm missing these permissions: \n- `{permissions}`\n",
            ephemeral=True,
        )
        
    elif isinstance(error, app_commands.CommandNotFound):
        await response_check(
            interaction,
            f"That command does not exist anymore.",
            ephemeral=True,
        )

    elif isinstance(error, app_commands.CommandInvokeError):
        await response_check(
            interaction,
            f"Something went wrong while executing this command. Please open a ticket or a GitHub issue ({GITHUB_LINK})",
            ephemeral=True,
        )



    else:
        await response_check(
            interaction,
            f"# Something went wrong :(\nPlease open a ticket or a GitHub issue ({GITHUB_LINK})",
            ephemeral=True,
        )
