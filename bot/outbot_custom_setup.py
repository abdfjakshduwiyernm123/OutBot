import discord

from .outbot import OutBot


def custom_setup() -> OutBot:
    """Util function to reuse OutBot's custom setup."""
    outbot: OutBot = OutBot(
        activity=discord.Game(name="📖 Reading Documentation"),
        command_prefix="NONE",
        intents=discord.Intents.default(),
        status=discord.Status.idle,
    )
    return outbot
