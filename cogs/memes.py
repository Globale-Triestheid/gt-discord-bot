import discord
from discord.ext import commands
from PIL import Image, ImageEnhance
from io import BytesIO
from bot_logic import get_image


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
        await ctx.message.add_reaction(u"\U0001F595")

        img = await get_image(ctx, user)

        if isinstance(img, str):
            await ctx.send(img)
            return

        wth_image = Image.open("images/wth.jpg")

        img = img.resize((130, 130))

        # pastes users pfp inside the wth image
        wth_image.paste(img, (41, 41))
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
        await ctx.message.add_reaction(u"\U0001F595")

        img = await get_image(ctx, user)

        if isinstance(img, str):
            await ctx.send(img)
            return

        keemstar_image = Image.open("images/keemstar.jpg")

        keemstar_image = keemstar_image.resize((128, 128))
        keemstar_image = keemstar_image.convert("RGB")

        img = img.resize((512, 512))
        img = img.convert("RGB")
        img.paste(keemstar_image, (0, 0))
        img.save("images/profile_keemstar.jpg")

        await ctx.send(file=discord.File("images/profile_keemstar.jpg"))

    @commands.command()
    async def wasted(self, ctx, user: discord.Member = None):
        """
        Returns a profile picture with the GTA "wasted"
        ctx: original message
        user: (optional) tagged user
        """
        await ctx.message.add_reaction(u"\U0001F595")

        img = await get_image(ctx, user)

        if isinstance(img, str):
            await ctx.send(img)
            return

        wasted_image = Image.open("images/wasted.jpg")

        width, height = img.size
        width2, height2 = wasted_image.size

        change_factor = width / width2

        wasted_image = wasted_image.resize((width, int(height2 * change_factor)))

        enhancer = ImageEnhance.Brightness(img)

        factor = 0.5  # darkens the image
        img = enhancer.enhance(factor)

        img.paste(wasted_image, (0, int(height / 2)))

        img.save("images/profile_wasted.jpg")

        await ctx.send(file=discord.File("images/profile_wasted.jpg"))

    @commands.command()
    async def whodidthis(self, ctx, user: discord.Member = None):
        """
        returns an image with the who did this? meme
        ctx: original message
        user: (optional) tagged user
        """
        await ctx.message.add_reaction(u"\U0001F595")

        img = await get_image(ctx, user)

        if isinstance(img, str):
            await ctx.send(img)
            return

        whodidthis_image = Image.open("images/whodidthis.jpg")

        img = img.resize((662, 662))

        whodidthis_image.paste(img, (103, 134))

        whodidthis_image.save("images/profile_whodidthis.jpg")

        await ctx.send(file=discord.File("images/profile_whodidthis.jpg"))

    @commands.command()
    async def brazzers(self, ctx, user: discord.Member = None):
        """
        Adds brazzers logo to the bottom right corner.
        :param ctx:
        :param user:
        :return:
        """
        await ctx.message.add_reaction(u"\U0001F595")

        img = await get_image(ctx, user)

        if isinstance(img, str):
            await ctx.send(img)
            return

        brazzers_image = Image.open("images/brazzers.png")

        # dimenties van beide plaatjes krijgen
        width, height = img.size
        width2, height2 = brazzers_image.size

        # nieuwe breedte van het plaatje moet 2,5 keer zo klein zijn als het originele plaatje,
        # dus hier bereken je hoeveel pixels het brazzers logo wordt in de breedte
        new_width = width / 2.5
        # de factor is keer hoeveel je de breedte moet doen om het plaatje zoveel pixels breed te maken
        factor = new_width / width2
        # resize, breedte en hoogte worden bepaald door de originele grootte keer de factor te doen
        brazzers_image = brazzers_image.resize((int(width2 * factor), int(height2 * factor)))
        width2, height2 = brazzers_image.size
        # logo wordt geplakt op hoogte van zichzelf zodat de onderkant precies de grond raakt (dus totale hoogte min zn eigen hoogte)
        img.paste(brazzers_image, (0, height - height2))
        img.save("images/brazzers_profile.jpg")

        await ctx.send(file=discord.File("images/brazzers_profile.jpg"))



def setup(client):
    client.add_cog(Memes(client))
