import discord
from discord.ext import commands

import botconfig

class CommandSentence(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases = ["предложение", "Sentence", "Предложение"])
	async def sentence(self, ctx, *, arg): # Создает команду
		author = ctx.message.author # Инициализирует автора
		channel_log = self.client.get_channel(channel_log) # Лог чат
		await ctx.message.add_reaction('✅') # Добавляет лайк
		await ctx.message.add_reaction('❎') # Добавляет дизлайк
		await ctx.send(embed=discord.Embed(description=f'{author.name}, спасибо за вашу идею.', color=botconfig.orange), delete_after=30) # Отправляет сообщение в чат
		await channel_log.send(embed=discord.Embed(description=f'Пользователь {author} преложил идею: \n``{arg}``', color=botconfig.orange)) # отправляет сообение в лог чат

class CommandUser(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def user(self, ctx, member: discord.Member):
		author = ctx.message.author
		embed = discord.Embed(title=f'Пользователь {member.name}', color=botconfig.orange)
		embed.add_field(name='Статус пользователя',value=f'Статус {member.status}',inline=True)
		embed.set_footer(text=f"Все права на бота пренадлежат: {BOT_AUTHOR}") # Подвал сообщения
		await ctx.send(embed=embed)

class CommandBots(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases=['bots', 'Бот', 'бот'])
	async def Bots(self, ctx):
		await ctx.send(f'Bots is {self.client.user}')

def setup(client):
	client.add_cog(CommandSentence(client)) # 6
	client.add_cog(CommandUser(client)) # 19
	client.add_cog(CommandBots(client)) # 31