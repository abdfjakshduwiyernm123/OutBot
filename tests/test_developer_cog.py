from unittest.mock import AsyncMock, Mock

import discord
import pytest

from bot import OutBot
from cogs import DeveloperCommands


@pytest.mark.asyncio
async def test_developer_commands_credit() -> None:
    """Tests the command /developer credit"""

    bot = Mock(spec=OutBot)
    developer_commands = DeveloperCommands(bot)

    interaction = Mock()
    interaction.response.send_message = AsyncMock()

    await developer_commands.credit.callback(developer_commands, interaction)  # pyright: ignore[reportCallIssue]

    call = interaction.response.send_message.call_args
    embed_message = call.kwargs["embed"]

    assert embed_message.title == "OutBot's Contributors/Developers: "
    assert embed_message.description == (
        "'someVeryCoolProgrammer' is the only developer/s and/or contributor/s for OutBot currently!"
    )
    assert embed_message.colour == discord.Colour.red()
