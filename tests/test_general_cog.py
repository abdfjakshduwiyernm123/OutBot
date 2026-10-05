# pyright: reportCallIssue=false

from unittest.mock import AsyncMock, Mock

import pytest

from cogs import GeneralCommands


@pytest.mark.asyncio
async def test_general_commands_greet() -> None:
    """Tests /link discord"""
    interaction = Mock()
    interaction.response.send_message = AsyncMock()

    general_commands = GeneralCommands()

    await general_commands.greet.callback(general_commands, interaction)

    interaction.response.send_message.assert_awaited_once_with(
        f"Hello, {interaction.user.mention}! How are you?"
    )
