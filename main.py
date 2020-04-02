""" Importing Module"""
import discord
from discord.ext import commands

import os, sys

import botconfig

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