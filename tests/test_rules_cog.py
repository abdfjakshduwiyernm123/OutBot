# pyright: reportCallIssue=false

from unittest.mock import AsyncMock, Mock

import pytest

from cogs import RulesCommands
from utils import TERMS_OF_SERVICE


@pytest.mark.asyncio
async def test_rules_commands_outmyth_rules() -> None:
    """Tests the command /rules outmyth_rules"""

    interaction = Mock()
    interaction.response.send_message = AsyncMock()

    rules_commands = RulesCommands()

    await rules_commands.outmyth_rules.callback(rules_commands, interaction)

    interaction.response.send_message.assert_awaited_once_with(
        "# 📜 OutMyth's Rules :\n\n"
        "# 1) ❌ NO NSFW And NO Malicious Content\n"
        "- Absolutely **NO** NSFW content, pornography, sexual content, or malicious links.\n\n"
        "# 2) 🤬 NO Swearing / Offensive Language\n"
        "- Use common sense when chatting.\n"
        "- Do **NOT** use censored words or other offensive language.\n\n"
        "# 3) 🔐 Respect Privacy\n"
        "- Do **NOT** dox or share anyone’s personal information.\n"
        "- Do **NOT** DM anyone without a valid reason.\n\n"
        "# 4) 🗣📢 No Self Promotion\n"
        "- **NO** advertising in DMs or channels.\n"
        "- This applies to EVERYONE, including staff and owners.\n\n"
        "# 5) @️ Use Mentions Responsibly And Lessange Spam\n\n"
        "- **DON’T** ping @everyone, @here, or use any other type of mass pinging or message spam.\n\n"
        "# 6) 🎟️ Tickets\n"
        "- Do NOT open tickets without a valid reason.\n\n"
        "# 7) 🫂 Behaviour\n"
        "- Be kind, respectful, and helpful to everyone.\n"
        "- Avoid disruptive behaviour. This includes malicious, manipulative, rage-baiting, or otherwise disruptive behaviour."
    )


@pytest.mark.asyncio
async def test_rules_commands_outbot_rules() -> None:
    """Tests the command /rules outbot"""

    interaction = Mock()
    interaction.response.send_message = AsyncMock()

    rules_commands = RulesCommands()

    await rules_commands.outbot_rules.callback(rules_commands, interaction)

    interaction.response.send_message.assert_awaited_once_with(
        "## OutBot Rules\n\n"
        "By using OutBot you agree to comply with Discord's Terms Of Service and Community Guidelines.\n"
        f"More information is available at: {TERMS_OF_SERVICE}.\n"
        "Breaking these rules will result in a punishment. The severity of the punishment depends on how nature and seriousness of the violation.\n"
    )
