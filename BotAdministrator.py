import discord
from discord.ext import commands

import config

from main import db

class Owners(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	@commands.is_owner()
	async def db(self, ctx, nameTable:str):
		author = ctx.message.author
		data = db._select_all(nameTable)
		embed = discord.Embed(title=f'{author.name} таблица {nameTable}')
		for a in data:
			embed.add_field(name=f'ID: **{a[0]}**', value=f'1. {a[1]}\n2. {a[2]}\n3. {a[3]}\n4. {a[4]}\n5. {a[5]}\n')
		await ctx.send(embed=embed)

class Verification(commands.Cog):
	def __init__(self, client):
		self.client = client

		self.allguildid = []

	def LenGuilds(self):
		self.allguildid = []
		data = db._select_all('guild')

		for a in data:
			self.allguildid.append(a[1])

		print(self.allguildid)

	@commands.command(aliases = ["Verification", "Верификация", "верификация"])
	@commands.has_permissions(administrator=True)
	async def verification(self, ctx, command=None, value=None):
		author = ctx.message.author
		command = command.lower()

		if command == None:
			await ctx.send(embed=discord.Embed(description=f'{author.name}, вы забыли написать команду!', color=config.orange))

		elif command == 'group' or command == 'группы':
			guild = ctx.guild
			if guild.id != self.allguildid:
				db.insert_guild(1, guild.id, guild.name)
				await ctx.send(embed=discord.Embed(description=f'{author.name}, эта группа была успешно верифицированая', color=config.orange))

			else:
				await ctx.send(embed=discord.Embed(description=f'{author.name}, к сожелению эта группа уже верифицирования.', color=config.orange))

		else:
			await ctx.send(embed=discord.Embed(description=f'{author.name}, неизвесная команда!', color=config.orange))

	@commands.command(aliases = ["Connect", "Подключение", "подключение"])
	@commands.has_permissions(administrator=True)
	async def connect(self, ctx):
		guild = ctx.guild
		author = ctx.message.author
		channel = ctx.message.channel

		db.update_guild(1, guild.id, channel.id)
		await ctx.send(embed=discord.Embed(description=f'{author.name}, теперь этот чат используется как чат для приведствий пользователей', color=config.orange))
		
def setup(client):
    try:
        client.add_cog(Owners(client))
        client.add_cog(Verification(client))
    except Exception as e:
        print(f'[ERROR] File BotAdministrator.py not work because: "{e}"')
