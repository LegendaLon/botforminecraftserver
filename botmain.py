# importing module

import discord
from discord.ext import commands
import botconfig
import random
import os

# Variable

event_list = []
raffle = []
code_stop = []
green = 0x00ff00 # color green for start
red = 0xff0000 # color red for error 
orange = 0xff8000 # color orange for custom

# Var variable



# Setting

client = commands.Bot(command_prefix=botconfig.PREFIX_COMMAND) # Префикс для команд 

client.remove_command('help') # Удаляет команду help

# client.event

@client.event
async def on_ready(): # Когда бот запущен и готов к работе
    channel = client.get_channel(botconfig.channel_start_bot_message)
    activity = activity = discord.Game(name=botconfig.BOT_STATUS) # Задает статус, берет их из botconfig.py
    await client.change_presence(status=discord.Status.idle, activity=activity) # Применяет статус
    print("Ready! Gooo!") # Пишет сообщение в консоль что бот запущен
    embed = discord.Embed(title="**Енот Бот** запущен", description="", color=green)
    embed.add_field(name='**Статус**', value="Статус бота - **{}**.".format(botconfig.BOT_STATUS), inline=True)
    embed.add_field(name='**Версия**', value='Версия - **{}**'.format(botconfig.version), inline=True)
    embed.add_field(name='**Все хорошо**', value='Все функции работают хорошо!', inline=True)
    embed.set_footer(text="Все права на бота пренадлежат: {0}".format(botconfig.BOT_AUTHOR)) # Подвал сообщения
    await channel.send(embed=embed)

@client.event
async def on_member_join(member):
    channel = client.get_channel(botconfig.chennel_join_message)
    print("{}, присоединился к нам!".format(member.name))
    await member.send('Привет {}, чтобы знать все мои команды напиши ``{}{}`` в любой доступный чат, а если нужна верся и IP-Адрес сервер напиши ``{}{}``'.format(member.name, botconfig.PREFIX_COMMAND, botconfig.help_private_message_onejoin, botconfig.PREFIX_COMMAND, botconfig.ip_private_message_onejoin))
    await channel.send(embed=discord.Embed(description= f'Пользователь ``{member.name}``, присоединился к нам!'))

# client.command
# Fun and test

@client.command(pass_context=True)
async def say(ctx, amount = 1):
    await ctx.channel.purge(limit = amount)
    author = ctx.message.author
    say_at_me = input("Введите сообщение через консоль для {}: ".format(author))
    await ctx.send('{}, вам посылка из консоли - `{}`'.format(author.mention, say_at_me))

@client.command(pass_context=True)
async def say_m(ctx, member: discord.Member, amount = 1):
    await ctx.channel.purge(limit = amount)
    author = ctx.message.author
    say_at_me = input("Введите сообщение через консоль для {} в лс: ".format(member))
    await member.send('{}, вам посылка из консоли - `{}`'.format(author.mention, say_at_me))

# Functions

@client.command(pass_context=True)
async def Помощь(ctx, amount = 1): # Clone 193
    await ctx.channel.purge(limit = amount)
    embed = discord.Embed(title="Все команды **Енот Бот**", description="", color=orange)
    embed.add_field(name='**{}Сервер**'.format(botconfig.PREFIX_COMMAND), value="Информация о сервере.", inline=False)
    embed.add_field(name='**{}ip**'.format(botconfig.PREFIX_COMMAND), value="IP-Адрес и версия.", inline=False)
    embed.add_field(name='**{}donate**'.format(botconfig.PREFIX_COMMAND), value="Пожертвования для сервера.", inline=False)
    embed.add_field(name='**{}cat**'.format(botconfig.PREFIX_COMMAND), value="Отправляет гифку кота =D.", inline=False)
    embed.add_field(name='**{}ver**'.format(botconfig.PREFIX_COMMAND), value="Узнать версию бота.", inline=False)
    embed.add_field(name='**{}add_event** [Ваш ник]'.format(botconfig.PREFIX_COMMAND), value="Добавить себя в проходящий ивент.", inline=False)
    embed.set_footer(text="Все права на бота пренадлежат: {0}".format(botconfig.BOT_AUTHOR)) # Подвал сообщения
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def Сервер(ctx, amount = 1):
    await ctx.channel.purge(limit = amount)
    embed = discord.Embed(title="Сервер: **Legend of The World**", description="**Енот Бот** был сделан специально для этого сервера.", color=orange)
    embed.add_field(name=":wave: **Привет дорогой друг.** :wave:", value="Если ты тут значит тебя приняли,\n чтобы узнать айпи напиши - $ip", inline=True)
    embed.add_field(name="**Немного о сервере:**", value="Нету приватов, нету доната, свобода действий, не ограниченая территория.", inline=False)
    embed.add_field(name="**Узнать все команды:**", value="{}Помощь.".format(botconfig.PREFIX_COMMAND), inline=False)
    embed.add_field(name="**Пожертвования:**", value="Если у вас появилось желание помочь серверу\n просто напишите - {}donate".format(botconfig.PREFIX_COMMAND), inline=False)
    embed.set_footer(text="Все права на бота пренадлежат: {0}".format(botconfig.BOT_AUTHOR)) # Подвал сообщения

    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def ip(ctx, amount = 1):
    await ctx.channel.purge(limit = amount)
    embed = discord.Embed(title="**IP - адрес и версия**", description="Удачи тебе, некогда не опускай руки", color=orange)
    embed.add_field(name="IP и версия", value="IP - {0}\nВерсия - {1}".format(botconfig.server_ip, botconfig.server_version), inline=True)
    embed.set_footer(text="Все права на бота пренадлежат: {0}".format(botconfig.BOT_AUTHOR)) # Подвал сообщения
    await ctx.author.send(embed=embed)

@client.command(pass_context=True)
async def donate(ctx, amount = 1):
    await ctx.channel.purge(limit = amount)
    embed = discord.Embed(title="**Реквизиты**", description="Места куда можно скинуть денюжку.", color=orange)
    embed.add_field(name="**Реквизиты**", value="QIWI - {0}\nWebMoney - {1}".format(botconfig.donate_qiwi, botconfig.donate_webmoney), inline=True)
    embed.set_footer(text="Все права на бота пренадлежат: {0}".format(botconfig.BOT_AUTHOR)) # Подвал сообщения
    await ctx.author.send(embed=embed)
    
@client.command(pass_context=True)
async def cat(ctx, amount = 1):
    await ctx.channel.purge(limit = amount)
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@client.command(pass_context=True)
async def ver(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(title="**Версия бота**", color=orange)
    embed.add_field(name="**Последняя версия**", value="Версия - {0}".format(botconfig.version), inline=True)
    embed.set_footer(text="Все права на бота пренадлежат: {0}".format(botconfig.BOT_AUTHOR)) # Подвал сообщения
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def add_event(ctx, arg1, amount=1):
    await ctx.channel.purge(limit = amount)
    author = ctx.message.author
    for x in [event_list]:
        if author not in x:
            event_list.extend([author, arg1])
            player_event_list = len(event_list)
            player_event_list = player_event_list / 2
            player_event_list = int(player_event_list)
            embed = discord.Embed(title='Ивенты', color=orange)
            embed.add_field(name='Вы были добавлены в список для проведение ивента',value='Спасибо',inline=True)
            embed.add_field(name='Список участников.', value='В списке участников находиться {} участник(ков) ивента.'.format(player_event_list))
            embed.set_footer(text="Все права на бота пренадлежат: {0}".format(botconfig.BOT_AUTHOR)) # Подвал сообщения
            await ctx.send(embed=embed)
        else:
            await ctx.send(embed=discord.Embed(description='{}, вы уже есть в списке участников ивента.'.format(author.name), color=red))

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def list_event(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    player_event_list = len(event_list)
    player_event_list = player_event_list / 2
    player_event_list = int(player_event_list)
    print(event_list)
    await ctx.send(embed=discord.Embed(description='В списке участников находиться {} участник(ков) ивента!'.format(player_event_list), color=orange))

@client.command(pass_context=True)
async def Розыгрыш(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    author = ctx.message.author
    for x in [raffle]:
        if author not in x:
            raffle.extend([author])
            player_raffle = len(raffle)
            embed = discord.Embed(title='Розыгрыш!', color=orange)
            embed.add_field(name='Спасибо!',value='Вы были добавлены в список участников розыгрыша!',inline=True)
            embed.add_field(name='Список участников.', value='В списке участников находиться {} участник(ков) розыгрыша.'.format(player_raffle))
            embed.set_footer(text="Все права на бота пренадлежат: {0}".format(botconfig.BOT_AUTHOR)) # Подвал сообщения
            await ctx.author.send(embed=embed)
        else:
            await ctx.send(embed=discord.Embed(description='{}, вы уже есть в списке участников розыгрыша!'.format(author.name), color=red))

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def start_raffle(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    author = ctx.message.author
    len_raffle = len(raffle)
    random_raffle = random.randint(1,len_raffle)
    embed = discord.Embed(title='Розыгрыш!', color=orange)
    embed.add_field(name='Победитель',value='Сейчас решиться кто станет победителем!',inline=True)
    embed.add_field(name='Нечего не подкручено!', value='Все решает бот!!')
    embed.add_field(name='Победитель...', value='Иии.. Это - {}'.format(raffle[random_raffle]))
    embed.set_footer(text="Все права на бота пренадлежат: {0}".format(botconfig.BOT_AUTHOR)) # Подвал сообщения
    await ctx.send(embed=embed)
    await author.send('Победитель {}'.format(raffle[random_raffle]))

@client.command(pass_context=True)
async def code(ctx, arg1, amount=1):
    await ctx.channel.purge(limit=amount)
    author = ctx.message.author
    bot_author = client.get_user(518766156790890496)
    if arg1 == botconfig.code1:
        for x in [code_stop]:
            if author not in x:
                code_stop.append(author)
                print(code_stop)
                await bot_author.send(embed=discord.Embed(description='{}, ввел код {}, {}!!'.format(author, arg1, botconfig.code1_comment), color=orange))
                await author.send(embed=discord.Embed(description='{}, вы ввели верный код!!'.format(author.name), color=orange))
            else:
                await author.send(embed=discord.Embed(description='{}, вы уже вводили этот код!!'.format(author.name), color=red))
    else:
        await author.send(embed=discord.Embed(description='Вы ввели не существующий код!!', color=red))

# Error

@add_event.error
async def add_event_error(ctx, error, amount = 1):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.channel.purge(limit=amount)
        await ctx.send(embed=discord.Embed(description='{}, вы не ввели свой ник!! ``.add_event [Ваш ник]``'.format(ctx.author.name), color=red))

@list_event.error
async def list_event_error(ctx, error, amount = 1):
    if isinstance(error, commands.errors.MissingPermissions):
        await ctx.channel.purge(limit=amount)
        await ctx.send(embed=discord.Embed(description='{}, у вас нету прав чтоб использывать эту функцию!'.format(ctx.author.name), color=red))

# Clone command

@client.command(pass_context=True)
async def помощь(ctx, amount = 1):
    await ctx.channel.purge( limit = amount)
    embed = discord.Embed(title="Все команды **Енот Бот**", description="", color=orange)
    embed.add_field(name='**{}Сервер**'.format(botconfig.PREFIX_COMMAND), value="Информация о сервере.", inline=False)
    embed.add_field(name='**{}ip**'.format(botconfig.PREFIX_COMMAND), value="IP-Адрес и версия.", inline=False)
    embed.add_field(name='**{}donate**'.format(botconfig.PREFIX_COMMAND), value="Пожертвования для сервера.", inline=False)
    embed.add_field(name='**{}cat**'.format(botconfig.PREFIX_COMMAND), value="Отправляет гифку кота =D.", inline=False)
    embed.add_field(name='**{}ver**'.format(botconfig.PREFIX_COMMAND), value="Узнать версию бота.", inline=False)
    embed.set_footer(text="Все права на бота пренадлежат: {0}".format(botconfig.BOT_AUTHOR)) # Подвал сообщения
    await ctx.send(embed=embed)

# RUN
    
token = os.environ.get('BOT_TOKEN')
client.run(str(token))
