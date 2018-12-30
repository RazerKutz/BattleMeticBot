import config
import discord
from discord.ext import commands

TOKEN = config.app_token
BOT_PREFIX = "!"
client = commands.Bot(command_prefix=commands.when_mentioned_or(BOT_PREFIX))

@client.event
async def on_ready():
    print ("Logged in as")
    print (client.user.name)
    print (client.user.id)
    print ("------")


@client.command(pass_context=True)
async def status(ctx, stuff=""):
    """Send Status"""
    await client.say("https://is.gd/03OmvF")

client.run(TOKEN)