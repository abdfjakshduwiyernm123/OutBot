# pyright: reportCallIssue=false

from unittest.mock import AsyncMock, Mock

import discord
import pytest

from cogs import PrivacyCommands
from utils import GITHUB_LINK, PRIVACY_POLICY


@pytest.mark.asyncio
async def test_privacy_commands_guide() -> None:
    """Tests the command /privacy guide"""

    interaction = Mock()
    interaction.response.send_message = AsyncMock()

    privacy_commands = PrivacyCommands()

    await privacy_commands.guide.callback(privacy_commands, interaction)

    call = interaction.response.send_message.call_args
    embed_message = call.kwargs["embed"]

    assert embed_message.title == "🔒 Information About OutBot's Privacy: \n"
    assert embed_message.description == (
        "\nOutBot has **NO** logs even for errors.\n"
        "OutBot does not use **ANY** gateway intents.\n"
        f"OutBot is 100% open source: {GITHUB_LINK}\n"
        f"More information at: {PRIVACY_POLICY}\n"
    )
    assert embed_message.colour == discord.Colour.dark_blue()


@pytest.mark.asyncio
async def test_privacy_commands_data() -> None:
    """Tests the command /privacy data"""

    interaction = Mock()
    interaction.response.send_message = AsyncMock()

    privacy_commands = PrivacyCommands()

    await privacy_commands.data.callback(privacy_commands, interaction)

    call = interaction.response.send_message.call_args
    embed_message = call.kwargs["embed"]

    assert embed_message.title == "🗃️ What data does OutBot collect?\n"
    assert embed_message.description == (
        "\nOutBot collects/logs no data about you. The only data OutBot may keep is user feedback to help improve OutBot.\n"
        "User feedback is only kept for only the time it needs to be retained for."
        f"For more information, please read: {PRIVACY_POLICY}"
    )
    assert embed_message.colour == discord.Colour.dark_green()
