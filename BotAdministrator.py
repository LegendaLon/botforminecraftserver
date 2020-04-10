import discord
from discord.ext import commands

import config

from main import db

adminRole = 645579508094599189

class Owners(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	@commands.has_role(adminRole)
	async def dbadd(self, ctx, tableName:str, name:str):
		pass

def setup(client):
    try:
        client.add_cog(Owners(client))
    except Exception as e:
        print(f'[ERROR] File BotAdministrator.py not work because: "{e}"')
