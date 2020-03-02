""" Importing Module"""
import discord
from discord.ext import commands
from discord import utils

import os, sys
import random
from random import choice
import asyncio

import botconfig

""" Variable """
green = 0x00ff00 # color green for start
red = 0xff0000 # color red for error 
orange = 0xff8000 # color orange for custom

""" Structure """
sys.path.insert(0, '..') 

""" Setting """
client = commands.Bot(command_prefix=botconfig.PREFIX_COMMAND) # Префикс для команд 

client.remove_command('help') # Удаляет команду help

<<<<<<< HEAD
# Error
# @add_event.error
# async def add_event_error(ctx, error, amount = 1):
#     if isinstance(error, commands.errors.MissingRequiredArgument):
#         await ctx.channel.purge(limit=amount)
#         await ctx.send(embed=discord.Embed(description=f'{ctx.author.name}, вы не ввели свой ник!! ``.add_event [Ваш ник]``', color=red), delete_after=60)

# @list_event.error
# async def list_event_error(ctx, error, amount = 1):
#     if isinstance(error, commands.errors.MissingPermissions):
#         await ctx.channel.purge(limit=amount)
#         await ctx.send(embed=discord.Embed(description=f'{ctx.author.name}, у вас нету прав чтоб использывать эту функцию!', color=red), delete_after=60)

""" Join Cogs """
# client.load_extension('cogs.EventGiveRoles') # Выдача ролей
client.load_extension('cogs.EventGlobal') # Глобальные ивенты
client.load_extension('cogs.CommandHelp') # Команды помощи
client.load_extension('cogs.CommandGame') # Игровые команды
client.load_extension('cogs.CommandUser') # Пользовательские команды

""" RUN """  
=======
# client.event

@client.event
async def on_ready(): # Когда бот запущен и готов к работе
    channel = client.get_channel(botconfig.channel_start_bot_message) # Чат в который кидает данные о боте
    status= choice(botconfig.BOT_STATUS) # Рандомизирует статус с botconfig
    activity = activity = discord.Game(name=status) # Задает статус
    await client.change_presence(status=discord.Status.idle, activity=activity) # Применяет статус
    embed = discord.Embed(title="**Енот Бот** запущен", description="", color=green) # Создает красивый вывод с заголовком title и цветом green 
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url) # Задает автора name и аватар бота icon_url
    embed.add_field(name='**Статус**', value=f"Статус бота - **{status}**.", inline=True) # Создает строку
    embed.add_field(name='**Статус**', value=f"Все статусы - **{botconfig.BOT_STATUS}**.", inline=True) # Создает строку
    embed.add_field(name='**Версия**', value=f'Версия - **{botconfig.version}**', inline=False) # Создает красивый вывод с заголовком title и цветом green 
    embed.add_field(name='**Все хорошо**', value='Все функции работают хорошо!', inline=False) # Создает строку
    embed.set_footer(text=f"Все права на бота пренадлежат: {botconfig.BOT_AUTHOR}") # Подвал сообщения
    print("Ready? Gooo!") # Пишет сообщение в консоль что бот запущен
    await channel.send(embed=embed, delete_after=180) # Отправляет сообщение а потому удалит после 180 секунд

@client.event
async def on_member_join(member): # Когда заходит новый пользователь
    channel = client.get_channel(botconfig.channel_message_join) # Чат в который будет оправляться сообщение о новых участниках
    print(f"{member.name}, присоединился к нам!") # Пишет в консоль о новом учатнике
    await channel.send(embed=discord.Embed(description= f'Пользователь ``{member.name}``, присоединился к нам!', color=orange)) # Пишет в чат сообщение
    await member.send(embed=discord.Embed(description=f':wave: Привет {member.name} тебя приняли :tada: :tada: , чтобы знать все мои команды напиши ``{botconfig.PREFIX_COMMAND}{botconfig.help_private_message_onejoin}`` в любой доступный чат, '
    f'а если нужна версия и IP-Адрес сервера напиши ``{botconfig.PREFIX_COMMAND}{botconfig.ip_private_message_onejoin}``', color=orange)) # Пишет новому пользователю в лс

# client.command
# Fun and test   No comments

@client.command() 
async def say(ctx, amount = 1): 
    await ctx.channel.purge(limit = amount)
    author = ctx.message.author
    say_at_me = input(f"Введите сообщение через консоль для {author}: ")
    await ctx.send(f'{author.mention}, вам посылка из консоли - `{say_at_me}`') 

@client.command()
async def say_m(ctx, member: discord.Member, amount = 1):
    await ctx.channel.purge(limit = amount)
    author = ctx.message.author
    say_at_me = input(f"Введите сообщение через консоль для {member} в лс: ")
    await member.send(f'{author.mention}, вам посылка из консоли - `{say_at_me}`')

# Functions

@client.command(aliases=["помощь", "Help", "help"]) # Команда Помощь работает также с...
async def Помощь(ctx): # Создает команду
    embed = discord.Embed(title="Все команды **Енот Бот**", description="", color=orange) # Создает красивый вывод с заголовком title и цветом green 
    embed.add_field(name=f'**{botconfig.PREFIX_COMMAND}Сервер**', value="Информация о сервере.", inline=False) # Создает строку
    embed.add_field(name=f'**{botconfig.PREFIX_COMMAND}ip**', value="IP-Адрес и версия.", inline=False) # Создает строку
    embed.add_field(name=f'**{botconfig.PREFIX_COMMAND}donate**', value="Пожертвования для сервера.", inline=False) # Создает строку
    embed.add_field(name=f'**{botconfig.PREFIX_COMMAND}cat**', value="Отправляет гифку кота =D.", inline=False) # Создает строку
    embed.add_field(name=f'**{botconfig.PREFIX_COMMAND}ver**', value="Узнать версию бота.", inline=False) # Создает строку
    embed.add_field(name=f'**{botconfig.PREFIX_COMMAND}шар**', value="Отвечает на заданый вопрос.", inline=False) # Создает строку
    embed.add_field(name=f'**{botconfig.PREFIX_COMMAND}add_event** [Ваш ник]', value="Добавить себя в проходящий ивент.", inline=False) # Создает строку
    embed.set_footer(text=f"Все права на бота пренадлежат: {botconfig.BOT_AUTHOR}") # Подвал сообщения
    await ctx.send(embed=embed, delete_after=300) # 

@client.command(aliases = ["предложение", "Sentence", "Предложение"]) # Команда sentence работает также с...
async def sentence(ctx, *, arg): # Создает команду
    author = ctx.message.author # Инициализирует автора
    channel_log = client.get_channel(botconfig.channel_log) # Лог чат
    await ctx.message.add_reaction('✅') # Добавляет лайк
    await ctx.message.add_reaction('❎') # Добавляет дизлайк
    await ctx.send(embed=discord.Embed(description=f'{author.name}, спасибо за вашу идею.', color=orange), delete_after=30) # Отправляет сообщение в чат
    await channel_log.send(embed=discord.Embed(description=f'Пользователь {author} преложил идею: \n``{arg}``', color=orange)) # отправляет сообение в лог чат

@client.command(aliases = ["сервер", "серв", "server", "Server"]) # Информация о сервере рабоает также с командами...
async def Сервер(ctx):
    guild = ctx.guild
    embed = discord.Embed(title=f"Сервер: **{guild.name}**", description="**Енот Бот** был сделан специально для этого сервера.", color=orange) # Создает строку
    embed.add_field(name=":wave: **Привет дорогой друг.** :wave:", value=f"Если ты тут значит тебя приняли,\n чтобы узнать айпи напиши - {botconfig.PREFIX_COMMAND}ip", inline=True) # Создает строку
    embed.add_field(name="Людей на сервере", value=f"{guild.member_count}", inline=False)
    embed.add_field(name="**Немного о сервере:**", value="Нету приватов, нету доната, свобода действий, не ограниченая территория.", inline=False) # Создает строку
    embed.add_field(name="**Узнать все команды:**", value=f"{botconfig.PREFIX_COMMAND}Помощь.", inline=False) # Создает строку
    embed.add_field(name="**Пожертвования:**", value=f"Если у вас появилось желание помочь серверу\n просто напишите - {botconfig.PREFIX_COMMAND}donate", inline=False) # Создает строку
    embed.set_footer(text=f"Все права на бота пренадлежат: {botconfig.BOT_AUTHOR}") # Подвал сообщения
    await ctx.send(embed=embed, delete_after=300) # Отправляет сообщение а потому удалит после 300 секунд

@client.command(aliases=["айпи", "ип", "Айпи", "Ип"]) # Команда ip работает также с...
async def ip(ctx): # Создает команду
    channel_msg = ctx.message.channel
    channel_black = client.get_channel(botconfig.black_list_channel)
    if channel_msg not in channel_black:
        embed = discord.Embed(title="**IP - адрес и версия**", description="Удачи тебе, некогда не опускай руки", color=orange) # 
        embed.add_field(name="IP и версия", value=f"IP - {botconfig.server_ip}\nВерсия - {botconfig.server_version}", inline=True) # 
        embed.set_footer(text=f"Все права на бота пренадлежат: {botconfig.BOT_AUTHOR}") # Подвал сообщения
        await ctx.author.send(embed=embed) # 
    else:
        await channel.send(embed=discord.Embed(description=f'{member.name}, нельзя сюда вводить эту команду', color=orange))

@client.command(aliases=["донат", "Донат", "Donate"]) # 
async def donate(ctx): # Создает команду
    embed = discord.Embed(title="**Реквизиты**", description="Места куда можно скинуть денюжку.", color=orange) # 
    embed.add_field(name="**Реквизиты**", value=f"QIWI - {botconfig.donate_qiwi}\nWebMoney - {botconfig.donate_webmoney}", inline=True) # 
    embed.set_footer(text=f"Все права на бота пренадлежат: {botconfig.BOT_AUTHOR}") # Подвал сообщения
    await ctx.author.send(embed=embed) # 
    
@client.command(aliases = ["кот", "мешок"]) # 
async def cat(ctx): # Создает команду
    r_cat_gif = choice(botconfig.cat_gif) # 
    await ctx.send(r_cat_gif, delete_after=43200) # 

@client.command(aliases = ["версия", "Версия", "Ver"]) # 
async def ver(ctx): # Создает команду
    embed = discord.Embed(title="**Версия бота**", color=orange) # 
    embed.add_field(name="**Последняя версия**", value=f"Версия - {botconfig.version}", inline=True) # 
    embed.set_footer(text=f"Все права на бота пренадлежат: {botconfig.BOT_AUTHOR}") # Подвал сообщения
    await ctx.send(embed=embed, delete_after=300) # 

@client.command(aliases = ["ball", "Ball", "Шар"]) # 
async def шар(ctx): # Создает команду
    r_ball = choice(botconfig.ball) # 
    await ctx.send( embed = discord.Embed(description=f'{ctx.message.author.name}, Знаки говорят - **{ r_ball }**.', color=orange)) # 

@client.command() # 
async def add_event(ctx, arg1, amount=1): # Создает команду
    await ctx.channel.purge(limit = amount)
    author = ctx.message.author
    for x in [event_list]:
        if author not in x:
            event_list.extend([author, arg1])
            player_event_list = len(event_list)
            player_event_list = int(player_event_list / 2)
            embed = discord.Embed(title='Ивенты', color=orange)
            embed.add_field(name='Вы были добавлены в список для проведение ивента',value='Спасибо',inline=True)
            embed.add_field(name='Список участников.', value=f'В списке участников находиться {player_event_list} участник(ков) ивента.')
            embed.set_footer(text=f"Все права на бота пренадлежат: {botconfig.BOT_AUTHOR}") # Подвал сообщения
            await ctx.send(embed=embed, delete_after=300)
        else:
            await ctx.send(embed=discord.Embed(description=f'{author.name}, вы уже есть в списке участников ивента.', color=red), delete_after=300)

@client.command() # 
@commands.has_permissions(administrator=True) # 
async def list_event(ctx, amount=1): # Создает команду
    await ctx.channel.purge(limit=amount)
    author_bot = client.get_user(botconfig.author_bot)
    player_event_list = len(event_list)
    player_event_list = int(player_event_list / 2)
    print(event_list)
    await ctx.send(embed=discord.Embed(description=f'В списке участников находиться {player_event_list} участник(ков) ивента!', color=orange), delete_after=300)
    await author.send(embed=discord.Embed(description=f'Вот список игроков на ивент: {event_list}'))

@client.command(aliases = ["розыгрыш"]) # 
async def Розыгрыш(ctx): # Создает команду
    author = ctx.message.author
    for x in [raffle]: # 
        if author not in x: # 
            raffle.extend([author]) # 
            player_raffle = len(raffle) # 
            embed = discord.Embed(title='Розыгрыш!', color=orange) # 
            embed.add_field(name='Спасибо!',value='Вы были добавлены в список участников розыгрыша!',inline=True) # 
            embed.add_field(name=f'Список участников.', value='В списке участников находиться {} участник(ков) розыгрыша.'.format(player_raffle)) # 
            embed.set_footer(text=f"Все права на бота пренадлежат: {botconfig.BOT_AUTHOR}") # Подвал сообщения
            await ctx.author.send(embed=embed) # 
        else:
            await ctx.send(embed=discord.Embed(description=f'{author.name}, вы уже есть в списке участников розыгрыша!', color=red)) # 

@client.command() # 
@commands.has_permissions(administrator=True) # 
async def start_raffle(ctx, amount=1): # Создает команду
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

@client.command(aliases = ["код", "Код", "Code"]) # 
async def code(ctx, arg1, amount=1): # Создает команду
    await ctx.channel.purge(limit=amount) # 
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
                await author.send(embed=discord.Embed(description=f'{author.name}, вы уже вводили этот код!!', color=red), delete_after=300)
    else:
        await author.send(embed=discord.Embed(description='Вы ввели не существующий код!!', color=red), delete_after=300)

# Request Accept and Refuse(Отказать)

# @client.command(aliases = ["request", "Заявка", "заявка"])
# async def Request(ctx, *, arg):
#    author = ctx.message.author
#    channel = ctx.message.channel
#    channel_white = client.get_channel(botconfig.channel_request_white)
#    channel_admin = client.get_channel(botconfig.channel_admin)
#    if channel == channel_white:
#        await ctx.send(embed=discord.Embed(description=f'{author.name}, заявка принята, ожидайте!', color=orange), delete_after=60)
#        embed = discord.Embed(title='Новая заявка!', color=orange)
#        embed.add_field(name='Автор:', value=f'Заявку написал {author}.', inline=False)
#        embed.add_field(name='Вот заявка', value=f'``{arg}``', inline=False)
#        embed.add_field(name='Принять', value=f'Чтоб принять заявку напишите: ``{botconfig.PREFIX_COMMAND}принять [Упоминание участника]`` в #заявка', inline=True )
#        embed.add_field(name='Отказать', value=f'Чтоб отказать заявку напишите: ``{botconfig.PREFIX_COMMAND}отказать [Упоминание участника]`` в #заявка', inline=True )
#        embed.set_footer(text=f"Все права на бота пренадлежат: {botconfig.BOT_AUTHOR}") # Подвал сообщения#
# 
#         await channel_admin.send(embed=embed) # В модераторскую
#     else:
#         await ctx.send(embed=discord.Embed(description=f'{author.name}, заявку нельзя писать в этот чат!', color=red), delete_after=60) 
# 
# @client.command(aliases = ["accept", "Принять", "принять"])
# @commands.has_permissions(manage_roles=True)
# async def Accept(ctx, member: discord.Member):
#     role_add = utils.get(member.guild.roles, id=botconfig.roll_add_accept)
#     role_rem = utils.get(member.guild.roles, id=botconfig.roll_add)
#     channel = client.get_channel(botconfig.channel_start_bot_message) 
#     print(f'Принят {member}')
#     await member.add_roles(role_add)
#     await member.remove_roles(role_rem)
#     await channel.send(embed=discord.Embed(description=f'{member.name}, был принят! :tada: :tada:', color=orange))
# 
#@client.command(aliases = ["denny", "Отказать", "отказать"])
#@commands.has_permissions(manage_roles=True)
#async def Denny(ctx, member: discord.Member):
#    await member.send(embed=discord.Embed(description=f':wave: Привет {member.name} тебя не приняли :frowning2: :frowning2: , попробуй ещё ', color=orange))
#
#@client.command(aliases = ["заявка_помощь", "Request_help", "request_help"])
#async def Заявка_помощь(ctx):
#    author = ctx.message.author
#    channel = client.get_channel(botconfig.channel_request)
#    await ctx.send(f'{author.mention}, заявку можна найти в {channel.mention}!', delete_after=120)

# Error

@add_event.error
async def add_event_error(ctx, error, amount = 1):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.channel.purge(limit=amount)
        await ctx.send(embed=discord.Embed(description=f'{ctx.author.name}, вы не ввели свой ник!! ``.add_event [Ваш ник]``', color=red), delete_after=60)

@list_event.error
async def list_event_error(ctx, error, amount = 1):
    if isinstance(error, commands.errors.MissingPermissions):
        await ctx.channel.purge(limit=amount)
        await ctx.send(embed=discord.Embed(description=f'{ctx.author.name}, у вас нету прав чтоб использывать эту функцию!', color=red), delete_after=60)

@Request.error
async def Request_error(ctx, error, amount = 1):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.channel.purge(limit=amount)
        await ctx.send(embed=discord.Embed(description=f'{ctx.author.name}, вы не написали заявку!! Чтобы узнать вопросы заявки напишите ``.заявка_помощь``', color=red), delete_after=60)

@Accept.error
async def Accept_error(ctx, error, amount = 1):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.channel.purge(limit=amount)
        await ctx.send(embed=discord.Embed(description=f'{ctx.author.name}, вы не указали участника!! ``.принять [Упоминание участника]``', color=red), delete_after=60)
    elif isinstance(error, commands.errors.MissingPermissions):
        await ctx.channel.purge(limit=amount)
        await ctx.send(embed=discord.Embed(description=f'{ctx.author.name}, у вас нету прав чтоб использывать эту функцию!', color=red), delete_after=60)

@Denny.error
async def Denny_error(ctx, error, amount = 1):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.channel.purge(limit=amount)
        await ctx.send(embed=discord.Embed(description=f'{ctx.author.name}, вы не указали участника!! ``.принять [Упоминание участника]``', color=red), delete_after=60)
    elif isinstance(error, commands.errors.MissingPermissions):
        await ctx.channel.purge(limit=amount)
        await ctx.send(embed=discord.Embed(description=f'{ctx.author.name}, у вас нету прав чтоб использывать эту функцию!', color=red), delete_after=60)

# RUN
    
>>>>>>> parent of 6c8fcf4... Update botmain.py
token = os.environ.get('BOT_TOKEN')
client.run(str(token))