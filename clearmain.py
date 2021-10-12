from os import name
import discord
from discord.ext import commands

Bot = commands.Bot(command_prefix='!')

@Bot.event
async def on_ready():
    await Bot.change_presence(activity=discord.Game(name='!help'))
    print("I'm Ready!")

@Bot.command()
async def clear(ctx, amount = 5):
    # @commands.has_role("roleName") Only "roleName" use this 'clear' command
    await ctx.channel.purge(limit=amount)

Bot.run() #Bot.run(Discord bot TOKEN)