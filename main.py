""" Importing Module"""
import discord
from discord.ext import commands
from discord import utils

import os, sys
import random
from random import choice
import asyncio

import botconfig

""" Constans """
green = 0x00ff00 # color green for start
red = 0xff0000 # color red for error 
orange = 0xff8000 # color orange for custom

""" Structure """
sys.path.insert(0, '..') 

""" Setting """
client = commands.Bot(command_prefix=botconfig.PREFIX_COMMAND) # Префикс для команд 

client.remove_command('help') # Удаляет команду help

client.load_extension('cogs.EventGlobal')

""" Code """
@client.event
async def on_ready(): # Когда бот запущен и готов к работе
    channel = client.get_channel(botconfig.channel_start_bot_message) # Чат в который кидает данные о боте
    status= choice(botconfig.BOT_STATUS) # Рандомизирует статус с botconfig
    activity = activity = discord.Game(name=status) # Задает статус
    await client.change_presence(status=discord.Status.idle, activity=activity) # Применяет статус
    print(f"Bot is start, {client.user} ")

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

@client.command(aliases = ["кнб"])
async def rps(ctx, arg1):
	author = ctx.message.author
	x = random.randint(1, 3)
	y = arg1

	""" Lose """
	if x == 1 and y == "ножницы":
		await ctx.send(f"{author.mention} вы выбрали ножнци, а бот - камень! Вы проиграли!")
	if x == 2 and y == "бумага":
		await ctx.send(f"{author.mention} вы выбрали бумагу, а бот - ножницы! Вы проиграли!")
	if x == 3 and y == "камень":
		await ctx.send(f"{author.mention} вы выбрали камень, а бот - бумагу! Вы проиграли!")
	
	""" Won """
	if x == 2 and y == "камень":
		await ctx.send(f"{author.mention} вы выбрали камень, а бот - ножници! Вы выиграли! :tada: ")
	if x == 3 and y == "ножницы":
		await ctx.send(f"{author.mention} вы выбрали ножницы, а бот - бумагу! Вы выиграли! :tada: ")
	if x == 1 and y == "бумага":
		await ctx.send(f"{author.mention} вы выбрали бумагу, а бот - камень! Вы выиграли! :tada: ")
	
	""" Draw """
	if x == 1 and y == "камень":
		await ctx.send(f"{author.mention} вы выбрали камень, а бот - камень! Ничья!")
	if x == 2 and y == "ножницы":
		await ctx.send(f"{author.mention} вы выбрали ножницы, а бот - ножницы! Ничья!")
	if x == 3 and y == "бумага":
		await ctx.send(f"{author.mention} вы выбрали бумагу, а бот - бумагу! Ничья!")

# RUN
token = os.environ.get('BOT_TOKEN')

client.run(str(token))