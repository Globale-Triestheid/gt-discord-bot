import discord
from discord.ext import commands
from PIL import Image, ImageEnhance
from io import BytesIO


class Memes(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Memes online")

    # Commands
    @commands.command()
    async def wth(self, ctx, user: discord.Member = None):
        """
            Returns the "worse than Hitler" image with somebodies profile picture inside.
            ctx: original message
            user: (optional) tagged user
            """

        # if no user parameter is specified, the OP gets used as user.
        if not user:
            user = ctx.author

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

    @commands.command()
    async def keemstar(self, ctx, user: discord.Member = None):
        """
            Returns an image with keemstar in the top left.
            ctx: original message
            user: (optional) tagged user
            """

        if not user:
            user = ctx.author

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

    @commands.command()
    async def wasted(self, ctx, user: discord.Member = None):
        """
        Returns a profile picture with the GTA "wasted"
        ctx: original message
        user: (optional) tagged user
        """

        if not user:
            user = ctx.author

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

    @commands.command()
    async def whodidthis(self, ctx, user: discord.Member = None):
        """
        returns an image with the who did this? meme
        ctx: original message
        user: (optional) tagged user
        """

        if not user:
            user = ctx.author

        whodidthis_image = Image.open("images/whodidthis.jpg")

        asset = user.avatar_url_as(size=512)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((662, 662))

        whodidthis_image.paste(pfp, (103, 134))

        pfp.save("images/profile_whodidthis.jpg")

        await ctx.send(file=discord.File("images/profile_whodidthis.jpg"))


def setup(client):
    client.add_cog(Memes(client))
