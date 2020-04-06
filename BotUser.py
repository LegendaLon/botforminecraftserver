import discord
from discord.ext import commands

import config

class Sentence(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases = ["предложение", "Sentence", "Предложение"])
	async def sentence(self, ctx, *, arg = None): # Создает команду
		if arg == None:
			await ctx.send(embed=discord.Embed(description=f'{author.name}, вы забыли написать текст.', color=config.orange), delete_after=30) # Отправляет сообщение в чат
		else:
			author = ctx.message.author # Инициализирует автора
			await ctx.message.add_reaction('✅') # Добавляет лайк
			await ctx.message.add_reaction('❎') # Добавляет дизлайк
			await ctx.send(embed=discord.Embed(description=f'{author.name}, спасибо за вашу идею.', color=config.orange), delete_after=30) # Отправляет сообщение в чат

class User(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases = ["User", "Юзер", "юзер"])
	async def user(self, ctx, member: discord.Member = None):
		if member == None:
			author = ctx.message.author
			embed = discord.Embed(title=f'Пользователь {author.name}', color=config.orange)
			embed.add_field(name='Статус пользователя',value=f'Статус {author.status}',inline=True)
			embed.set_footer(text=f"Все права на бота пренадлежат: {config.BOT_AUTHOR}") # Подвал сообщения
			await ctx.send(embed=embed)
		else:
			embed = discord.Embed(title=f'Пользователь {member.name}', color=config.orange)
			embed.add_field(name='Статус пользователя',value=f'Статус {member.status}',inline=True)
			embed.set_footer(text=f"Все права на бота пренадлежат: {config.BOT_AUTHOR}") # Подвал сообщения
			await ctx.send(embed=embed)

def setup(client):
	try:
		client.add_cog(Sentence(client))
		client.add_cog(User(client))
	except Exception as e:
		print(f'[ERROR] File BotUser.py not work because: "{e}"')