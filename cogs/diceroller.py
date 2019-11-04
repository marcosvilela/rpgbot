import discord
import random
from discord.ext import commands
import re

class Roller(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print('Bot is ready!')
	
	@commands.command(brief='rolls a specified dice')
	async def roll(self, ctx, dice):
		if(re.match(r'd(\d)', dice) != None):
			dice_sides = dice.replace('d','')
			result = random.randint(1, int(dice_sides))
			msg = str(ctx.message.author.name) + ' rolled a '+ dice + ' with result: ' + str(result)
			await ctx.send(msg)

			if(result == int(dice_sides)):
				await ctx.send('\nCritical success!')

			if(result == 1):
				await ctx.send('\nCritical failure!')
		else:
			await ctx.send("Invalid argument! Try again!")


def setup(client):
	client.add_cog(Roller(client))