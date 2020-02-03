import discord
from discord.ext import commands
from botconfig import *

bot = commands.Bot(command_prefix=PREFIX_COMMAND)

@bot.event
async def on_ready():
    print('------')
    print("      ")
    print('Бот успешно запущен')
    print("Имя бота: "+ bot.user.name)
    print("      ")
    print('------')

@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def тест(ctx, arg):  # создаем асинхронную фунцию бота
    await ctx.send(arg)  # отправляем обратно аргумент

@bot.command()
async def Инфо(ctx):
    await ctx.send(MESSAGE_INFO)

@bot.command()
async def cat(ctx):
    await ctx.send("Вот вам кот: https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

bot.run(TOKEN)