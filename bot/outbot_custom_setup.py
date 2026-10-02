import discord

from .outbot import OutBot


def custom_setup() -> OutBot:
    """Util function to reuse OutBot's custom setup."""
    outbot: OutBot = OutBot(
        activity=discord.Game(name="📖 Reading Documentation"),
        allowed_mentions=discord.AllowedMentions.none(),
        intents=discord.Intents.none(),
        status=discord.Status.idle,
    )
    return outbot
