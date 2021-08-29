import discord
from discord.ext import commands
# import datetime
# import asyncio
# import random
import os

from PIL import Image
from io import BytesIO

client = commands.Bot(command_prefix="!")


@client.command()
async def wth(ctx, user: discord.Member = None):
    if not user:
        user = ctx.author

    print(user.nick)

    wanted_image = Image.open("wth.jpg")

    asset = user.avatar_url_as(size=128)

    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((130, 130))

    wanted_image.paste(pfp, (41, 41))
    wanted_image = wanted_image.convert("RGB")
    wanted_image.save("profile.jpg")

    await ctx.send(file=discord.File("profile.jpg"))

client.run(os.getenv("TOKEN"))
