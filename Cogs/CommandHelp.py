import discord
from discord.ext import commands

from botforminecraftserver import botconfig

class CommandHelp(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases = ["сервер", "серв", "server", "Server"]) # Информация о сервере рабоает также с командами...
	async def Сервер(self, ctx):
	    guild = ctx.guild
	    embed = discord.Embed(title=f"Сервер: **{guild.name}**", description="**Енот Бот** был сделан специально для этого сервера.", color=botconfig.orange) # Создает строку
	    embed.add_field(name=":wave: **Привет дорогой друг.** :wave:", value=f"Если ты тут значит тебя приняли,\n чтобы узнать айпи напиши - {botconfig.PREFIX_COMMAND}ip", inline=True) # Создает строку
	    embed.add_field(name="Людей на сервере", value=f"{guild.member_count}", inline=False)
	    embed.add_field(name="**Немного о сервере:**", value="Нету приватов, нету доната, свобода действий, не ограниченая территория.", inline=False) # Создает строку
	    embed.add_field(name="**Узнать все команды:**", value=f"{botconfig.PREFIX_COMMAND}Помощь.", inline=False) # Создает строку
	    embed.add_field(name="**Пожертвования:**", value=f"Если у вас появилось желание помочь серверу\n просто напишите - {botconfig.PREFIX_COMMAND}donate", inline=False) # Создает строку
	    embed.set_footer(text=f"Все права на бота пренадлежат: {botconfig.BOT_AUTHOR}") # Подвал сообщения
	    await ctx.send(embed=embed) # Отправляет сообщение а потому удалит после 300 секунд

	@commands.command(aliases=["помощь", "Help", "help"]) # Команда Помощь работает также с...
	async def Помощь(self, ctx): # Создает команду
	    embed = discord.Embed(title="Все команды **Енот Бот**", description="", color=botconfig.orange) # Создает красивый вывод с заголовком title и цветом green 
	    embed.add_field(name=f'**{botconfig.PREFIX_COMMAND}Сервер**', value="Информация о сервере.", inline=False) # Создает строку
	    embed.add_field(name=f'**{botconfig.PREFIX_COMMAND}cat**', value="Отправляет гифку кота =D.", inline=False) # Создает строку
	    embed.add_field(name=f'**{botconfig.PREFIX_COMMAND}ver**', value="Узнать версию бота.", inline=False) # Создает строку
	    embed.add_field(name=f'**{botconfig.PREFIX_COMMAND}шар**', value="Отвечает на заданый вопрос.", inline=False) # Создает строку
	    embed.set_footer(text=f"Все права на бота пренадлежат: {botconfig.BOT_AUTHOR}") # Подвал сообщения
	    await ctx.send(embed=embed) # 

	@commands.command(aliases = ["версия", "Версия", "Ver"]) # 
	async def ver(self, ctx): # Создает команду
	    embed = discord.Embed(title="**Версия бота**", color=botconfig.orange) # 
	    embed.add_field(name="**Последняя версия**", value=f"Версия - {botconfig.version}", inline=True) # 
	    embed.set_footer(text=f"Все права на бота пренадлежат: {botconfig.BOT_AUTHOR}") # Подвал сообщения
	    await ctx.send(embed=embed) # 

	@commands.command(aliases=["донат", "Донат", "Donate"])
	async def donate(self, ctx):
		await ctx.author.send("Sorry it's command don't work")
	    # embed = discord.Embed(title="**Реквизиты**", description="Места куда можно скинуть денюжку.", color=orange)
	    # embed.add_field(name="**Реквизиты**", value=f"QIWI - {botconfig.donate_qiwi}\nWebMoney - {botconfig.donate_webmoney}", inline=True) # 
	    # embed.set_footer(text=f"Все права на бота пренадлежат: {botconfig.BOT_AUTHOR}") # Подвал сообщения
	    # await ctx.author.send(embed=embed)

	@commands.command(aliases=["айпи", "ип", "Айпи", "Ип"]) # Команда ip работает также с...
	async def ip(self, ctx): # Создает команду
	    channel_msg = ctx.message.channel
	    channel_black = self.client.get_channel(botconfig.black_list_channel)
	    if channel_msg not in channel_black:
	        embed = discord.Embed(title="**IP - адрес и версия**", description="Удачи тебе, некогда не опускай руки", color=botconfig.orange) # 
	        embed.add_field(name="IP и версия", value=f"IP - {botconfig.server_ip}\nВерсия - {botconfig.verver_version}", inline=True) # 
	        embed.set_footer(text=f"Все права на бота пренадлежат: {botconfig.BOT_AUTHOR}") # Подвал сообщения
	        await ctx.author.send(embed=embed) # 
	    else:
	        await channel.send(embed=discord.Embed(description=f'{member.name}, нельзя сюда вводить эту команду', color=orange))

def setup(client):
	client.add_cog(CommandHelp(client))