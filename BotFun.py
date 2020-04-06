import discord
from discord.ext import commands

from random import randint, choice

import config

class Utils(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases = ["рандом"])
	async def random(self, ctx, arg1:int, arg2:int):
		author = ctx.message.author
		random = randint(arg1, arg2)
		await ctx.send(embed=discord.Embed(description=f"{author.name} рандомное число которое тебе выпало: **{random}**", color=config.orange))

class Raffle(commands.Cog):
	def __init__(self, client):
		self.client = client

		self.raffle = []

	@commands.command(aliases = ["розыгрыш"])
	async def Розыгрыш(self, ctx): # Создает команду
		author = ctx.message.author
		for x in [self.raffle]:
			if author not in x:
				self.raffle.extend([author])
				player_raffle = len(raffle)
				embed = discord.Embed(title='Розыгрыш!', color=config.orange)
				embed.add_field(name='Спасибо!',value='Вы были добавлены в список участников розыгрыша!',inline=True) # 
				embed.add_field(name=f'Список участников.', value=f'В списке участников находиться {player_raffle} участник(ков) розыгрыша.') # 
				embed.set_footer(text=f"Все права на бота пренадлежат: {config.BOT_AUTHOR}") # Подвал сообщения
				await ctx.author.send(embed=embed) # 
			else:
				await ctx.send(embed=discord.Embed(description=f'{author.name}, вы уже есть в списке участников розыгрыша!', color=config.red)) # 

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def start_raffle(self, ctx): # Создает команду
		await ctx.channel.purge(limit=1)
		author = ctx.message.author
		len_raffle = len(self.raffle)
		random_raffle = randint(1, len_raffle)
		random_raffle = random.randint(1,len_raffle)
		# Сообщение
		embed = discord.Embed(title='Розыгрыш!', color=config.orange)
		embed.add_field(name='Победитель',value='Сейчас решиться кто станет победителем!',inline=True)
		embed.add_field(name='Нечего не подкручено!', value='Все решает бот!!')
		embed.add_field(name='Победитель...', value=f'Иии.. Это - {raffle[random_raffle]}')
		embed.set_footer(text=f"Все права на бота пренадлежат: {config.BOT_AUTHOR}") # Подвал сообщения
		self.raffle = []
		# Отправка
		await ctx.send(embed=embed, delete_after=300)
		await author.send(f'Победитель {raffle[random_raffle]}')

class Codes(commands.Cog):
	def __init__(self, client):
		self.client = client

		self.code_stop = []

	@commands.command(aliases = ["код", "Код", "Code"]) # 
	async def code(self, ctx, arg1): # Создает команду
		await ctx.channel.purge(limit=1) # 
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

	@commands.command(aliases = ["кот", "мешок"]) # 
	async def cat(self, ctx): # Создает команду
		r_cat_gif = choice(config.cat_gif) # 
		await ctx.send(r_cat_gif, delete_after=43200) # 

	@commands.command(aliases = ["Ball", "Шар", "шар"]) # 
	async def ball(self, ctx): # Создает команду
		r_ball = choice(config.ball)
		await ctx.send(embed=discord.Embed(description=f'{ctx.message.author.name}, Знаки говорят - **{ r_ball }**.', color=config.orange)) # 

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
				if arg1 == None:
					Random1 = randint(1, 6)
				else:
					Random2 = randint(arg1, arg2)

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
		client.add_cog(Utils(client))
		client.add_cog(Raffle(client))
		client.add_cog(Codes(client))
		client.add_cog(MiniGame(client))
		client.add_cog(Food(client))
		client.add_cog(RPS(client))
	except Exception as e:
		print(f'[ERROR] File BotFun.py not work because: "{e}"')