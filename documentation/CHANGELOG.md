# OutBot Bug Fix - 22 September 2026

## Update 0.5.9

- Fixed 'bot is not definied' in the command /ping

# OutBot Bug Fix - 19 September 2026

## Update 0.5.8

- discord.user.id ---> interaction user.id

---

# OutBot Bug Fix - 16 September 2026

## Update 0.5.7

- Fixed unexpected error handling
- Fixed undifined ephemeral in rate limit error handling
- interaction.followup.send_message ---> interaction.followup.send

---

# OutBot Bug Fix - 12 September 2026

## Update 0.5.6

- Fixed /sync not working and links cog spelling errors/dupe commands

---

# OutBot Bug Fix - 12 September 2026

## Update 0.5.5

- Fixed rate limit not working

---

# OutBot Bug Fix - 12 September 2026

## Update 0.5.4

- Fixed undefined name PingUserButton and type hint OutBot
- Added bitch to censor words
- Command prefix set to null terminator (\0)

---

# OutBot Bug Fix - 11 September 2026

# Update 0.5.3

Fixed import bug. (cogs/information_cog.py)

---

# OutBot Bug Fix - 10 September 2026

## Update 0.5.2

Fixed messages not getting send because of allowed mentions.

---

# OutBot Bug Fix - 9 September 2026

## Version 0.5.1

Fixed tests not working.

---

# OutBot - Update - 9 September 2026

## Version 0.5.0

### Removed

- /outmyth and /outhis
- Removed most try except blocks and replaced it with error handling
- Commands pinging you every time you invoke them except /ping
- 6 poll reactions
- ephemeral for /say (/echo)

### Renamed

- /rickroll ---> /freenitro
- /outbot ---> /about
- /say ---> /echo
- /serverlink ---> /discord
- /hello ---> /greet

### Added / removed

- type hints
- .gitignore
- Improved documentation
- All commands are inside cogs
- Centralized error handling
- Improved code readability
- Updated all commands and commands quality
- Added an MIT License, contributing, code of conduct, tos, privacy policy, and security to OutBot's repository
- New commands (/privacy, /data, /logs, /developer, /reporthelp, /report, /feedbackhelp, /feedback, /fakeban)
- Improved ux and added buttons to the commands /ping and /freenitro
- Created a test for /developer
- Custom logger 
- Logs that delete themselves daily

Update 0.6 will more interactive commands. I think I have not been adding enough features to OutBot. 

---

# OutBot - Update - 28th July 2026

## **Version 0.4**

- **New slash commands** (/rickroll, /invite, /roadmap, /serverlink, /youtube, /ping, /outbot, /botrules)
- **Removed prefix commands**
- **Improved readability** (Code ran through black)
- **on_ready print statement update**
- **All typos fixed**
- **Bugs Patched**
- **Most comments changed to doc strings**
- **Log mode | w ---> a**
- **emojis tuple is in a new file called emojis.py**
- **Imports sorted**
- **More branches**
- **Member intents enabled** this is for adding/removing onboarding commands
- **Removed /outhis command**
- **Error handling for /dm and /say**
- **Checks if token is none**
- **Better command names**
- **14 new poll reactions**

> **This update was mainly focused on patching bugs. Update 0.5 will add a lot more commands. Update 0.5 is aimed to come out before September and is currently in development!**

---

# Update 0.3

## **OutBot - Update - 22nd July 2026**

### **Version 0.3**

- **Slash commands added.** (/obhelp or do !obhelp)
- **New prefixes:** !, ?, -,  =,  ;
- **OutBot's code is now on GItHub** = https://github.com/Mythordian-py/OutBot
- **Logging change | a ---> w**
- **Prefix reply command now replies with:** Hello <@mention>! How are you!
- **Bug fixes**
- **Typos fixed**
- **Removed censor filter**
- **More readable comments**
- **Better command names**
- **More readable code**
- **Description change:** GItHub link added

> **All updates can be found in OutMyth's Discord server in the channel "bot-updates" and "dev-notes".**

**OutMyth Discord Server:** https://discord.gg/Sc5vAvTJtc

---


# OutBot - Update - 19th July 2026

### **Version 0.2**

- **Name change** Outmyth Ai ---> OutBot
- **Description added**
- **Out Bot's will be on GitHub in the couple of days days.**
- **Command Prefix is**  '/' (**Update 0.3 will add !**)
- **Swear word filter** - I will add all censored words in update 0.3 - Currently if you say the words in the screenshot, it will delete your message and ping you. "@{user} - Don't say that word!"
- **Bot Commands Added** - /hello ,/outmyth ,/outmyth_history ,/dm /poll ,/bot_help,. Again more commands will be added in update 0.3 and the following updates. If you want to know what each command does, type /help in #🤖┃chatbot or #💻┃commands . Or you can read the code once it's on GitHub.
- **All bot commands work in the bot's Dms.**

---

# OutBot - Update - 12th July 2026

## **Version: 0.1**

- **Responds when /outmyth is used.**
