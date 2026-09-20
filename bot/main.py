import os

import discord

from bot import load_env_bot_token, OutBot


if __name__ == "__main__":
    discord_token = load_env_bot_token()

    bot = OutBot(
        activity=discord.Game(name="📖 Reading Documentation"),
        command_prefix="NONE",
        intents=discord.Intents.default(),
        status=discord.Status.idle,
    )

    try:
        bot.run(discord_token)
    except discord.LoginFailure:
        raise RuntimeError("The Discord bot token in config/.env is invalid.")
