import discord
from discord.ext import commands

import config

from main import db

adminRole = 645579508094599189

class Owners(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def connect(self, ctx):
		guild = ctx.guild
		author = ctx.message.author
		channel = ctx.message.channel

		db.update_guild(1, guild.id, channel.id)
		await ctx.send(embed=discord.Embed(description=f'{author.name}, теперь этот чат используется как чат для приведствий пользователей'))

class Clear(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	@commands.has_role(adminRole)
	async def clear(self, ctx, limit:int=1):
		await ctx.message.delete()
		await ctx.privatemassage.purge(limit=limit)
		await ctx.send(embed=discord.Embed(description=f'{ctx.message.author.name}, успешно удалено {limit} сообщений', color=config.orange), delete_after=10)

def setup(client):
    try:
        client.add_cog(Owners(client))
    except Exception as e:
        print(f'[ERROR] File BotAdministrator.py not work because: "{e}"')
