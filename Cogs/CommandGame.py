import discord
from discord.ext import commands

from random import randint, choice

from botforminecraftserver import botconfig

raffle = []
code_stop = []

class Raffle(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases=["розыгрыш"])
	async def Розыгрыш(self, ctx): # Создает команду
		author = ctx.message.author
		for x in [raffle]:
			if author not in x:
				raffle.extend([author])
				player_raffle = len(raffle)
				embed = discord.Embed(title='Розыгрыш!', color=botconfig.orange)
				embed.add_field(name='Спасибо!',value='Вы были добавлены в список участников розыгрыша!',inline=True) # 
				embed.add_field(name=f'Список участников.', value=f'В списке участников находиться {player_raffle} участник(ков) розыгрыша.') # 
				embed.set_footer(text=f"Все права на бота пренадлежат: {botconfig.BOT_AUTHOR}") # Подвал сообщения
				await ctx.author.send(embed=embed) # 
			else:
				await ctx.send(embed=discord.Embed(description=f'{author.name}, вы уже есть в списке участников розыгрыша!', color=botconfig.red)) # 

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def start_raffle(self, ctx, amount=1): # Создает команду
		await ctx.channel.purge(limit=amount)
		author = ctx.message.author
		len_raffle = len(raffle)
		random_raffle = randint(1, len_raffle)
		embed = discord.Embed(title='Розыгрыш!', color=botconfig.orange)
		embed.add_field(name='Победитель',value='Сейчас решиться кто станет победителем!',inline=True)
		embed.add_field(name='Нечего не подкручено!', value='Все решает бот!!')
		embed.add_field(name='Победитель...', value=f'Иии.. Это - {raffle[random_raffle]}')
		embed.set_footer(text=f"Все права на бота пренадлежат: {botconfig.BOT_AUTHOR}") # Подвал сообщения
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
					await bot_author.send(embed=discord.Embed(description=f'{author}, ввел код {arg}, {botconfig.code1_comment}!!', color=botconfig.orange))
					await author.send(embed=discord.Embed(description=f'{author.name}, вы ввели верный код!!', color=botconfig.orange))
				else:
					await author.send(embed=discord.Embed(description=f'{author.name}, вы уже вводили этот код!!', color=botconfig.red), delete_after=300)
		else:
			await author.send(embed=discord.Embed(description='Вы ввели не существующий код!!', color=botconfig.red), delete_after=300)

class MiniGame(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases = ["кот", "мешок"]) # 
	async def cat(self, ctx): # Создает команду
		r_cat_gif = choice(botconfig.cat_gif) # 
		await ctx.send(r_cat_gif, delete_after=43200) # 

	@commands.command(aliases = ["ball", "Ball", "Шар"]) # 
	async def шар(self, ctx): # Создает команду
		r_ball = choice(botconfig.ball)
		await ctx.send(embed=discord.Embed(description=f'{ctx.message.author.name}, Знаки говорят - **{ r_ball }**.', color=botconfig.orange)) # 

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
	client.add_cog(Raffle(client))
	client.add_cog(Codes(client))
	client.add_cog(MiniGame(client))
	client.add_cog(RPS(client))