import discord
from discord.ext import commands

from random import randint, choice

from asyncio import sleep as timer

from main import db

import config

class RanbowRole(object):
	def __init__(self, client):
		self.client = client

class Raffle(commands.Cog):
	def __init__(self, client):
		self.client = client

		self.startRaffle = False
		self.raffle = []

	@commands.command(aliases = ["Розыгрыш", "розыгрыш"])
	async def raffle(self, ctx): # Создает команду
		print(self.raffle)
		author = ctx.message.author
		if self.startRaffle:
			if author != self.raffle:
				self.raffle.append(author)
				player_raffle = len(self.raffle)
				embed = discord.Embed(title='Розыгрыш!', color=config.orange)
				embed.add_field(name='Спасибо!',value='Вы были добавлены в список участников розыгрыша!',inline=True)
				embed.add_field(name=f'Список участников.', value=f'В списке участников находиться {player_raffle} участник(ков) розыгрыша.')
				embed.set_footer(text=f"Все права на бота пренадлежат: {config.BOT_AUTHOR}")
				await author.send(embed=embed)
				await ctx.send(embed=discord.Embed(description=f'{author.name}, Вы были успешно добавлены в розыгрыш', color=config.orange))
			else:
				await ctx.send(embed=discord.Embed(description=f'{author.name}, вы уже есть в списке участников розыгрыша!', color=config.red))
			
		else:
			await ctx.send(embed=discord.Embed(description=f'{author.name}, сейчас не проводится не какие розыгрыши', color=config.orange))

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def araffle(self, ctx, command:str=None, value:str=None):
		author = ctx.message.author
		if command == 'activate':
			self.startRaffle = True
			await ctx.send(embed=discord.Embed(description=f'{author.name}, запустил розыгрыш!!', color=config.orange))

		elif command == 'start':
			if self.startRaffle:
				len_raffle = len(self.raffle)
				winner = choice(self.raffle)
				# Сообщение
				embed = discord.Embed(title='Розыгрыш!', color=config.orange)
				embed.add_field(name='Победитель',value='Сейчас решиться кто станет победителем!',inline=True)
				embed.add_field(name='Нечего не подкручено!', value='Все решает бот!!')
				embed.add_field(name='Победитель...', value=f'Иии.. Это - {winner}')
				embed.set_footer(text=f"Все права на бота пренадлежат: {config.BOT_AUTHOR}") # Подвал сообщения
				self.startRaffle = False
				# Отправка
				await ctx.send(embed=embed)
			else:
				await ctx.send(embed=discord.Embed(description=f'{author.name}, Вы не можете начать розыгрыш потому что он не был активирован =(', color=config.orange))

		elif command == 'deactivate':
			self.startRaffle = False
			self.raffle = []
			await ctx.send(embed=discord.Embed(description=f'{author.name}, остановил розыгрыш!!', color=config.orange))

		elif command == 'help':
			embed = discord.Embed(title=f'Админ команды для ``{config.PREFIX_COMMAND}araffle``', color=config.orange)
			embed.add_field(name='**Активация розыгрыша**  | ', value=f'``{config.PREFIX_COMMAND}araffle activate``')
			embed.add_field(name='**Запустить розыгрыш**  | ', value=f'``{config.PREFIX_COMMAND}araffle start``')
			embed.add_field(name='**Деактивация розыгрыша** ', value=f'``{config.PREFIX_COMMAND}araffle deactivate``')
			await ctx.send(embed=embed)

		else:
			await ctx.send(embed=discord.Embed(description=f'{author.name}, Вы наверно не знаете но нужно вводить агрумент', color=config.orange))	

class Codes(commands.Cog):
	def __init__(self, client):
		self.client = client

		self.code_stop = []

	@commands.command(aliases = ["код", "Код", "Code"]) # 
	async def code(self, ctx, arg1): # Создает команду
		await ctx.message.delete()
		author = ctx.message.author
		guildAuthor = ctx.guild.owner
		if arg1 == botconfig.code1:
			for x in [self.code_stop]:
				if author not in x:
					self.code_stop.append(author)
					print(code_stop)
					await guildAuthor.send(embed=discord.Embed(description=f'{author}, ввел код {arg}, {config.code1_comment}!!', color=config.orange))
					await author.send(embed=discord.Embed(description=f'{author.name}, вы ввели верный код!!', color=config.orange))
				else:
					await author.send(embed=discord.Embed(description=f'{author.name}, вы уже вводили этот код!!', color=config.red), delete_after=300)
		else:
			await author.send(embed=discord.Embed(description='Вы ввели не существующий код!!', color=config.red), delete_after=300)

class MiniGame(commands.Cog):
	def __init__(self, client):
		self.client = client

		self._stric__last_member = None
		self._stric__member_stric = 0

	@commands.command(aliases = ["кот", "мешок"]) # 
	async def cat(self, ctx): # Создает команду
		r_cat_gif = choice(config.cat_gif) # 
		await ctx.send(r_cat_gif, delete_after=43200) # 

	@commands.command(aliases = ["Ball", "Шар", "шар"]) # 
	async def ball(self, ctx): # Создает команду
		r_ball = choice(config.ball)
		await ctx.send(embed=discord.Embed(description=f'{ctx.message.author.name}, Знаки говорят - **{ r_ball }**.', color=config.orange)) # 

	@commands.command(aliases = ["рандом"])
	async def random(self, ctx, arg1:int, arg2:int):
		author = ctx.message.author
		random = randint(arg1, arg2)
		await ctx.send(embed=discord.Embed(description=f"{author.name} рандомное число которое тебе выпало: **{random}**", color=config.orange))

	@commands.command()
	async def russian_ruletka(self, ctx, member:discord.Member=None):
		author = ctx.message.author
		if member == author:
			await ctx.send(embed=description.Embed(description=f'Все улышали громкий звук выстрела и увидили что {author.name} застрелил сам себя в попытках сыграть сам с собой в "Русскую рулетку"'))
		else:		
			if member == None:
				await ctx.send(embed=discord.Embed(description=f'{author.name}, напишите своего противника'))
			else:
				random = randint(1, 6)
				RandomAuthor = randint(1, 6)
				RandomMember = randint(1, 6)

				while won:
					await ctx.send(embed=discord.Embed(description=f'{self.client.user.name}, заряжает шестизарядный револьвер и протягивает его {author}'))
					sleep(1)
					await ctx.send("К чтобы пройти дальше нужно подождать пока появится код! =)")

	@commands.cooldown(1, 10, commands.BucketType.user)
	@commands.command()
	async def stric(self, ctx, helps:str=None):
		if helps == None:

			author = ctx.message.author

			if self._stric__last_member != author and self._stric__last_member != None:
				secondauthor = self._stric__last_member
				self._stric__last_member = author
				self._stric__member_stric = 0
				await ctx.send(embed=discord.Embed(description=f'``{secondauthor.name}`` потерял лидерство, ``{author.name}`` занял место лидера!', color=config.orange))

			elif author == self._stric__last_member or self._stric__last_member == None:
				self._stric__last_member = author
				self._stric__member_stric += 1
				await ctx.send(embed=discord.Embed(description=f'``{author.name}``, ваш стрик {self._stric__member_stric}', color=config.orange))

		else:
			await ctx.send(embed=discord.Embed(title='Правила игры **Стрик**', description=f'Удерживайте место в лидерстве.', color=config.orange))



	@commands.command(aliases = ["Кости", "кости", "Bones"])
	async def bones(self, ctx, member:discord.Member=None, arg1:int=None, arg2:int=None):
		author = ctx.message.author
		if member == None:
			if arg1 == None and arg2 == None:
				random = randint(1, 6)
				await ctx.send(embed=discord.Embed(description=f'{author.name}, вам выпало {random}', color=config.orange))

			else:
				random = randint(arg1, arg2)
				await ctx.send(embed=discord.Embed(description=f'{author.name}, вам выпало {random}', color=config.orange))

		else:
			if arg1 == None and arg2 == None:
				Random1 = randint(1, 6)
				Random2 = randint(1, 6)

				if Random1 > Random2:
					await ctx.send(embed=discord.Embed(description=f"{author.name}, победил получив {Random1} балов! А {member.name} набрал всего {Random2} баллов", color=config.orange))

				elif Random1 < Random2:
					await ctx.send(embed=discord.Embed(description=f"{member.name}, победил получив {Random2} балов! А {author.name} набрал всего {Random1} балов", color=config.orange))
			
			else:
				# Генерация рандомного число
				if arg1 == None:
					Random1 = randint(1, 6)
				else:
					Random1 = randint(arg1, arg2)

				if arg2 == None:
					Random2 = randint(1, 6)
				else:
					Random2 = randint(arg1, arg2)

				# Отправка сообщений
				if Random1 > Random2:
					await ctx.send(embed=discord.Embed(description=f"{author.name}, победил получив {Random1} балов! А {member.name} набрал всего {Random2} баллов", color=config.orange))

				elif Random1 < Random2:
					await ctx.send(embed=discord.Embed(description=f"{member.name}, победил получив {Random2} балов! А {author.name} набрал всего {Random1} балов", color=config.orange))

class Food(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases = ["Дать", "дать"])
	async def donut(self, ctx, *, food=None):
		author = ctx.message.author
		if food == None:
			await ctx.send(embed=discord.Embed(description=f'{author.name}, пожалуйста напишите что именно вы ходите дать!', color=config.orange))
		else:
			await ctx.send(embed=discord.Embed(description=f'{self.client.user.name}, забирает **{food}** у {author.name}, и молча уходит в свою комнату =D', color=config.orange))

class RPS(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases = ["кнб"])
	async def rps(self, ctx, arg1):
		author = ctx.message.author
		x = randint(1, 3)
		y = arg1

		""" Lose """
		if x == 1 and y == "ножницы":
			await ctx.send(embed=discord.Embed(description=f"{author.name}, вы выбрали ножнцы, а бот - камень! \n\n Вы проиграли!", color=config.orange))
		if x == 2 and y == "бумага":
			await ctx.send(embed=discord.Embed(description=f"{author.name}, вы выбрали бумагу, а бот - ножници! \n\nВы проиграли!", color=config.orange))
		if x == 3 and y == "камень":
			await ctx.send(embed=discord.Embed(description=f"{author.name}, вы выбрали камень, а бот - бумагу! \n\nВы проиграли!", color=config.orange))
		
		""" Won """
		if x == 2 and y == "камень":
			await ctx.send(embed=discord.Embed(description=f"{author.name}, вы выбрали камень, а бот - ножници! \n\nВы выиграли! :tada: ", color=config.orange))
		if x == 3 and y == "ножницы":
			await ctx.send(embed=discord.Embed(description=f"{author.name}, вы выбрали ножницы, а бот - бумагу! \n\nВы выиграли! :tada: ", color=config.orange))
		if x == 1 and y == "бумага":
			await ctx.send(embed=discord.Embed(description=f"{author.name}, вы выбрали бумагу, а бот - камень! \n\nВы выиграли! :tada: ", color=config.orange))
		
		""" Draw """
		if x == 1 and y == "камень":
			await ctx.send(embed=discord.Embed(description=f"{author.name}, вы выбрали камень, а бот - камень! \n\nНичья!", color=config.orange))
		if x == 2 and y == "ножницы":
			await ctx.send(embed=discord.Embed(description=f"{author.name}, вы выбрали ножницы, а бот - ножници! \n\nНичья!", color=config.orange))
		if x == 3 and y == "бумага":
			await ctx.send(embed=discord.Embed(description=f"{author.name}, вы выбрали бумагу, а бот - бумагу! \n\nНичья!", color=config.orange))

def setup(client):
	try:
		client.add_cog(Raffle(client))
		client.add_cog(Codes(client))
		client.add_cog(MiniGame(client))
		client.add_cog(Food(client))
		client.add_cog(RPS(client))
	except Exception as e:
		print(f'[ERROR] File BotFun.py not work because: "{e}"')