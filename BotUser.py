import discord
from discord.ext import commands

from main import db

import config

class Sentence(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases = ["предложение", "Sentence", "Предложение"])
	async def sentence(self, ctx, *, arg = None): # Создает команду
		author = ctx.message.author
		if arg == None:
			await ctx.send(embed=discord.Embed(description=f'{author.name}, вы забыли написать текст.', color=config.orange), delete_after=30) # Отправляет сообщение в чат
		else:
			await ctx.message.add_reaction('✅') # Добавляет лайк
			await ctx.message.add_reaction('❎') # Добавляет дизлайк
			await ctx.send(embed=discord.Embed(description=f'{author.name}, спасибо за вашу идею.', color=config.orange), delete_after=30) # Отправляет сообщение в чат

class Request(commands.Cog):
	def __init__(self, client):
		self.client = client

		self.LenRequest = 0
		self.isStart = False

	@commands.command()
	async def request(self, ctx, *, arg=None):
		author = ctx.message.author
		if self.isStart:
			pass
		elif not self.isStart:
			await ctx.channel.purge(limit=1)
			await ctx.send(embed=discord.Embed(description=f'{author.name}, извените но сейчас заявки не принимаются! :D', color=config.orange))
			embed = discord.Embed(title=f'Заявка {author.name}', description=arg)
			embed.add_field(name='**Что случилось с заявкой?**', value='Сейчас заявки не принимаются,\nи я скинул Вам вашу заявку чтобы вы не писали ее ещё раз =D', inline=True)
			await author.send(embed=embed)

	@commands.command()
	async def arequest(self, ctx, command, value):
		author = ctx.message.author
		if command == 'start' or command == 'старт':
			self.isStart = True
		elif command == 'stop' or command == 'стоп':
			self.isStart = False

class User(commands.Cog):
	def __init__(self, client):
		self.client = client

		self.users = []

	def LenUsers(self):
		data = db._select_order_by('users', 'id')
		for a in data:
			self.users.append(a[1])

	@commands.command(aliases = ["User", "Юзер", "юзер"])
	async def user(self, ctx, member: discord.Member = None):
		users = None
		author = ctx.message.author
		self.LenUsers()
		if member == None:
			users = author
		elif member != None:
			users = member

		if str(users) in self.users:
			""" Parametrs """
			data = db.select_where('users', 'user', str(users))[0]
			status = data[2]
			money = data[3]

			embed = discord.Embed(title=f'Пользователь {users.name}', color=config.orange)
			embed.add_field(name='Статус пользователя',value=f'Статус {users.status}',inline=True)

			if status == 0:
				embed.add_field(name=f'VIP статус: ', value=f'{users.name} не имеет статус VIP', inline=True)
			elif status == 1:
				embed.add_field(name=f'VIP статус: ', value=f'{users.name} имеет статус VIP', inline=True)
			elif status == 2:
				embed.add_field(name=f'VIP статус: ', value=f'{users.name} имеет статус Super VIP', inline=True)

			embed.set_footer(text=f"Все права на бота пренадлежат: {config.BOT_AUTHOR}") # Подвал сообщения
			await ctx.send(embed=embed)
		else:
			embed = discord.Embed(title=f'Пользователь {users.name}', color=config.orange)
			embed.add_field(name='Статус пользователя',value=f'Статус {users.status}',inline=True)
			embed.set_footer(text=f"Все права на бота пренадлежат: {config.BOT_AUTHOR}") # Подвал сообщения
			await ctx.send(embed=embed)

class Economy(commands.Cog):
	def __init__(self, client):
		self.client = client

		self.users = []

	def LenUsers(self):
		self.users = []
		data = db._select_order_by('users', 'id')
		for a in data:
			self.users.append(a[1])

	# Перевод денег
	@commands.command()
	async def pay(self, ctx, member: discord.Member):
		pass

	@commands.command()
	async def createwallet(self, ctx):
		self.LenUsers()
		author = ctx.message.author
		print(author)
		if str(author) in self.users:
			db.insert_users(1, author, None, None)
			await ctx.send(embed=discord.Embed(description=f'{author.name}, ваш профиль был успешно прокачан. =D', color=config.orange))
		else:
			await ctx.send(embed=discord.Embed(description=f'{author.name}, ваш профиль уже был прокачан. =D', color=config.orange))

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def aeconomy(self, ctx, command:str=None, value:str=None):
		pass


def setup(client):
	try:
		client.add_cog(Sentence(client))
		client.add_cog(User(client))
	except Exception as e:
		print(f'[ERROR] File BotUser.py not work because: "{e}"')