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
token = os.environ.get('BOT_TOKEN')
client.run(str(token))