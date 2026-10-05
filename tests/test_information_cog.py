# pyright: reportCallIssue=false

from unittest.mock import AsyncMock, Mock

import discord
import pytest

from bot import OutBot
from cogs import InformationCommands
from utils import (
    BOT_VERSION,
    GITHUB_LINK,
    OUTBOT_INVITE_LINK,
    OUTBOT_LICENSE,
    PRIVACY_POLICY,
    TERMS_OF_SERVICE,
)


@pytest.mark.asyncio
async def test_information_commands_ping_button() -> None:
    """Tests /info ping"""
    bot = Mock(spec=OutBot)
    bot.latency = 0.090

    information_commands = InformationCommands(bot)

    interaction = Mock()
    interaction.response.send_message = AsyncMock()

    await information_commands.ping.callback(information_commands, interaction)

    call = interaction.response.send_message.call_args
    embed_message = call.kwargs["embed"]

    assert embed_message.title == "Pong 🏓!"
    assert embed_message.description == "OutBot's gateway latency: `90`ms!"
    assert embed_message.colour == discord.Colour.green()


@pytest.mark.asyncio
async def test_information_commands_help() -> None:
    """Tests /info help"""
    bot = Mock(spec=OutBot)
    information_commands = InformationCommands(bot)

    interaction = Mock()
    interaction.response.send_message = AsyncMock()

    await information_commands.help.callback(information_commands, interaction)

    call = interaction.response.send_message.call_args
    embed_message = call.kwargs["embed"]

    assert embed_message.title == "📋 OutBot's Command List: \n"
    assert embed_message.description == (
        "\n# 💻 Developer Commands: \n"
        "- **`/developer devs`**\n"
        "- **`/developer sync`**\n"
        "#\n 🎉 Fun Commands: \n"
        "- **`/fun freenitro`**\n"
        "- **`/fun fakeban`**\n"
        "#\n ⚙️ General Commands: \n"
        "- **`/general hello`**\n"
        "- **`/general dm`**\n"
        "- **`/general ehco`**\n"
        "- **`/general poll`**\n"
        "#\n 🧠 Information Commands: \n"
        "- **`/info ping`**\n"
        "- **`/info help`**\n"
        "- **`/info about`**\n"
        "- **`/info roadmap`**\n"
        "#\n 🔗 Link Commands: \n"
        "- **`/link discord`**\n"
        "- **`/link invite`**\n"
        "- **`/link github`**\n"
        "- **`/link contributing_policy`**\n"
        "- **`/link contributing_policy`**\n"
        "- **`/link contributing policy`**\n"
        "- **`/link license`**\n"
        "- **`/link privacy_policy`**\n"
        "- **`/link tos`**\n"
        "- **`/link security_policy`**\n"
        "#\n 🛡️ Moderation Commands: \n"
        "- **`/moderation ban`**\n"
        "#\n 🔐 Privacy Commands: \n"
        "- **`/privacy privacy_information`**\n"
        "- **`/privacy data`**\n"
        "#\n ⚖️ Rules Commands: \n"
        "- **`/rules outmythrules`**\n"
        "- **`/rules outbotrules`**\n"
        "#\n 🙋‍♂️ Support Commands: \n"
        "- **`/support report`**\n"
        "- **`/support feedback`**\n"
    )
    assert embed_message.colour == discord.Colour.blurple()


@pytest.mark.asyncio
async def test_information_commands_about() -> None:
    """Tests /info about"""

    bot = Mock(spec=OutBot)
    interaction = Mock()
    interaction.response.send_message = AsyncMock()

    information_commands = InformationCommands(bot)

    await information_commands.about.callback(information_commands, interaction)

    call = interaction.response.send_message.call_args
    embed_message = call.kwargs["embed"]

    assert embed_message.title == "About: "
    assert embed_message.description == (
        "Outbot is a general utility bot that takes user privacy and security seriously.\n"
        "Most discord bots do not. OutBot is a general purpose utility bot.\n"
        f"- Outbot's Version: v{BOT_VERSION}\n"
        f"OutBot's sourse code is available at: {GITHUB_LINK} under {OUTBOT_LICENSE}\n"
        f"{OUTBOT_INVITE_LINK}\n"
        f"{PRIVACY_POLICY}\n"
        f"{TERMS_OF_SERVICE}\n"
    )
    assert embed_message.colour == discord.Colour.blurple()
    assert embed_message.footer.text == "OutBot was made with python using discord.py."


@pytest.mark.asyncio
async def test_information_commands_roadmap() -> None:
    """Tests /info roadmap"""

    bot = Mock(spec=OutBot)
    interaction = Mock()
    interaction.response.send_message = AsyncMock()

    information_commands = InformationCommands(bot)

    await information_commands.roadmap.callback(information_commands, interaction)
    
    call = interaction.response.send_message.call_args
    embed_message = call.kwargs["embed"]

    assert embed_message.title == "OutBot's Planned Features: "
    assert embed_message.description == (
        "# User: \n"
        "- ||🛠️|| More interactive and fun commands for users\n"
        "- ||🛠️|| Add better way to report.\n"
        "- ||❌️|| Host Outbot's privacy policy and terms of service on a website.\n"
        "\n# Code quality: \n"
        "- ||🛠️|| More tests and clearer docs.\n"
        "- ||❌️|| Add ymal files to .github.\n"
        "- ||✅|| More robust code.\n"
    )
    assert embed_message.colour == discord.Colour.green()
    assert len(embed_message.fields) == 1
    assert embed_message.fields[0].name == "Key: "
    assert (
        embed_message.fields[0].value
        == "✅ = Feature completed - 🛠️ = In development - ❌️ = Did not started to working on feature"
    )
    assert embed_message.fields[0].inline is True
