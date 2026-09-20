import os

import discord
from discord import Status
from dotenv import load_dotenv

from bot import OutBot


if __name__ == "__main__":
    load_dotenv("config/.env")
    DISCORD_TOKEN: str | None = os.getenv("DISCORD_TOKEN")
    if DISCORD_TOKEN is None:
        raise RuntimeError("The Discord bot token was not found in config/.env.")

    bot = OutBot(
        activity=discord.Game(name="📖 Reading Documentation"),
        command_prefix="NONE",
        intents=discord.Intents.default(),
        status=Status.idle,
    )

    try:
        bot.run(DISCORD_TOKEN)

    except discord.LoginFailure:
        raise RuntimeError("The Discord bot token in config/.env is invalid.")
