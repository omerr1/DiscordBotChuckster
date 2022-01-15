# bot.py
import os
import random
from discord.ext import commands
import random
import requests
import json
from types import SimpleNamespace
from os.path import exists


import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name="joke",help = "Tells a random Chuck Norris joke, add query for a specific joke")
async def joke(ctx,text=""):

        if len(text) > 0:
            #Based on query
            q = text
            response = jokes_bases_on_query(q)
        else:
            response = get_random_joke()

        await ctx.send(response)



def get_random_joke():
    url = "https://api.chucknorris.io/jokes/random"
    val = requests.get(url)

    if val.ok:
        x = json.loads(val.text, object_hook=lambda d: SimpleNamespace(**d))
        return (x.value)
    else:
        return ("Chucky is out of jokes now, try later!")

def jokes_bases_on_query(query):
    url = "https://api.chucknorris.io/jokes/search?query="
    val = requests.get(url + query)

    if val.ok:
        x = json.loads(val.text, object_hook=lambda d: SimpleNamespace(**d))
        return x.result[random.randrange(x.total)].value
    else:
        if query == "" or query == " ":
            query = "blank"
        return "Chucky doesnt believe in '" + query + "' pick another subject"

bot.run(TOKEN)