import discord
from discord.ext import commands


class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Example online")

    # Commands
    @commands.command()
    async def kanker(self, ctx):
        await ctx.send("KANKER")


def setup(client):
    client.add_cog(Example(client
