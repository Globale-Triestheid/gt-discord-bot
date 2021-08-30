import discord
from discord.ext import commands
import os
import requests

from webscraper import Fryer
from bot_logic import get_image

from PIL import Image
from io import BytesIO


class Manipulate(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Image manipulation online")

    # Commands
    @commands.command()
    async def deepfry(self, ctx, user: discord.Member = None):
        await ctx.message.add_reaction(u"\U0001F595")

        img = await get_image(ctx, user)

        if isinstance(img, str):
            await ctx.send(img)
            return

        img = img.convert("RGB")
        img.save("images/deepfry.jpg")
        path = os.path.dirname(os.path.realpath('images/deepfry.jpg')) + "\deepfry.jpg"
        Fryer().deepFry(image_url=path)
        await ctx.send(file=discord.File("images/deep_img.png"))


def setup(client):
    client.add_cog(Manipulate(client))
