import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    # Avoid bot replying to itself
    if message.author == client.user:
        return

    # Check if the message is a direct message
    if isinstance(message.channel, discord.DMChannel):
        await message.channel.send(f'You said: {message.content}')

client.run(TOKEN)
