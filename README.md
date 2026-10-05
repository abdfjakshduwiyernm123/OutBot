# Table Of Contents

- [About](#about)
    - [Intents](#intents)
    - [What Is Open Source?](#what-is-open-source)
- [Useful Link](#useful-links)
- [Ephemeral Messages](#what-are-ephemeral-messages)
- [OutBot's Config](#outbots-config)
- [Getting Started](#getting-started)
    - [Requirements](#requirements)
        - [Windows](#installing-dependencies-on-windows)
        - [Linux/macOS](#installing-dependencies-on-linuxmacos)
    - [Getting A Local Copy Of OutBot](#getting-a-local-copy-of-outbot)
    - [Virtual Environment](#creating-a-virtual-environment)
        - [Windows Virtual Environment](#windows-virtual-environment)
        - [Linux/macOS Virtual Environment](#linuxmacos-virtual-environment)
    - [Discord Bot Token](#discord-bot-token)
    - [Discord Developer Portal Setup](#discord-developer-portal-setup)
    - [Creating .env](#creating-env)
    - [Adding Your Bot To Your Apps/Servers](#adding-your-bot-to-your-appsservers)
    - [Changing Developer Id](#changing-developer-id)
    - [Run OutBot](#run-outbot)
        - [Run OutBot On Windows](#run-outbot-on-windows)
        - [Run OutBot On Linux/macOS](#run-outbot-on-linuxmacos)
- [IMPORTANT NOTICE](#important-notice)
- [Inviting OutBot To Your Apps/Discord Servers](#inviting-outbot-to-your-appsdiscord-servers)
- [Developer notes](#developer-notes)

---

# About

OutBot is an open source, privacy respecting Discord utility bot built using **discord.py**. **OutBot is 100% open source**. Most popular Discord bots are **NOT** open source. Open source is covered in more detail [here](https://opensource.org/osd).

OutBot uses **NO** privileged intents. OutBot does **NOT** use **ANY GATEWAY INTENTS**. Intents will be covered in more detail [here](#intents).

[![GitHub Release](https://img.shields.io/github/v/release/abdfjakshduwiyernm123/OutBot)](https://github.com/abdfjakshduwiyernm123/OutBot/releases/latest)

## Intents

There are two types of intents. Privileged intents and regular intents. Think of an intent as a way of the bot to "subscribe" to specific events (information). OutBot uses no intents at all because it does not need any. This may change in the future.
```py
intents = discord.Intents.none()
```

Discord always has something going on. A member gets banned, a member goes offline, a member sends a message etc. That information does not go to your bot. Intents are a way to tell discord what to send your bot. For example "message content privileged intent" is used when your bot needs command prefixes. This is because your bot needs to know if a message starts with your given command prefix with your command name (there are more uses to "message content privileged intent" prefix commands are probably the most common). 

A privileged intent is an intent that is more sensitive or potentially less private than regular intents. There are three privileged intents which are covered below. These need to be enabled in the Discord Developer Portal and requested by your bot in code. Non-privileged intents can be enabled by:  
```py
intents = discord.Intents.default()  # Enables all default non-privileged intents
```

You can disable specific gateway intents by:  
```py
intents.guilds = False  # Disables guild intents.
```

To disable all non-privileged gateway intents 
```py
intents = discord.Intents.none()  # Disables all default non-privileged gateway intents
```

| Name | Privileged | What Does It Do? | Enabled |
| --- | --- | --- | --- |
| Member Intent | Yes | Receives member join, leave, and update information | No |
| Message Content Intent | Yes | Allows the bot to read message content | No |
| Presence Intent | Yes | Receives member activity and status updates | No |
| Guilds Intent | No | Receives guild/server-related events | No |
| Ban Intent | No | Receives information when users are banned or unbanned | No |
| Emoji Intent | No | Receives emoji/sticker creation, update, and deletion events | No |
| Integrations Intent | No | Receives integration-related events | No |
| Webhook Intent | No | Receives webhook creation, update, and deletion events | No |
| Invite Intent | No | Receives invite creation and deletion events | No |
| Voice States Intent | No | Receives voice state updates, such as users joining or leaving voice channels | No |
| Messages Intent | No | Receives message creation, update, and deletion events in guilds | No |
| Reactions Intent | No | Receives reaction add and removal events on messages | No |
| Typing Intent | No | Receives typing events in guild channels | No |
| DM Messages Intent | No | Receives message events in direct messages | No |
| DM Reactions Intent | No | Receives reaction events in direct messages | No |
| DM Typing Intent | No | Receives typing events in direct messages | No |


## What Is Open Source? 

Open source is when a project's source code is available. Users can modify, distribute, sell, and contribute to the project. Some examples you may have heard of are: the Linux kernel, python, gcc, typescript, and vscode. Open source allows more user transparency than closed source does. It can also be more convenient for users. Lets say you have a problem. For a closed source project, you would have to open support tickets and sometimes not get the help you wanted. With an open source project, you can solve the problem yourself. The link [here](https://opensource.org/osd) discusses open source in much more detail.

---

# Useful Links

[OutBot's TOS](https://github.com/abdfjakshduwiyernm123/OutBot/blob/main/TERMS.md)  

[OutBot's Privacy Policy](https://github.com/abdfjakshduwiyernm123/OutBot/blob/main/PRIVACY.md)  

[OutBot's Security Policy](https://github.com/abdfjakshduwiyernm123/OutBot?tab=security-ov-file)  

[OutBot's License](https://github.com/abdfjakshduwiyernm123/OutBot/?tab=MIT-1-ov-file)  

[OutBot's Invite Link Guild (Server)](https://discord.com/oauth2/authorize?client_id=1525595736706781384&scope=bot%20applications.commands)  
[OutBot's Invite Link User](https://discord.com/oauth2/authorize?client_id=1525595736706781384&scope=applications.commands)

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

OutBot does **NOT** use prefix  commands. OutBot uses **NO** gateway intents. Therefore, intents=discord.Intents.none()

---

# Getting Started

## Requirements

- [Python's Latest Version](https://www.python.org/downloads/)
- discord.py (Newest version) You can check discord.py latest version [here](https://pypi.org/project/discord.py/)
- [git](https://git-scm.com/install/) 

### Installing Dependencies On Windows:

You have to install this to allow OutBot to work:
```shell
pip install -r requirements/core.txt
```

If you want to use ruff and cloc:
```shell
pip install -r requirements/developer.txt
```

If you want to use tests:
```shell
pip install -r requirements/tests.txt
```

### Installing Dependencies On Linux/macOS:

You have to install this to allow OutBot to work:
```shell
pip3 install -r requirements/core.txt
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

Linux/macOS:
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

To add OutBot to your apps and/or servers change the placeholder in the links to your bots id.

```text
https://discord.com/oauth2/authorize?client_id=YOUR_BOT_ID&scope=bot%20applications.commands
OutBot's Invite Link Userhttps://discord.com/oauth2/authorize?client_id=YOUR_BOT_ID&scope=applications.commands
```

To get your bots id, head over to [disord developer portal](https://discord.com/developers) and log in with your discord account. Now click on your application and your bot id should be after application. Eg: https://discord.com/developers/applications/YOUR_BOT_ID  

## Changing Developer Id

There is one final thing we need to do and that is to change the developer id. By default it is set to OutBot's developers. By keeping it that way, you will **NOT** be able to sync OutBot's command tree. Go to Discord's settings and enable developer mode. Right click on your profile and click "copy user id". Copy that user id into config/.env (the same file with your disocrd token).  


## Run OutBot

### Run OutBot On Windows
```shell
py -m bot.main
```

### Run OutBot On Linux/macOS
```shell
py -m bot.main
```

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
