""" Importing Module"""
import discord
from discord.ext import commands

import os, sys

import config

""" Setting """
client = commands.Bot(command_prefix=config.PREFIX_COMMAND) # Префикс для команд 

client.remove_command('help') # Удаляет команду help

""" Cogs """
module = ["BotSystem", "BotFun", "BotUser", "BotHelp"]
for x in module:
    print(f"Модуль загружен: {x}")
    client.load_extension(str(x))

# RUN
token = os.environ.get('BOT_TOKEN')

client.run(str(token))