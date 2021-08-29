import discord
from discord.ext import commands
# import datetime
# import asyncio
# import random
import os
import requests
from webscraper import Fryer
from time import sleep

from PIL import Image
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
async def deepfry(ctx, user: discord.Member = None):
    print(ctx.message.reference)
    await ctx.message.add_reaction(u"\U0001F595")

    if not user:
        if not ctx.message.reference:
            await ctx.send("Pls reply to an image to deepfry with this command")
            return

        ref_message = await ctx.fetch_message(ctx.message.reference.message_id)

        if not ref_message.attachments:
            await ctx.send("Pls reply to an image to deepfry with this command")
            return

        print(ref_message.attachments[0].url)
        url = ref_message.attachments[0].url

        if not url.endswith((".jpg", ".png", ".jpeg")):
            await ctx.send("Pls reply to an image to deepfry with this command")
            return

        res = requests.get(url)
        img = Image.open(BytesIO(res.content))
    else:
        asset = user.avatar_url_as(size=512)

        data = BytesIO(await asset.read())
        img = Image.open(data)

    img = img.convert("RGB")
    img.save("deepfry.jpg")
    path = os.path.dirname(os.path.realpath('deepfry.jpg')) + "\deepfry.jpg"
    print(path)
    Fryer().deepFry(image_url=path)
    await ctx.send(file=discord.File("deep_img.png"))

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



client.run(os.getenv("TOKEN"))
