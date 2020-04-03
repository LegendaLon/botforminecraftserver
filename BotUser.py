import discord
from discord.ext import commands

import config

class CommandSentence(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases = ["предложение", "Sentence", "Предложение"])
	async def sentence(self, ctx, *, arg): # Создает команду
		author = ctx.message.author # Инициализирует автора
		await ctx.message.add_reaction('✅') # Добавляет лайк
		await ctx.message.add_reaction('❎') # Добавляет дизлайк
		await ctx.send(embed=discord.Embed(description=f'{author.name}, спасибо за вашу идею.', color=config.orange), delete_after=30) # Отправляет сообщение в чат

class CommandUser(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def user(self, ctx, member: discord.Member):
		author = ctx.message.author
		embed = discord.Embed(title=f'Пользователь {member.name}', color=config.orange)
		embed.add_field(name='Статус пользователя',value=f'Статус {member.status}',inline=True)
		embed.set_footer(text=f"Все права на бота пренадлежат: {config.BOT_AUTHOR}") # Подвал сообщения
		await ctx.send(embed=embed)

class CommandBots(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases=['bots', 'Бот', 'бот'])
	async def Bots(self, ctx):
		await ctx.send(f'Bots is {self.client.user.name}')

def setup(client):
	client.add_cog(CommandSentence(client)) # 6
	client.add_cog(CommandUser(client)) # 19
	client.add_cog(CommandBots(client)) # 31