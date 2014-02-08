import json
import os
from thealot import TheAlot

config = {
    "server"    : "irc.quakenet.org",
    "port"      : 6667,
    "channel"   : "#TheAlot",
    "nickname"  : "HerokuAlot",
    "prefix"    : "!",
    "database"  : os.getenv("DATABASE_URL"),
    "plugins"   : [
        "quote",
        "links",
        "alot",
        "excuse",
    ]
}

with open('config.json', 'w') as f:
    json.dump(config, f)

bot = TheAlot()
bot.start()
