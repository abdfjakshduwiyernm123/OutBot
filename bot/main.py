from .load_env import load_env_bot_token
from .outbot_custom_setup import custom_setup
from .run_outbot import run_bot

if __name__ == "__main__":
    outbot = custom_setup()
    load_env_bot_token()
    run_bot()
