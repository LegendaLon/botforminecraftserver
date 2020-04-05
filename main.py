""" Importing Module"""
import discord
from discord.ext import commands

import os, sys

import config

""" Setting """
client = commands.Bot(command_prefix=config.PREFIX_COMMAND) # Префикс для команд 

client.remove_command('help') # Удаляет команду help

""" Cogs """
module = ["BotSystem", "BotFun", "BotUser", "BotHelp", "BotAdministrator"]
numY = 0
numN = 0
for x in module:
    try:
        print(f"[INFO] Модуль загружен: {x}")
        client.load_extension(str(x))
        numY += 1
    except Exception as e:
        del module[numY]
        numY += 1
        numN += 1
        print(f'[ERROR] Модуль "{x}" не может быть загружен из-за ошибки: {e}')
print('')
# RUN
token = os.environ.get('BOT_TOKEN')

try:
    client.run(str(token))
except Exception as e:
    print(f'[ERROR] Бот не может запуститься: Ошибка с токеном')