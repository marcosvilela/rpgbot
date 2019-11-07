import discord
import random
from discord.ext import commands
import re


class Roller(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(brief='Rolagem de ataque (d20 + Precisão')
	async def rollatk(self, ctx, dice, prec):
		if((re.match(r'd(\d)', dice)) != None):
			dice_sides = dice.replace('d','')
			diceresult = random.randint(1, int(dice_sides))
			finalresult = diceresult + int(prec)
			msg = str(ctx.message.author.name) + ' rolou um ' + dice + ' para tentar atacar com resultado: ' + str(finalresult) + ' (' + str(diceresult) + '+' + str(prec) + ')' + '\n'
			await ctx.send(msg)
		else:
			await ctx.send("Argumentos inválidos, role novamente!")

	@commands.command(brief='Rolagem de defesa (d20 + Agilidade)')
	async def rolldef(self, ctx, dice, agil):
		if((re.match(r'd(\d)', dice)) != None):
			dice_sides = dice.replace('d','')
			diceresult = random.randint(1, int(dice_sides))
			finalresult = diceresult + int(agil)
			msg = str(ctx.message.author.name) + ' rolou um ' + dice + ' para tentar defender com resultado: ' + str(finalresult) + ' (' + str(diceresult) + '+' + str(agil) + ')' +'\n' 
			await ctx.send(msg)
		else:
			await ctx.send("Argumentos inválidos, role novamente!")

	@commands.command(brief='Rolagem de dano (d20 + Força/Sabedoria)')
	async def rolldmg(self, ctx, dice, modifier):
		if((re.match(r'd(\d)', dice) != None)):
			dice_sides = dice.replace('d','')
			result = random.randint(1, int(dice_sides))
			dmg = result + int(modifier)
			msg = str(ctx.message.author.name) + ' rolou um ' + dice + ' para causar ' + str(dmg) + ' (' + str(result) + '+' + str(modifier) +')' + ' de dano'
			await ctx.send(msg)
		else:
			await ctx.send("Argumentos inválidos, role novamente!")


def setup(client):
	client.add_cog(Roller(client))