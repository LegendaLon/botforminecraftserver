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

""" Cogs """
client.load_extension('EventGlobal')
client.load_extension('CommandGame')
client.load_extension('CommandUser')
client.load_extension('CommandHelp')

# RUN
token = os.environ.get('BOT_TOKEN')

client.run(str(token))