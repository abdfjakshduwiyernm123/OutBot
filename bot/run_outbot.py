import discord

from .load_env import load_env_bot_token
from .outbot_custom_setup import custom_setup


def run_bot() -> None:
    """Runs OutBot"""
    outbot = custom_setup()
    try:
        outbot.run(load_env_bot_token())
    except discord.LoginFailure:
        raise RuntimeError('The Discord bot token in "config/.env" is invalid.')
