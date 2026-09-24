import os

from dotenv import load_dotenv


def load_env_bot_token() -> str | None:
    """
    Loads OutBot's discord bot token.

    Returns:
        discord_token (str | None): OutBot's discord token.
    """
    load_dotenv("config/.env")
    discord_token: str | None = os.getenv("DISCORD_TOKEN")

    if discord_token is None:
        raise RuntimeError("The Discord bot token was not found in config/.env.")

    return discord_token
