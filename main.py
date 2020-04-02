""" Importing Module"""
import discord

import os, sys

import botconfig

""" Setting """
client = commands.Bot(command_prefix=botconfig.PREFIX_COMMAND) # Префикс для команд 

client.remove_command('help') # Удаляет команду help

""" Cogs """
client.load_extension('Cogs.EventGlobal')
client.load_extension('Cogs.CommandGame')
client.load_extension('Cogs.CommandUser')
client.load_extension('Cogs.CommandHelp')

# RUN
token = os.environ.get('BOT_TOKEN')

client.run(str(token))