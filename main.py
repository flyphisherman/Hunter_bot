# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('DISCORD_GUILD_ID')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.id == GUILD_ID:
            break

    print(f'{client.user} has connected to Discord!')
    print(f'{guild.name}(id: {guild.id})\n')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'A wild bird appears!' in message.content:
        response = '$bang'
        await message.channel.send(response)


client.run(TOKEN)