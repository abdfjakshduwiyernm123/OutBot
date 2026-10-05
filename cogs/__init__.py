from .developer_cog import DeveloperCommands
from .fun_cog import FunCommands
from .general_cog import GeneralCommands
from .information_cog import InformationCommands
from .links_cog import LinksCommands
from .moderation_cog import ModerationCommands
from .privacy_cog import PrivacyCommands
from .rules_cog import RulesCommands
from .support_cog import SupportCommands

__all__: list[str] = [
    "DeveloperCommands",
    "FunCommands",
    "GeneralCommands",
    "InformationCommands",
    "LinksCommands",
    "ModerationCommands",
    "PrivacyCommands",
    "RulesCommands",
    "SupportCommands",
]
