import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix=config.prefix,intents=discord.Intents().all())
bot.remove_command("help")

bot.run(os.environ['TOKEN'])
