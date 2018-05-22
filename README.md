# PythonTwitchBotFramework
working twitchbot framework made in python 3.6+

#basic info
This is a fully async twitch bot framework complete with:

* builtin command system using decorators
* overridable events (message received, whisper received, ect)
* full permission system that is individual for each channel
* message timers 
* quotes 
* custom commands
* builtin economy 


# quick start

the minimum code to get the bot running is this:
```python
import asyncio
from twitchbot.bots import BaseBot

async def main():
    bot = await BaseBot.create()
    await bot.start()

asyncio.get_event_loop().run_until_complete(main())

```

this will start the bot. 

if this is the first time running the bot it will generate a folder
named `configs`. 

inside is `config.json` which you put the authentication into

as the bot is used it will also generate channel permission files 
in the `configs` folder

# adding your own commands

to register your own commands use the Command decorator:

* using decorators
```python
from twitchbot import Command

@Command('COMMAND_NAME')
async def cmd_function(msg, *args):
    await msg.reply('i was called!')

```


# config

the default config values are:
```json
{
  "oauth": "oauth:",
  "client_id": "CLIENT_ID",
  "nick": "nick",
  "prefix": "!",
  "default_balance": 200,
  "owner": "BOT_OWNER_NAME",
  "channels": [
    "channel"
  ]
}

```

`oauth` is the twitch oauth used to login

`client_id` is the client_id used to login to from the TwitchAPI

`nick` is the twitch accounts nickname

`prefix` is the command prefix the bot will use for commands that 
dont use custom prefixes

`default_balance `is the default balance for new users that dont
already have a economy balance

`owner` is the bot's owner

`channels` in the twitch channels the bot will join