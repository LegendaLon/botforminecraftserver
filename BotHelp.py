import discord
from discord.ext import commands

from main import module, db, allfiles

from lenlines import counterLinesWordsLetters

import config

""" Constants """
adminhelparr = ["админ", "admin"]
bothelparr = ["бот", "bot"]
rphelparr = ["рп", "rp", "roleplay"]


class Help(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.cooldown(1, 10, commands.BucketType.user)
	@commands.command(aliases = ["сервер", "серв", "server", "Server"])
	async def Сервер(self, ctx):
		guild = ctx.guild
		embed = discord.Embed(title=f'Информация о сервере: **{guild.name}**', color=config.orange)
		embed.set_thumbnail(url=guild.icon_url)
		# embed.add_field(name=":wave: **Привет дорогой друг.** :wave:", value="Ты сейчас на закрытом сервере.", inline=True) # Создает строку
		embed.add_field(name="**Узнать все команды:**", value=f"{config.PREFIX_COMMAND}Помощь.", inline=False)
		embed.add_field(name="**Сейчас людей на сервере:**", value=f"{guild.member_count}", inline=True)
		embed.add_field(name="**Регион:**", value=guild.region, inline=True)
		embed.add_field(name="**Создатель сервера:**", value=guild.owner, inline=True)
		embed.add_field(name=f"**Количество чатов[{len(guild.channels)}]: **", value=f'Текстовых: **{len(guild.text_channels)}**\nГолосовых: **{len(guild.voice_channels)}**', inline=True)
		embed.add_field(name=f"**Количество ролей:**",value=len(guild.roles), inline=True)
		embed.add_field(name=f"**Сервер был создан:**",value=guild.created_at, inline=True)
		embed.set_footer(text=f"Все права на бота пренадлежат: {config.BOT_AUTHOR}")
		await ctx.send(embed=embed)

	@commands.cooldown(1, 10, commands.BucketType.user)
	@commands.command(aliases=["помощь", "Help", "help"])
	async def Помощь(self, ctx, types=None):

		embed = discord.Embed(title=f"Все обычные команды **{self.client.user.name}**", description="", color=config.orange)
		embed.set_thumbnail(url=self.client.user.avatar_url)
		embed.add_field(name=f'**{pr}Сервер**', value="Информация о сервере.", inline=False)
		embed.add_field(name=f'**{pr}шар [Вопрос]**', value="Отвечает на заданый вопрос, да или нет.", inline=False)
		embed.add_field(name=f'**{pr}кости [Упоминание] [Минимальное число] [Максимальное число]**', value="Сыграть с игроком в игру кости.", inline=False)
		embed.add_field(name=f'**{pr}Розыгрыш**', value="Поучаствовать в розыгрыше.", inline=False)
		embed.add_field(name=f'**{pr}код [*Код]**', value="Ввести код для получение некого подарка.", inline=False)
		embed.add_field(name=f'**{pr}юзер [Упоминание]**', value="Узнать информацию о пользователе.", inline=False)
		embed.add_field(name=f'**{pr}бот**', value="Узнать информацию о боте.", inline=False)
		embed.add_field(name=f'**{pr}кнб [*камень/ножницы/бумага]**', value="Камень ножници бумага с ботом.", inline=False)
		embed.add_field(name=f'**{pr}дать [*Вещь]**', value="Дать что-то боту.", inline=False)
		embed.add_field(name=f'**{pr}рандом [*Минимальное число] [*Максимальное число]**', value="Генерация рандомного числа.", inline=False)
		embed.add_field(name=f'**{pr}cat**', value="Отправляет гифку кота =D.", inline=False)
		embed.add_field(name=f'**{pr}модули**', value="Список всех модулей.", inline=False)
		embed.add_field(name=f'**{pr}ver**', value="Узнать версию бота.", inline=False)
		embed.add_field(name=f'**Аргументы:**', value="Если перед аргументом стоит ``*`` то нужно обезательно указывать аргумент.", inline=False)
		embed.set_footer(text=f"Все права на бота пренадлежат: {config.BOT_AUTHOR}")

		await ctx.send(embed=embed)

	@commands.command(aliases = ["версия", "Версия", "Ver"])
	async def ver(self, ctx): # Создает команду
		embed = discord.Embed(title="**Версия бота**", color=config.orange) # 
		embed.add_field(name="**Последняя версия**", value=f"Версия - {config.version}", inline=True)
		embed.set_footer(text=f"Все права на бота пренадлежат: {config.BOT_AUTHOR}")
		await ctx.send(embed=embed) # 

class Info(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases = ["Module", "Модули", "модули"])
	@commands.has_permissions(administrator=True)
	async def module(self, ctx):
		author = ctx.message.author
		await ctx.send(embed=discord.Embed(description=f'{author}, все модули которые бот использует:\n``{module}``', color=config.orange))

	@commands.command(aliases=['Bots', 'Бот', 'бот'])
	async def bots(self, ctx):
		embed = discord.Embed(title=f'Бот: {self.client.user.name}')
		embed.set_thumbnail(url=self.client.user.avatar_url)
		# embed.add_field(name=f'Сервера:', value=f'Бот стоит на {}', inline=False)
		embed.add_field(name=f'Идеи пользователей:', value=f'Если у Вас появилась идея что можно добавить в {self.client.user.name}\nтогда пишите в группу которую можете увидеть ниже', inline=True)
		embed.add_field(name=f'Обновления:', value=f'Регулярные', inline=False)
		embed.add_field(name=f'Сервер:', value=f'Место где можно получить тех поддержку бота + место\nгде можно пообщатся и поиграть!\nhttps://discord.gg/tJMrQhN', inline=False)
		embed.add_field(name=f'Автор:', value=f'Автор бота {config.BOT_AUTHOR}', inline=True)
		embed.set_footer(text=f"Все права на бота пренадлежат: {config.BOT_AUTHOR}")
		await ctx.send(embed=embed)

	@commands.cooldown(1, 10, commands.BucketType.user)
	@commands.command()
	async def lines(self, ctx):
		totallines = 0
		totalwords = 0
		totalletters = 0
		alllines = counterLinesWordsLetters(allfiles)
		embed = discord.Embed(title='Количество строчек, слов, букв в коде бота', color=config.orange)
		for a in alllines:
			embed.add_field(name=f'Все строчки файла: {a[0]}', value=f'Строчки: {a[1]}\nСлова: {a[2]}\nБуквы: {a[3]}', inline=True)

			totallines += a[1]
			totalwords += a[2]
			totalletters += a[3]

		embed.add_field(name=f'Все строчки всех вайлов:\n{allfiles}', value=f'Строчки: {totallines}\nСлова: {totalwords}\nБуквы: {totalletters}', inline=False)
		embed.set_footer(text=f"Все права на бота пренадлежат: {config.BOT_AUTHOR}")
		print(alllines)
		await ctx.send(embed=embed)

def setup(client):
	try:
		client.add_cog(Help(client))
		client.add_cog(Info(client))
	except Exception as e:
		print(f'[ERROR] File BotHelp.py not work because: "{e}"')