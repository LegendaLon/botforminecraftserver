import discord
from discord.ext import commands
import botconfig
import os

# Setting

client = commands.Bot(command_prefix=botconfig.PREFIX_COMMAND) # Префикс для команд 

client.remove_command('help') # Удаляет команду help

# client.event

# client.command

@client.command(pass_context = True)
async def say(ctx, amount = 1):
    await ctx.channel.purge( limit = amount)
    author = ctx.message.author
    say_at_me = input("Введите сообщение через консоль для {}: ".format(author))
    await ctx.send('{}, вам посылка из консоли - `{}`'.format(author.mention, say_at_me))

@client.command(pass_context = True)
async def say_m(ctx, member: discord.Member, amount = 1):
    await ctx.channel.purge( limit = amount)
    author = ctx.message.author
    say_at_me = input("Введите сообщение через консоль для {} в лс: ".format(member))
    await member.send('{}, вам посылка из консоли - `{}`'.format(author.mention, say_at_me))

@client.command(pass_context = True)
async def Помощь(ctx):
    embed = discord.Embed(title="Все команды **Енот Бот**", description="", color=0xeee657)
    embed.add_field(name='**{}Сервер**'.format(botconfig.PREFIX_COMMAND), value="Информация о сервере.", inline=False)
    embed.add_field(name='**{}ip**'.format(botconfig.PREFIX_COMMAND), value="IP-Адрес и версия.", inline=False)
    embed.add_field(name='**{}donate**'.format(botconfig.PREFIX_COMMAND), value="Пожертвования для сервера.", inline=False)
    embed.add_field(name='**{}cat**'.format(botconfig.PREFIX_COMMAND), value="Отправляет гифку кота =D.", inline=False)
    embed.add_field(name='**{}ver**'.format(botconfig.PREFIX_COMMAND), value="Узнать версию бота.", inline=False)
    embed.set_footer(text="Все права на бота пренадлежат: {0}".format(botconfig.BOT_AUTHOR)) # Подвал сообщения
    await ctx.send(embed=embed)

@client.command(pass_context = True)
async def Сервер(ctx):
    embed = discord.Embed(title="Сервер: **Legend of The World**", description="**Енот Бот** был сделан специально для этого сервера.", color=0xeee657)
    embed.add_field(name=":wave: **Привет дорогой друг.** :wave:", value="Если ты тут значит тебя приняли,\n чтобы узнать айпи напиши - $ip", inline=True)
    embed.add_field(name="**Немного о сервере:**", value="Нету приватов, нету доната, свобода действий, не ограниченая территория.", inline=False)
    embed.add_field(name="**Узнать все команды:**", value="{}Помощь.".format(botconfig.PREFIX_COMMAND), inline=False)
    embed.add_field(name="**Пожертвования:**", value="Если у вас появилось желание помочь серверу\n просто напишите - {}donate".format(botconfig.PREFIX_COMMAND), inline=False)
    embed.set_footer(text="Все права на бота пренадлежат: {0}".format(botconfig.BOT_AUTHOR)) # Подвал сообщения

    await ctx.send(embed=embed)

@client.command(pass_context = True)
async def ip(ctx, amount = 1):
    await ctx.channel.purge( limit = amount)
    embed = discord.Embed(title="**IP - адрес и версия**", description="Удачи тебе, некогда не опускай руки", color=0xeee657)
    embed.add_field(name="IP и версия", value="IP - {0}\nВерсия - {1}".format(botconfig.server_ip, botconfig.server_version), inline=True)
    embed.set_footer(text="Все права на бота пренадлежат: {0}".format(botconfig.BOT_AUTHOR)) # Подвал сообщения
    await ctx.author.send(embed=embed)

@client.command(pass_context = True)
async def donate(ctx, amount = 1):
    await ctx.channel.purge( limit = amount)
    embed = discord.Embed(title="**Реквизиты**", description="Места куда можно скинуть денюжку.", color=0xeee657)
    embed.add_field(name="**Реквизиты**", value="QIWI - {0}\nWebMoney - {1}".format(botconfig.donate_qiwi, botconfig.donate_webmoney), inline=True)
    embed.set_footer(text="Все права на бота пренадлежат: {0}".format(botconfig.BOT_AUTHOR)) # Подвал сообщения
    await ctx.author.send(embed=embed)
    
@client.command(pass_context = True)
async def cat(ctx):
    await ctx.send("Вот вам кот: https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@client.command(pass_context = True)
async def ver(ctx):
    embed = discord.Embed(title="**Версия бота**", color=0xeee657)
    embed.add_field(name="**Последняя версия**", value="Версия - {0}".format(botconfig.version), inline=True)
    embed.set_footer(text="Все права на бота пренадлежат: {0}".format(botconfig.BOT_AUTHOR)) # Подвал сообщения
    await ctx.send(embed=embed)
    
token = os.environ.get('BOT_TOKEN')
bot.run(str(token))
