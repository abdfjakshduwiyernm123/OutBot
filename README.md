# Table Of Contents

- [About](#about)
- [Useful Link](#useful-links)
- [Ephemeral Messages](#what-are-ephemeral-messages)
- [OutBot's Config](#outbots-config)
- [Getting Started](#getting-started)
    - [Requirements](#requirements)
        - [Windows](#windows)
        - [Linux/macOS](#linuxmacos)
    - [Getting A Local Copy Of OutBot](#getting-a-local-copy-of-outbot)
    - [Virtual Environment](#creating-a-virtual-environment)
        - [Windows Virtual Environment](#windows-virtual-environment)
        - [Linux/macOS Virtual Environment](#linuxmacos-virtual-environment)
    - [Discord Bot Token](discord-bot-token)
    - [Discord Developer Portal Setup](#discord-developer-portal-setup)
    - [Creating .env](#creating-env)
    - [Adding Your Bot To Your Apps/Servers](#adding-your-bot-to-your-appsservers)
    - [Changing Developer Id](#changing-developer-id)
- [IMPORTANT NOTICE](#important-notice)
- [Inviting OutBot To Your Apps/Discord Servers](#inviting-outbot-to-your-appsdiscord-servers)
- [Developer notes](#developer-notes)

---

# About

OutBot is an open source, privacy respecting Discord utility bot built using **discord.py**. **OutBot is 100% open source**. Most popular Discord bots **NOT** open source. Open Source helps users understand what they are using while allowing them to do whatever they want to do with the project (depending on the license). It can also help make your project become a lot better. Take the kernel for instance, if it were closed source, it would be nowhere near as good as it is now.

OutBot uses **NO** privileged intents. Most popular discord bots use them. Member intents allows the bot to see members joining/leaving the server. Presence intent allows the bot to see member status (idle, offline, online, do not disturb et cetera). Message content intent allows the bot to see user messages. This is intent usually used for prefix commands. However OutBot does use discor's default intents.  

For more information, please read: [OutBot's Privacy Policy](https://github.com/abdfjakshduwiyernm123/OutBot/blob/main/PRIVACY.md)

OutBot's Current Version: **v0.5.8**

---

# Useful Links

[OutBot's TOS](https://github.com/abdfjakshduwiyernm123/OutBot/blob/main/TERMS.md)  

[OutBot's Privacy Policy](https://github.com/abdfjakshduwiyernm123/OutBot/blob/main/PRIVACY.md)  

[OutBot's Security Policy](https://github.com/abdfjakshduwiyernm123/OutBot?tab=security-ov-file)  

[OutBot's License](https://github.com/abdfjakshduwiyernm123/OutBot/?tab=MIT-1-ov-file)  

[OutBot's Invite link](https://discord.com/oauth2/authorize?client_id=1525595736706781384)  

---

# What Are Ephemeral Messages?

> Some messages can only be seen by the user who triggered the command. (ephemeral=True)
> Most messages can be seen by everyone. (ephemeral=False by default).
> The following commands are some examples of ephemeral=True commands:

- **`/dm`**
- **`/help`**
- **`/freenitro`**

> Error messages from the bot are all ephemeral=True.

---

# OutBot's Config

OutBot does **NOT** use prefix  commands. Therefore, command_prefix="NONE". OutBot uses **NO** privileged intents. Therefore, intents=discord.Intents.default()

OutBot's Config:
```py
bot = OutBot(
    activity=discord.Game(name="📖 Reading Documentation"),
    command_prefix="NONE",
    intents=discord.Intents.default(),
    status=Status.idle,
)
```

Command prefix has to be set to a string. "NONE" was used to show that OutBot uses no prefix commands. You have freedom to change that. Because OutBot uses no privillaged intents, "(current time) WARNING  discord.ext.commands.bot Privileged message content intent is missing, commands may not work as expected." will be displayed in the terminal. If you want prefix commands enable the "Message Content" privillaged intent. You can ignore it if you don't plan on using prefix commands.

---

# Getting Started

## Requirements

- [Python's Latest Version](https://www.python.org/downloads/)
- discord.py 2.7.1
- git - [Git Install link](https://git-scm.com/install/) 

### Windows:

You have to install this to allow OutBot to work:
```shell
pip install -r requirements/base.txt
```

If you want to use ruff and cloc:
```shell
pip install -r requirements/developer.txt
```

If you want to use tests:
```shell
pip install -r requirements/tests.txt
```

### Linux/macOS:

You have to install this to allow OutBot to work:
```shell
pip3 install -r requirements/base.txt
```

If you want to use ruff and cloc use:
```shell
pip3 install -r requirements/developer.txt
```

If you want to use tests:
```shell
pip3 install -r requirements/tests.txt
```

## Getting A Local Copy Of OutBot

```shell
git clone https://github.com/abdfjakshduwiyernm123/OutBot.git
```

```shell
cd OutBot
```

## Creating A Virtual Environment

### Windows Virtual Environment
Windows:
```shell
python -m venv .venv
```

Activating it:
Windows:
```shell
.venv\Scripts\Activate.ps1
```

### Linux/macOS Virtual Environment

Linix/macOS:
```shell
python3 -m venv .venv
```

```shell
source .venv/bin/activate
```

## Discord Bot Token

You now have a local copy of OutBot on your computer. For OutBot to actually run, we will need a Discord Bot Token. 
DO NOT SHARE YOUR DISCORD BOT TOKEN WITH ANYONE. IF YOU DO, YOU GIVE THEM ACCESS TO YOUR BOT. THEY CAN EVEN FIND YOUR EMAIL WITH IT.

## Discord Developer Portal Setup

Head over to [Discord Developer portal](https://discord.com/developers/applications) and sign in/create an account. Click "new application". Name your bot and accept Discord's Developer TOS/Privacy Policy. 

## Creating .env

Create a new file called .env and make sure it is in .gitignore. Create a variable called DISCORD_TOKEN. To get your discord bot's token. Head over to [Discord Developer Portal](https://discord.com/developers/home), click "Bot" and then click "Reset Token". Click "Yes do it to" confirm. Copy your Discord token into the file ".env".

## Adding Your Bot To Your Apps/Servers

Go to the [Discord Developer portal Installation Tab](https://discord.com/developers/applications/installation); copy the install link and paste the install link into your browser. Then, choose whether you want OutBot in your apps or if you would like to add OutBot to your server/s. 

## Changing Developer Id

There is one final thing we need to do and that is to change the developer id. By default it is set to OutBot's developers. By keeping it that way, you will NOT be able to sync OutBot's command tree. Go to Discord's settings and enable developer mode. Right click on your profile and click "copy user id". Copy that user id into config/.env (the same file with your disocrd token).

# IMPORTANT NOTICE

**IF YOU DO NOT ADD YOUR DISCORD BOT TOKEN TO ".env", A RUNTIME ERROR WILL BE RAISED.**

# Inviting OutBot To Your Apps/Discord Servers

To invite OutBot to your server(s)/add it to your apps, head over to this link:

[OutBot's Invite Link](https://discord.com/oauth2/authorize?client_id=1525595736706781384&scope=bot%20applications.commands)

Then choose if you want OutBot to your Discord server(s) or to your apps.

---

# Developer notes

To report any issues (other than security vulnerabilities) please open a GitHub issue, a ticket on OutMyth, or use /report.  
Before reporting a security issue please read [OutBot's Security Policy](https://github.com/abdfjakshduwiyernm123/OutBot?tab=security-ov-file).  
Thank **you** for using OutBot! ❤️
