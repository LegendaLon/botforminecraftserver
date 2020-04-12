""" Importing Module"""
import discord
from discord.ext import commands
from DataBase import DataBase

import os, sys

import config

""" Setting """
client = commands.Bot(command_prefix=config.PREFIX_COMMAND) # Префикс для команд 

client.remove_command('help') # Удаляет команду help

""" Data Base """
# Путь к базе данных
pathDataBase = 'example.db'

# Подключение данных базы
try:
    db = DataBase(str(pathDataBase))
    print(f"[INFO] База данных '{pathDataBase}' успешно подключилась!")
except Exception as e:
    print(f"[ERROR] База данных '{pathDataBase}' не смогла запуститься из-за ошибки: {e}")
print('')

""" Cogs """
module = ["BotSystem", "BotFun", "BotUser", "BotHelp", "BotAdministrator"]
numY = 0
numN = 0

# Загрузка когов
for cog in module:
    try:
        print(f"[INFO] Модуль загружен: {cog}")
        client.load_extension(str(cog))
        numY += 1
        
    except Exception as e:
        del module[numY]
        numY += 1
        numN += 1
        print(f'[ERROR] Модуль "{cog}" не может быть загружен из-за ошибки: {e}')
print('')

# Подключение бота
token = os.environ.get('BOT_TOKEN')

try:
    client.run(str(token))
except Exception as e:
    print(f'[ERROR] Бот не может запуститься: Ошибка с токеном')