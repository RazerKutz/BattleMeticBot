import config
import requests
from io import BytesIO
from PIL import Image
from urllib.request import urlretrieve
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

    response = requests.get("http://cache.gametracker.com/server_info/108.61.118.183:2302/b_560_95_1.png")
    pic = Image.open(BytesIO(response.content))

    pic.save("pic.png")
    # print(testImage)
    await client.upload("pic.png")

client.run(TOKEN)