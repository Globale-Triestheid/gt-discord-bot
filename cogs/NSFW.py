import discord
from discord.ext import commands
from webscraper import NSFWWebscraper


class NSFW(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("NSFW online")

    # I'm not proud of this one
    @commands.command()
    async def rule34(self, ctx, *args):

        await ctx.message.add_reaction(u"\U0001F595")

        if not ctx.channel.is_nsfw():
            await ctx.send("This command can only be used in NSFW channels")
            return

        search = " ".join(args[:])
        scraper = NSFWWebscraper()
        try:
            link, url = scraper.get_rule34(search)
        except ValueError:
            scraper.close_window()
            await ctx.send("No images found!")
            return

        scraper.close_window()

        embed = discord.Embed()
        embed.description = f"[source]({url})"

        await ctx.send(link)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(NSFW(client))
