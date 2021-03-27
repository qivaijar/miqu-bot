# miqu-bot
Experimental discord bot

## Setup:

Install required packages by running the command below:
```bash
git clone <https://github.com/qivaijar/miqu-bot.git>
$ cd miqu-bot
$ pip install -r requirements.txt
```
## add ".env" file

create ".env" file and add credential information 

```python
# .env file
bot_token = <bot-token>           
guild_name = <your-guild-name>    # e.g.  'my guild'
```

## Available commmands
- Below are the commands available when using the bot, triggered using `mq` (e.g. `mqg`, `mqgim`, ...)
- Commands also can be seen by typing `mqhelp` when using the bot.

### General
| command | description |
| ------- | ----------- |
|    g    |  Returns google search result |
|   gim   |  Returns google image search result |
|   roll  |  Returns random number from 1 to 100 |
|  typed  |  Returns typed massage |

### Music:
| command | description |
| ------- | ----------- |
|  join   |  Joins a voice channel |
|  pause  |  Pauses an audio stream |
|  play   |  Plays a file from the local filesystem |
|  resume |  Resumes the audio stream |
|  stop   |  Stops and disconnects the bot from voice |
|  stream |  Streams music from search terms) |
|  volume |  Adjusts the player's volume |

## Contributors:
These people helped in the development process of this bot

[@qivaijar](https://github.com/qivaijar)<br />
[@gilang](https://github.com/gilangp1)<br />
[@darmawan](https://github.com/Rusian971)
