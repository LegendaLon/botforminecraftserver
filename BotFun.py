import discord
from discord.ext import commands

from random import randint, choice

import config

raffle = []
code_stop = []

class Utils(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases = ["рандом"])
	async def random(self, ctx, arg1:int, arg2:int):
		author = ctx.message.author
		random = randint(arg1, arg2)
		await ctx.send(f"{author.name} рандомное число которое тебе выпало - {random}")

class Raffle(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases = ["розыгрыш"])
	async def Розыгрыш(self, ctx): # Создает команду
		author = ctx.message.author
		for x in [raffle]:
			if author not in x:
				raffle.extend([author])
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
	async def start_raffle(self, ctx, amount=1): # Создает команду
		await ctx.channel.purge(limit=amount)
		author = ctx.message.author
		len_raffle = len(raffle)
		random_raffle = randint(1, len_raffle)
		embed = discord.Embed(title='Розыгрыш!', color=config.orange)
		random_raffle = random.randint(1,len_raffle)
		embed.add_field(name='Победитель',value='Сейчас решиться кто станет победителем!',inline=True)
		embed.add_field(name='Нечего не подкручено!', value='Все решает бот!!')
		embed.add_field(name='Победитель...', value=f'Иии.. Это - {raffle[random_raffle]}')
		embed.set_footer(text=f"Все права на бота пренадлежат: {config.BOT_AUTHOR}") # Подвал сообщения
		await ctx.send(embed=embed, delete_after=300)
		await author.send(f'Победитель {raffle[random_raffle]}')

class Codes(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases = ["код", "Код", "Code"]) # 
	async def code(self, ctx, arg1, amount=1): # Создает команду
		await ctx.channel.purge(limit=amount) # 
		author = ctx.message.author
		bot_author = self.client.get_user(518766156790890496)
		if arg1 == botconfig.code1:
			for x in [code_stop]:
				if author not in x:
					code_stop.append(author)
					print(code_stop)
					await bot_author.send(embed=discord.Embed(description=f'{author}, ввел код {arg}, {config.code1_comment}!!', color=config.orange))
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

	@commands.command(aliases = ["Вызов","вызов"])
	async def call(self, ctx, member:discord.Member):
		author = ctx.message.author

		Random1 = randint(1, 10)
		Random2 = randint(1, 10)

		if Random1 > Random2:
			await ctx.send(f"{author.name} победил получив {Random1} балов! А {member.name} набрал всего {Random2} баллов")

		elif Random1 < Random2:
			await ctx.send(f"{member.name} победил получив {Random2} балов! А {author.name} набрал всего {Random1} балов")

class RPS(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases = ["кнб"])
	async def rps(self, ctx, arg1):
		author = ctx.message.author
		x = randint(1, 3)
		y = arg1

		""" Lose """
		if x == 1 and y == "ножници":
			check = 1
			await ctx.send(f"{author.mention} вы выбрали ножнци, а бот - камень! Вы проиграли!")
		if x == 2 and y == "бумага":
			check = 1
			await ctx.send(f"{author.mention} вы выбрали бумагу, а бот - ножници! Вы проиграли!")
		if x == 3 and y == "камень":
			check = 1
			await ctx.send(f"{author.mention} вы выбрали камень, а бот - бумагу! Вы проиграли!")
		
		""" Won """
		if x == 2 and y == "камень":
			check = 1
			await ctx.send(f"{author.mention} вы выбрали камень, а бот - ножници! Вы выиграли! :tada: ")
		if x == 3 and y == "ножницы":
			check = 1
			await ctx.send(f"{author.mention} вы выбрали ножници, а бот - бумагу! Вы выиграли! :tada: ")
		if x == 1 and y == "бумага":
			check = 1
			await ctx.send(f"{author.mention} вы выбрали бумагу, а бот - камень! Вы выиграли! :tada: ")
		
		""" Draw """
		if x == 1 and y == "камень":
			check = 1
			await ctx.send(f"{author.mention} вы выбрали камень, а бот - камень! Ничья!")
		if x == 2 and y == "ножницы":
			check = 1
			await ctx.send(f"{author.mention} вы выбрали ножници, а бот - ножници! Ничья!")
		if x == 3 and y == "бумага":
			check = 1
			await ctx.send(f"{author.mention} вы выбрали бумагу, а бот - бумагу! Ничья!")

def setup(client):
	client.add_cog(Utils(client))
	client.add_cog(Raffle(client))
	client.add_cog(Codes(client))
	client.add_cog(MiniGame(client))
	client.add_cog(RPS(client))