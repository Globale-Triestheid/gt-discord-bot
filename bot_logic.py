import discord
from discord.ext import commands
import os
import requests
from webscraper import Fryer
from time import sleep

from PIL import Image, ImageEnhance
from io import BytesIO


async def check_reference(ctx):
    try:
        ref_message = await ctx.fetch_message(ctx.message.reference.message_id)
    except AttributeError:
        return False

    if len(ref_message.attachments) == 0:
        return False

    if not ref_message.attachments[0].url.endswith((".jpg", ".png", ".jpeg")):
        return False

    return True


async def get_image_from_url(url):
    res = requests.get(url)
    return Image.open(BytesIO(res.content))


async def get_image_from_user(user, size):
    asset = user.avatar_url_as(size=size)
    return Image.open(BytesIO(await asset.read()))
