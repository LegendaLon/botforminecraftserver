import discord
from discord.ext import commands
from botconfig import *
import os

bot = commands.Bot(command_prefix=PREFIX_COMMAND)

bot.remove_command('help') # Удаляет команду help

@bot.event
async def on_ready():
    activity = activity = discord.Game(name=BOT_STATUS) # Задает статус, берет их botconfig.py
    await bot.change_presence(status=discord.Status.idle, activity=activity) # Применяет статус
    print('Бот запущен')

@bot.command()
async def say(ctx):
    say_at_me = input("Введите сообщение через консоль: ")
    await ctx.send(say_at_me)

@bot.command()
async def Помощь(ctx):
    embed = discord.Embed(title="Все команды которые может предоставить **Енот Бот**", description="", color=0xeee657)
    embed.add_field(name='$Сервер', value="Информация о сервере.", inline=False)
    embed.set_footer(text="Все права на бота пренадлежат: Lonely_#1572.") # Подвал сообщения
    await ctx.send(embed=embed)

@bot.command()
async def Сервер(ctx):
    embed = discord.Embed(title="Сервер: **Legend of The World**", description="**Енот Бот** был сделан специально для этого сервера.", color=0xeee657)
    embed.add_field(name=":wave: **Привет дорогой друг.** :wave:", value="Если ты тут значит тебя приняли,\n чтобы узнать айпи напиши - $ip", inline=True)
    embed.add_field(name="**Немного о сервере:**", value="Нету приватов, нету доната, свобода действий, не ограниченая территория.", inline=False)
    embed.add_field(name="**Узнать все команды:**", value="$Помощь.", inline=False)
    embed.add_field(name="**Пожертвования:**", value="Если у вас появилось желание помочь серверу\n просто напишите - $donate", inline=False)
    embed.set_footer(text="Все права на бота пренадлежат: **Lonely_#1572**") # Подвал сообщения

    await ctx.send(embed=embed)


@bot.command()
async def cat(ctx):
    await ctx.send("Вот вам кот: https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

token = os.environ.get('BOT_TOKEN')
bot.run(str(token))
