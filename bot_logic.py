import discord
from discord.ext import commands
import os
import requests
from webscraper import Fryer
from time import sleep
import datetime

from PIL import Image, ImageEnhance
from io import BytesIO


async def get_image(ctx, user: discord.Member = None):
    """
    1. Als er een image bij het bericht word gestuurd pakt hij die
    2. Als er gereageerd word op een afbeelding dan pakt hij die
    3. Als er een tag van een Member word genoemd pakt hij de avatar
    4. Als er niks achter de command staat pakt hij de laaste afbeelding in dat kanaal
    """
    if len(ctx.message.attachments) > 0:
        return await get_image_from_url(ctx.message.attachments[0])
    elif await check_reference(ctx):
        ref_message = await ctx.fetch_message(ctx.message.reference.message_id)
        url = ref_message.attachments[0].url
        return await get_image_from_url(url)
    elif user:
        return await get_image_from_user(user)
    else:
        image = await get_newest_image(ctx)
        if isinstance(image, discord.Message):
            return await get_image_from_url(image.attachments[0].url)

    return "No image found"



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


async def get_image_from_user(user, size=512):
    asset = user.avatar_url_as(size=size)
    return Image.open(BytesIO(await asset.read()))


async def get_newest_image(ctx):
    messages = await ctx.channel.history(limit=100).flatten()

    images = []
    for message in messages:
        if check_image(message):
            images.append(message)

    newest_time = max(image.created_at for image in images)

    for image in images:
        if image.created_at == newest_time:
            return image

    return False


def check_image(message):
    if len(message.attachments) > 0 and message.attachments[0].url.endswith((".jpg", ".png", ".jpeg")):
        return True
    return False
