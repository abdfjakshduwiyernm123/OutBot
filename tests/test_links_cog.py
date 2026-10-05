# pyright: reportCallIssue=false

from unittest.mock import AsyncMock, Mock

import discord
import pytest

from cogs import LinksCommands
from utils import (
    CODE_OF_CONDUCT,
    CONTRIBUTING_POLICY,
    DISCORD_SERVER_INVITE_LINK,
    GITHUB_LINK,
    OUTBOT_INVITE_LINK,
    PRIVACY_POLICY,
    SECURITY_POLICY,
    TERMS_OF_SERVICE,
)


@pytest.mark.asyncio
async def test_links_commands_discord() -> None:
    """Tests /link discord"""
    interaction = Mock()
    interaction.response.send_message = AsyncMock()

    links_commands = LinksCommands()

    await links_commands.outmyth_discord_server_invite_link.callback(
        links_commands, interaction
    )
    interaction.response.send_message.assert_awaited_once_with(
        DISCORD_SERVER_INVITE_LINK
    )


@pytest.mark.asyncio
async def test_links_commands_invite() -> None:
    """Tests /link discord"""
    interaction = Mock()
    interaction.response.send_message = AsyncMock()

    links_commands = LinksCommands()

    await links_commands.invite.callback(links_commands, interaction)

    interaction.response.send_message.assert_awaited_once_with(OUTBOT_INVITE_LINK)


@pytest.mark.asyncio
async def test_links_commands_github() -> None:
    """Tests /link discord"""
    interaction = Mock()
    interaction.response.send_message = AsyncMock()

    links_commands = LinksCommands()

    await links_commands.github.callback(links_commands, interaction)

    interaction.response.send_message.assert_awaited_once_with(GITHUB_LINK)


@pytest.mark.asyncio
async def test_information_commands_help() -> None:
    """Tests /info help"""
    links_commands = LinksCommands()
    interaction = Mock()
    interaction.response.send_message = AsyncMock()

    await links_commands.policy.callback(links_commands, interaction)

    call = interaction.response.send_message.call_args
    embed_message = call.kwargs["embed"]

    assert embed_message.title == "OutBot's Policy Links: \n"
    assert embed_message.description == (
        f"- {PRIVACY_POLICY}\n"
        f"- {TERMS_OF_SERVICE}\n"
        f"- {SECURITY_POLICY}\n"
        f"- {CONTRIBUTING_POLICY}\n"
        f"- {CODE_OF_CONDUCT}\n"
    )
    assert embed_message.colour == discord.Colour.dark_grey()
