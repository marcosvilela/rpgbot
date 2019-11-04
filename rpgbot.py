import discord
from discord.ext import commands
import random
import os


'''

This is the main Bot file. It loads all commands based on Cogs, sets up
all the command prefixes and runs the bot itself.

'''

#### BOT CONSTANTS #####

bot_prefix = ("$", "=", ".")
bot_token = ""

client = commands.Bot(command_prefix=bot_prefix)

#### On ready status changes

@client.event()
async def on_ready():
	await client.change_presence(status=discord.Status.idle, activity=discord.Game('Online and working!'))

#### Cogs loading methods

@client.command()
async def load(ctx, extension):
	print("Load cog!")
	client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
	print("Unload cog!")
	client.unload_extension(f'cogs.{extension}')


##### Locally running the Bot code and loading every cog available

for filename in os.listdir('./cogs'):
	if(filename.endswith('.py')):
		client.load_extension(f'cogs.{filename[:-3]}')

client.run(bot_token)
