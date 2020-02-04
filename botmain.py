import discord
from discord.ext import commands
from discord.ext.commands import Bot
import botconfig
import os

bot = commands.Bot(command_prefix=botconfig.PREFIX_COMMAND) # Задает префикс для команд, берит из botconfig.py

bot.remove_command('help') # Удаляет команду help

@bot.event
async def on_ready(): # Когда запускаеться бот
    activity = activity = discord.Game(name=botconfig.BOT_STATUS) # Задает статус, берет их из botconfig.py
    await bot.change_presence(status=discord.Status.idle, activity=activity) # Применяет статус
    print('Бот запущен') # Выводит сообщение в консоль

@bot.command()
async def say(ctx):
    say_at_me = input("Введите сообщение через консоль: ")
    await ctx.send(say_at_me)

@bot.command()
async def Помощь(ctx):
    embed = discord.Embed(title="Все команды **Енот Бот**", description="", color=0xeee657)
    embed.add_field(name='**$Сервер**', value="Информация о сервере.", inline=False)
    embed.add_field(name='**$ip**', value="IP-Адрес и версия.", inline=False)
    embed.add_field(name='**$donate**', value="Пожертвования для сервера.", inline=False)
    embed.add_field(name='**$cat**', value="Отправляет гифку кота =D.", inline=False)
    embed.add_field(name='**$ver**', value="Узнать версию бота.", inline=False)
    embed.set_footer(text="Все права на бота пренадлежат: {0}".format(botconfig.BOT_AUTHOR)) # Подвал сообщения
    await ctx.send(embed=embed)

@bot.command()
async def Сервер(ctx):
    embed = discord.Embed(title="Сервер: **Legend of The World**", description="**Енот Бот** был сделан специально для этого сервера.", color=0xeee657)
    embed.add_field(name=":wave: **Привет дорогой друг.** :wave:", value="Если ты тут значит тебя приняли,\n чтобы узнать айпи напиши - $ip", inline=True)
    embed.add_field(name="**Немного о сервере:**", value="Нету приватов, нету доната, свобода действий, не ограниченая территория.", inline=False)
    embed.add_field(name="**Узнать все команды:**", value="$Помощь.", inline=False)
    embed.add_field(name="**Пожертвования:**", value="Если у вас появилось желание помочь серверу\n просто напишите - $donate", inline=False)
    embed.set_footer(text="Все права на бота пренадлежат: {0}".format(botconfig.BOT_AUTHOR)) # Подвал сообщения

    await ctx.send(embed=embed)

@bot.command()
async def ip(ctx):
    embed = discord.Embed(title="**IP - адрес и версия**", description="Удачи тебе, некогда не опускай руки", color=0xeee657)
    embed.add_field(name="IP и версия", value="IP - {0}\nВерсия - {1}".format(botconfig.server_ip, botconfig.server_version), inline=True)
    embed.set_footer(text="Все права на бота пренадлежат: {0}".format(botconfig.BOT_AUTHOR)) # Подвал сообщения
    await ctx.author.send(embed=embed)

@bot.command()
async def donate(ctx):
    embed = discord.Embed(title="**Реквизиты**", description="Места куда можно скинуть денюжку.", color=0xeee657)
    embed.add_field(name="**Реквизиты**", value="QIWI - {0}\nWebMoney - {1}".format(botconfig.donate_qiwi, botconfig.donate_webmoney), inline=True)
    embed.set_footer(text="Все права на бота пренадлежат: {0}".format(botconfig.BOT_AUTHOR)) # Подвал сообщения
    await ctx.author.send(embed=embed)
    
@bot.command()
async def cat(ctx):
    await ctx.send("Вот вам кот: https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def ver(ctx):
    embed = discord.Embed(title="**Версия бота**", description=" ", color=0xeee657)
    embed.add_field(name="**Последняя версия**", value="Версия - {0}".format(botconfig.version), inline=True)
    embed.set_footer(text="Все права на бота пренадлежат: {0}".format(botconfig.BOT_AUTHOR)) # Подвал сообщения
    await ctx.send(embed=embed)
    
token = os.environ.get('BOT_TOKEN')
bot.run(str(token))
