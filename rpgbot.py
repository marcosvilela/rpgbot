import discord
from discord.ext import commands
import random
import os
import token


'''

This is the main Bot file. It loads all commands based on Cogs, sets up
all the command prefixes and runs the bot itself.

'''

#### BOT CONSTANTS #####

bot_prefix = ("$")
#I'll comment the bot_token line since I'm importing it from an untracked file. What you should do is uncomment the line below
#and paste your bot token right there
#bot_token = ""
bot_token = token.bot_token

client = commands.Bot(command_prefix=bot_prefix)

#### On ready status changes
@client.event
async def on_ready():
	print('Bot is ready!')

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
