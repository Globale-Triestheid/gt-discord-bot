import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix="!")
blocked_extensions = {"example"}


@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")


@client.event
async def on_ready():
    print("Bot initiated")

if __name__ == "__main__":
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and filename[:-3] not in blocked_extensions:
            client.load_extension(f"cogs.{filename[:-3]}")

    client.run(os.getenv("TOKEN"))
