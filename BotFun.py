import discord
from discord.ext import commands

from random import randint, choice

from asyncio import sleep as timer

from main import db

import config

class Psychologist(commands.Cog):
	def __init__(self, client):
		self.client = client
		

class Raffle(commands.Cog):
	def __init__(self, client):
		self.client = client

		self.startRaffle = False
		self.raffle = []

	@commands.command(
		aliases = ["Розыгрыш", "розыгрыш"],
		help = None,
		description = '',
		hidden = True,
		)
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

	@commands.command(
		help = None,
		description = '',
		hidden = True,
		)
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

class RolePlay(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(
		aliases = ["Push", "Ударить", "ударить"],
		help = '[*Пользователь] [*Предмет]',
		description = 'Ударит пользователя предметом',
		hidden = False,
		)
	async def push(self, ctx, member: discord.Member=None, *, arg=None):
		author = ctx.message.author
		await ctx.message.delete()

		if member != None and arg != None:
			await ctx.send(embed=discord.Embed(description=f'``{author.name}`` ударил ``{member.name}`` с помощью {arg}', color=config.orange))

	@commands.command(
		aliases = ["Me", "Ме", "ме"],
		help = '[*Пользователь] [*Предмет]',
		description = 'Выполний рп действие',
		hidden = False,
		)
	async def me(self, ctx, *, arg=None):
		author = ctx.message.author
		won = randint(1, 2)
		await ctx.message.delete()

		if won == 1:
			await ctx.send(embed=discord.Embed(description=f'{author.name} {arg}\nУспешно', color=config.orange))
		else:
			await ctx.send(embed=discord.Embed(description=f'{author.name} {arg}\nПровалено', color=config.orange))


class MiniGame(commands.Cog):
	def __init__(self, client):
		self.client = client

		self._stric__last_member = None
		self._stric__member_stric = 0
		self._stric__guild_name = None

	@commands.command(
		aliases = ["кот", "мешок"],
		help = None,
		description = 'Отправит гифку котика <3',
		hidden = False,
		) 
	async def cat(self, ctx): # Создает команду
		r_cat_gif = choice(config.cat_gif) # 
		await ctx.send(r_cat_gif, delete_after=43200) # 


	@commands.command(
		aliases = ["Ball", "Шар", "шар"],
		help = '[Вопрос]',
		description = 'Ответит на ваш вопрос',
		hidden = False,
		) 
	async def ball(self, ctx): # Создает команду
		r_ball = choice(config.ball)
		await ctx.send(embed=discord.Embed(description=f'{ctx.message.author.name}, Знаки говорят - **{ r_ball }**.', color=config.orange)) # 

	@commands.command(
		aliases = ["рандом"],
		help = '[Минимальное число] [Максимальное число]',
		description = 'Сгенерирует число.',
		hidden = False,
		
		)
	async def random(self, ctx, arg1:int, arg2:int):
		author = ctx.message.author
		random = randint(arg1, arg2)
		await ctx.send(embed=discord.Embed(description=f"{author.name} рандомное число которое тебе выпало: **{random}**", color=config.orange))

	@commands.command(
		help = '',
		description = '',
		hidden = True,
		)
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
	@commands.command(
		help = '',
		description = '',
		hidden = True,
		)
	async def stric(self, ctx, helps:str=None):
		if helps == None:

			author = ctx.message.author
			guild = ctx.guild

			if self._stric__last_member != author and self._stric__last_member != None:
				secondauthor = self._stric__last_member
				self._stric__last_member = author
				self._stric__member_stric = 1
				self._stric__guild_name = guild.name
				await ctx.send(embed=discord.Embed(description=f'``{secondauthor.name}`` потерял лидерство, ``{author.name}`` занял место лидера!', color=config.orange))

			elif author == self._stric__last_member or self._stric__last_member == None:
				self._stric__last_member = author
				self._stric__member_stric += 1
				await ctx.send(embed=discord.Embed(description=f'``{author.name}``, ваш стрик {self._stric__member_stric}', color=config.orange))

		else:
			await ctx.send(embed=discord.Embed(title='Правила игры **Стрик**', description=f'Удерживайте место в лидерстве.', color=config.orange))

	@commands.command(
		aliases = ["Love", "Любовь", "любовь"],
		help = '[*Человек/Предмет]',
		description = 'Покажет Вашу любовь к человеку/предмету в процентах',
		hidden = False,
		)
	async def love(self, ctx, *, arg):
		love = randint(1, 100)
		author = ctx.message.author

		await ctx.send(embed=discord.Embed(description=f'Любовь {author.name} к {arg} измеряеться в {love}%', color=config.orange))

	@commands.command(
		aliases = ["Кости", "кости", "Bones"],
		help = '[*Пользователь] [Максимальное число] [Минимальное число]',
		description = 'Сыграть с пользователем в кости.',
		hidden = False,
		
		)
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

class Pasxalci(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(
		help = '',
		description = '',
		hidden = True,
		)
	async def createdfor(self, ctx):
		author = ctx.message.author
		await ctx.send(embed=discord.Embed(description=f'{author.name}, о Ты нашёл одну из пасхалок!\nЭтот бот изначально создавался для группы дискорд одно из серверов игры **MineCraft**', color=config.orange))

	@commands.command(
		help = '',
		description = '',
		hidden = True,
		)
	async def BadPerson(self, ctx):
		author = ctx.message.author
		await ctx.send(embed=discord.Embed(description=f'``{author.name}``, о Ты нашёл одну из пасхалок!\nАвтор бота плохо относится к людям которые были извесны под никами ``Neros_``, ``DonDanon``, ``KislBall``, ``EnotKEK3``', color=config.orange))


class Food(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(
		aliases = ["Дать", "дать"],
		help = '[*Предмет]',
		description = 'Вы дадите предмет боту',
		hidden = False,
		)
	async def donut(self, ctx, *, food='воздух'):
		author = ctx.message.author
		await ctx.send(embed=discord.Embed(description=f'{self.client.user.name}, забирает **{food}** у {author.name}, и молча уходит в свою комнату =D', color=config.orange))

class RPS(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(
		aliases = ["кнб"],
		help = '[*Камень/Ножницы/Бумага]',
		description = 'Сыграть в камень кожницы бумага с ботом',
		hidden = False,
		)
	async def rps(self, ctx, arg1):
		author = ctx.message.author
		x = randint(1, 3)
		y = arg1.lower()

		""" Lose """
		if x == 1 and y == "ножницы":
			await ctx.send(embed=discord.Embed(description=f"{author.name}, вы выбрали ножнцы, а бот - камень! \n\n Вы проиграли!", color=config.orange))
		if x == 2 and y == "бумага":
			await ctx.send(embed=discord.Embed(description=f"{author.name}, вы выбрали бумагу, а бот - ножницы! \n\nВы проиграли!", color=config.orange))
		if x == 3 and y == "камень":
			await ctx.send(embed=discord.Embed(description=f"{author.name}, вы выбрали камень, а бот - бумагу! \n\nВы проиграли!", color=config.orange))
		
		""" Won """
		if x == 2 and y == "камень":
			await ctx.send(embed=discord.Embed(description=f"{author.name}, вы выбрали камень, а бот - ножницы! \n\nВы выиграли! :tada: ", color=config.orange))
		if x == 3 and y == "ножницы":
			await ctx.send(embed=discord.Embed(description=f"{author.name}, вы выбрали ножницы, а бот - бумагу! \n\nВы выиграли! :tada: ", color=config.orange))
		if x == 1 and y == "бумага":
			await ctx.send(embed=discord.Embed(description=f"{author.name}, вы выбрали бумагу, а бот - камень! \n\nВы выиграли! :tada: ", color=config.orange))
		
		""" Draw """
		if x == 1 and y == "камень":
			await ctx.send(embed=discord.Embed(description=f"{author.name}, вы выбрали камень, а бот - камень! \n\nНичья!", color=config.orange))
		if x == 2 and y == "ножницы":
			await ctx.send(embed=discord.Embed(description=f"{author.name}, вы выбрали ножницы, а бот - ножницы! \n\nНичья!", color=config.orange))
		if x == 3 and y == "бумага":
			await ctx.send(embed=discord.Embed(description=f"{author.name}, вы выбрали бумагу, а бот - бумагу! \n\nНичья!", color=config.orange))

def setup(client):
	try:
		client.add_cog(Raffle(client))
		client.add_cog(RolePlay(client))
		client.add_cog(MiniGame(client))
		client.add_cog(Pasxalci(client))
		client.add_cog(Food(client))
		client.add_cog(RPS(client))
	except Exception as e:
		print(f'[ERROR] File BotFun.py not work because: "{e}"')