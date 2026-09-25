from .error_handling import on_app_command_error
from .load_env import load_env_bot_token
from .run_outbot import run_bot
from utils import custom_setup

if __name__ == "__main__":
    outbot = custom_setup()
    outbot.tree.on_error = on_app_command_error
    load_env_bot_token()
    run_bot()
