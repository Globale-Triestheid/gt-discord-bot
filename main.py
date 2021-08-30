import discord
from discord.ext import commands
import os
import requests
from webscraper import Fryer
from time import sleep

from PIL import Image, ImageEnhance
from io import BytesIO

client = commands.Bot(command_prefix="!")


@client.command()
async def wth(ctx, user: discord.Member = None):
    """
    Returns the "worse than Hitler" image with somebodies profile picture inside.
    ctx: original message
    user: (optional) tagged user
    """

    # if no user parameter is specified, the OP gets used as user.
    if not user:
        user = ctx.author

    print(user)

    wth_image = Image.open("images/wth.jpg")

    asset = user.avatar_url_as(size=128)

    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((130, 130))

    # pastes users pfp inside the wth image
    wth_image.paste(pfp, (41, 41))
    wth_image = wth_image.convert("RGB")
    wth_image.save("images/profile_wth.jpg")

    await ctx.send(file=discord.File("images/profile_wth.jpg"))


@client.command()
async def deepfry(ctx, user: discord.Member = None):
    """
    Returns a deepfried image of a profile picture or a referenced image.
    ctx: original message
    user: (optional) tagged user
    """

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
    img.save("images/deepfry.jpg")
    path = os.path.dirname(os.path.realpath('images/deepfry.jpg')) + "\deepfry.jpg"
    print(path)
    Fryer().deepFry(image_url=path)
    await ctx.send(file=discord.File("images/deep_img.png"))


@client.command()
async def keemstar(ctx, user: discord.Member = None):
    """
    Returns an image with keemstar in the top left.
    ctx: original message
    user: (optional) tagged user
    """

    if not user:
        user = ctx.author

    print(user)

    keemstar_image = Image.open("images/keemstar.jpg")

    asset = user.avatar_url_as(size=512)

    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    keemstar_image = keemstar_image.resize((128, 128))
    keemstar_image = keemstar_image.convert("RGB")
    pfp = pfp.resize((512, 512))
    pfp = pfp.convert("RGB")
    pfp.paste(keemstar_image, (0, 0))
    pfp.save("images/profile_keemstar.jpg")

    await ctx.send(file=discord.File("images/profile_keemstar.jpg"))


@client.command()
async def wasted(ctx, user: discord.Member = None):
    """
    Returns a profile picture with the GTA "wasted"
    ctx: original message
    user: (optional) tagged user
    """
  
    if not user:
        user = ctx.author

    print(user)

    wasted_image = Image.open("images/wasted.jpg")

    asset = user.avatar_url_as(size=512)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    enhancer = ImageEnhance.Brightness(pfp)

    factor = 0.5  # darkens the image
    pfp = enhancer.enhance(factor)

    pfp.paste(wasted_image, (0, 200))


    pfp.save("images/profile_wasted.jpg")

    await ctx.send(file=discord.File("images/profile_wasted.jpg"))

@client.command()
async def whodidthis(ctx, user: discord.Member = None):
    """
    returns an image with the who did this? meme
    ctx: original message
    user: (optional) tagged user
    """

    if not user:
        user = ctx.author

    print(user)

    whodidthis_image = Image.open("images/whodidthis.jpg")

    asset = user.avatar_url_as(size=512)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((662, 662))

    whodidthis_image.paste(pfp, (103, 134))

    pfp.save("profile_whodidthis.jpg")

    await ctx.send(file=discord.File("profile_whodidthis.jpg"))


client.run(os.getenv("TOKEN"))

