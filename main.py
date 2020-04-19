""" Importing Module"""
import discord
from discord.ext import commands
from DataBase import DataBase

import os, sys

import config

""" Setting """
client = commands.Bot(command_prefix=config.PREFIX_COMMAND) # Префикс для команд 

client.remove_command('help') # Удаляет команду help

allfiles = ['main.py', 'BotSystem.py', 'BotUser.py', 'BotAdministrator.py', 'BotHelp.py', 'BotFun.py', 'DataBase.py', 'config.py']

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
module = [
    # Система
    "BotSystem",
    # Веселие
    "BotFun",
    # Помощь
    "BotUser",
    "BotHelp",
    # Админ
    "BotAdministrator",
]

# Загрузка когов
for cog in module:
    print(f"[INFO] Модуль загружен: {cog}")
    client.load_extension(str(cog))
print('')

# Подключение бота
token = os.environ.get('BOT_TOKEN')

try:
    client.run(str(token))
except Exception as e:
    print(f'[ERROR] Бот не может запуститься')