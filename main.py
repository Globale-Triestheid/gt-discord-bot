import discord
from discord.ext import commands
# import datetime
# import asyncio
# import random
import os

from PIL import Image, ImageEnhance
from io import BytesIO

client = commands.Bot(command_prefix="!")

@client.command()
async def wth(ctx, user: discord.Member = None):
    if not user:
        user = ctx.author

    print(user)

    wanted_image = Image.open("wth.jpg")

    asset = user.avatar_url_as(size=128)

    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((130, 130))

    wanted_image.paste(pfp, (41, 41))
    wanted_image = wanted_image.convert("RGB")
    wanted_image.save("profile.jpg")

    await ctx.send(file=discord.File("profile.jpg"))


@client.command()
async def keemstar(ctx, user: discord.Member = None):
    if not user:
        user = ctx.author

    print(user)

    keemstar_image = Image.open("keemstar.jpg")

    asset = user.avatar_url_as(size=512)

    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    keemstar_image = keemstar_image.resize((128, 128))
    keemstar_image = keemstar_image.convert("RGB")
    pfp.paste(keemstar_image, (0, 0))

    pfp.save("profile_keemstar.jpg")

    await ctx.send(file=discord.File("profile_keemstar.jpg"))


@client.command()
async def wasted(ctx, user: discord.Member = None):
    if not user:
        user = ctx.author

    print(user)

    wasted_image = Image.open("wasted.jpg")

    asset = user.avatar_url_as(size=512)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    enhancer = ImageEnhance.Brightness(pfp)

    factor = 0.5  # darkens the image
    pfp = enhancer.enhance(factor)

    wasted_image = Image.open("wasted.jpg")

    pfp.paste(wasted_image, (0, 200))


    pfp.save("profile_wasted.jpg")

    await ctx.send(file=discord.File("profile_wasted.jpg"))




client.run(os.getenv("TOKEN"))

