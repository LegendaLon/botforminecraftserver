# importing module

import discord
from discord.ext import commands

import os
import random
from random import choice
import asyncio

import botconfig

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
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    embed.add_field(name='**Статус**', value=f"Статус бота - **{botconfig.BOT_STATUS}**.", inline=True)
    embed.add_field(name='**Версия**', value=f'Версия - **{botconfig.version}**', inline=True)
    embed.add_field(name='**Все хорошо**', value='Все функции работают хорошо!', inline=True)
    embed.set_footer(text=f"Все права на бота пренадлежат: {botconfig.BOT_AUTHOR}") # Подвал сообщения
    await channel.send(embed=embed, delete_after=180)

@client.event
async def on_member_join(member):
    channel = client.get_channel(botconfig.channel_join_message)
    print(f"{member.name}, присоединился к нам!")
    await member.send(embed=discord.Embed(f'Привет {member.name}, чтобы знать все мои команды напиши ``{botconfig.PREFIX_COMMAND}{botconfig.help_private_message_onejoin}`` в любой доступный чат,' 
        f'а если нужна верся и IP-Адрес сервер напиши ``{botconfig.PREFIX_COMMAND}{botconfig.ip_private_message_onejoin}``', color=orange))
    await channel.send(embed=discord.Embed(description= f'Пользователь ``{member.name}``, присоединился к нам!', color=orange))

# client.command
# Fun and test

@client.command(pass_context=True)
async def say(ctx, amount = 1):
    await ctx.channel.purge(limit = amount)
    author = ctx.message.author
    say_at_me = input(f"Введите сообщение через консоль для {author}: ")
    await ctx.send(f'{author.mention}, вам посылка из консоли - `{say_at_me}`')

@client.command(pass_context=True)
async def say_m(ctx, member: discord.Member, amount = 1):
    await ctx.channel.purge(limit = amount)
    author = ctx.message.author
    say_at_me = input(f"Введите сообщение через консоль для {member} в лс: ")
    await member.send(f'{author.mention}, вам посылка из консоли - `{say_at_me}`')

# Functions

@client.command(pass_context=True, aliases=["помощь", "Help", "help"])
async def Помощь(ctx, amount = 1):
    await ctx.channel.purge(limit = amount)
    embed = discord.Embed(title="Все команды **Енот Бот**", description="", color=orange)
    embed.add_field(name=f'**{botconfig.PREFIX_COMMAND}Сервер**', value="Информация о сервере.", inline=False)
    embed.add_field(name=f'**{botconfig.PREFIX_COMMAND}ip**', value="IP-Адрес и версия.", inline=False)
    embed.add_field(name=f'**{botconfig.PREFIX_COMMAND}donate**', value="Пожертвования для сервера.", inline=False)
    embed.add_field(name=f'**{botconfig.PREFIX_COMMAND}cat**', value="Отправляет гифку кота =D.", inline=False)
    embed.add_field(name=f'**{botconfig.PREFIX_COMMAND}ver**', value="Узнать версию бота.", inline=False)
    embed.add_field(name=f'**{botconfig.PREFIX_COMMAND}add_event** [Ваш ник]', value="Добавить себя в проходящий ивент.", inline=False)
    embed.set_footer(text=f"Все права на бота пренадлежат: {botconfig.BOT_AUTHOR}") # Подвал сообщения
    await ctx.send(embed=embed, delete_after=300)

@client.command(pass_context=True, aliases = ["предложение", "Sentence", "Предложение"])
async def sentence(ctx, *, arg):
    author = ctx.message.author
    channel_log = client.get_channel(botconfig.channel_log)
    await ctx.message.add_reaction('✅')
    await ctx.message.add_reaction('❎')
    await ctx.send(embed=discord.Embed(description=f'{author.name}, спасибо за вашу идею.', color=orange), delete_after=20)
    await channel_log.send(embed=discord.Embed(description=f'Пользователь {author} преложил идею: \n``{arg}``', color=orange))

@client.command(pass_context=True, aliases = ["сервер", "серв", "server", "Server"])
async def Сервер(ctx, amount = 1): 
    await ctx.channel.purge(limit = amount)
    embed = discord.Embed(title="Сервер: **Legend of The World**", description="**Енот Бот** был сделан специально для этого сервера.", color=orange)
    embed.add_field(name=":wave: **Привет дорогой друг.** :wave:", value=f"Если ты тут значит тебя приняли,\n чтобы узнать айпи напиши - {botconfig.PREFIX_COMMAND}ip", inline=True)
    embed.add_field(name="**Немного о сервере:**", value="Нету приватов, нету доната, свобода действий, не ограниченая территория.", inline=False)
    embed.add_field(name="**Узнать все команды:**", value=f"{botconfig.PREFIX_COMMAND}Помощь.", inline=False)
    embed.add_field(name="**Пожертвования:**", value=f"Если у вас появилось желание помочь серверу\n просто напишите - {botconfig.PREFIX_COMMAND}donate", inline=False)
    embed.set_footer(text=f"Все права на бота пренадлежат: {botconfig.BOT_AUTHOR}") # Подвал сообщения

    await ctx.send(embed=embed, delete_after=300)

@client.command(pass_context=True, aliases=["айпи", "ип", "Айпи", "Ип"])
async def ip(ctx, amount = 1):
    await ctx.channel.purge(limit = amount)
    embed = discord.Embed(title="**IP - адрес и версия**", description="Удачи тебе, некогда не опускай руки", color=orange)
    embed.add_field(name="IP и версия", value=f"IP - {botconfig.server_ip}\nВерсия - {botconfig.server_version}", inline=True)
    embed.set_footer(text=f"Все права на бота пренадлежат: {botconfig.BOT_AUTHOR}") # Подвал сообщения
    await ctx.author.send(embed=embed)

@client.command(pass_context=True, aliases=["донат", "Донат", "Donate"])
async def donate(ctx, amount = 1):
    await ctx.channel.purge(limit = amount)
    embed = discord.Embed(title="**Реквизиты**", description="Места куда можно скинуть денюжку.", color=orange)
    embed.add_field(name="**Реквизиты**", value=f"QIWI - {botconfig.donate_qiwi}\nWebMoney - {botconfig.donate_webmoney}", inline=True)
    embed.set_footer(text=f"Все права на бота пренадлежат: {botconfig.BOT_AUTHOR}") # Подвал сообщения
    await ctx.author.send(embed=embed)
    
@client.command(pass_context=True, aliases = ["кот", "мешок"])
async def cat(ctx, amount = 1):
    await ctx.channel.purge(limit=amount)
    cat_gif = [
        "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif", "https://i.gifer.com/VrJ.gif", "https://i.gifer.com/Ah.gif", "https://i.gifer.com/307G.gif",
        "https://i.gifer.com/3p72.gif", "https://i.gifer.com/1g5K.gif", "https://i.gifer.com/9w8.gif", "https://i.gifer.com/FEl8.gif", "https://i.gifer.com/OuUi.gif",  
        "https://i.gifer.com/ZHbd.gif", "https://i.gifer.com/5v1Y.gif", "https://i.gifer.com/2CR.gif", "https://i.gifer.com/ZUyt.gif"
    ] 
    r_cat_gif = choice(cat_gif)
    await ctx.send(r_cat_gif, delete_after=300)
    await asyncio.sleep(300)
    await ctx.message.delete()

@client.command(pass_context=True, aliases = ["версия", "Версия", "Ver"])
async def ver(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(title="**Версия бота**", color=orange)
    embed.add_field(name="**Последняя версия**", value=f"Версия - {botconfig.version}", inline=True)
    embed.set_footer(text=f"Все права на бота пренадлежат: {botconfig.BOT_AUTHOR}") # Подвал сообщения
    await ctx.send(embed=embed, delete_after=300)

@client.command(pass_context=True, aliases = ["ball", "Ball", "Шар"])
async def шар(ctx):
    words = [
        "Да", "Нет", "Возможно", "Скорее всего да", "Скорее всего нет", "Не советую", "Лучше не надо", "Больше да, чем нет", "Больше нет, чем да",
        "Не могу сказать, попробуйте ещё", "На самом деле нет, но для тебя да", "На самом деле да, но для тебя нет", "Лучше не спрашивай", "Сам подумай",
        "Я незнаю, загугли сам", "Однозначно нет", "Однозначно да"
    ]
    r_words = choice(words)
    await ctx.send( embed = discord.Embed(description=f'{ctx.message.author.name}, Знаки говорят - **{ r_words }**.', color=orange), delete_after=300)
    await asyncio.sleep(300)
    await ctx.message.delete()

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
            embed.add_field(name='Список участников.', value=f'В списке участников находиться {player_event_list} участник(ков) ивента.')
            embed.set_footer(text=f"Все права на бота пренадлежат: {botconfig.BOT_AUTHOR}") # Подвал сообщения
            await ctx.send(embed=embed, delete_after=300)
        else:
            await ctx.send(embed=discord.Embed(description=f'{author.name}, вы уже есть в списке участников ивента.', color=red), delete_after=300)

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def list_event(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    author_bot = client.get_user(botconfig.author_bot)
    player_event_list = len(event_list)
    player_event_list = player_event_list / 2
    player_event_list = int(player_event_list)
    print(event_list)
    await ctx.send(embed=discord.Embed(description=f'В списке участников находиться {player_event_list} участник(ков) ивента!', color=orange), delete_after=300)
    await author.send(embed=discord.Embed(description=f'Вот список игроков на ивент: {event_list}'))

@client.command(pass_context=True, aliases = ["розыгрыш"])
async def Розыгрыш(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    author = ctx.message.author
    for x in [raffle]:
        if author not in x:
            raffle.extend([author])
            player_raffle = len(raffle)
            embed = discord.Embed(title='Розыгрыш!', color=orange)
            embed.add_field(name='Спасибо!',value='Вы были добавлены в список участников розыгрыша!',inline=True)
            embed.add_field(name=f'Список участников.', value='В списке участников находиться {} участник(ков) розыгрыша.'.format(player_raffle))
            embed.set_footer(text=f"Все права на бота пренадлежат: {botconfig.BOT_AUTHOR}") # Подвал сообщения
            await ctx.author.send(embed=embed)
        else:
            await ctx.send(embed=discord.Embed(description=f'{author.name}, вы уже есть в списке участников розыгрыша!', color=red))

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
    embed.add_field(name='Победитель...', value=f'Иии.. Это - {raffle[random_raffle]}')
    embed.set_footer(text=f"Все права на бота пренадлежат: {botconfig.BOT_AUTHOR}") # Подвал сообщения
    await ctx.send(embed=embed, delete_after=300)
    await author.send(f'Победитель {raffle[random_raffle]}')

@client.command(pass_context=True, aliases = ["код", "Код", "Code"])
async def code(ctx, arg1, amount=1):
    await ctx.channel.purge(limit=amount)
    author = ctx.message.author
    bot_author = client.get_user(518766156790890496)
    if arg1 == botconfig.code1:
        for x in [code_stop]:
            if author not in x:
                code_stop.append(author)
                print(code_stop)
                await bot_author.send(embed=discord.Embed(description=f'{author}, ввел код {arg}, {botconfig.code1_comment}!!', color=orange))
                await author.send(embed=discord.Embed(description=f'{author.name}, вы ввели верный код!!', color=orange))
            else:
                await author.send(embed=discord.Embed(description=f'{author.name}, вы уже вводили этот код!!', color=red))
    else:
        await author.send(embed=discord.Embed(description='Вы ввели не существующий код!!', color=red))

# Error

@add_event.error
async def add_event_error(ctx, error, amount = 1):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.channel.purge(limit=amount)
        await ctx.send(embed=discord.Embed(description=f'{ctx.author.name}, вы не ввели свой ник!! ``.add_event [Ваш ник]``', color=red))

@list_event.error
async def list_event_error(ctx, error, amount = 1):
    if isinstance(error, commands.errors.MissingPermissions):
        await ctx.channel.purge(limit=amount)
        await ctx.send(embed=discord.Embed(description=f'{ctx.author.name}, у вас нету прав чтоб использывать эту функцию!', color=red))

# RUN
    
token = os.environ.get('BOT_TOKEN')
client.run(str(token))
