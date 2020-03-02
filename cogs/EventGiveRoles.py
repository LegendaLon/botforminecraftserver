from discord.ext import commands

from botforminecraftserver.botconfig import *

class GiveRoles(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_raw_reaction_add(self, payload):
	    msgID = int(payload.message_id)
	    if msgID == int(botconfig.message_id):
	        emoji = str(payload.emoji)
	        member = payload.member 
	        role = discord.utils.get(member.guild.roles, id=botconfig.roles[emoji])
	        await member.add_roles(role)
	    else:
	        pass

	@commands.Cog.listener()
	async def on_raw_reaction_remove(self, payload):
	    msgID = int(payload.message_id)
	    if msgID == int(botconfig.message_id):
	        channelID = payload.channel_id
	        channel = clibotent.get_channel(channelID)
	        messageID = payload.message_id
	        message = await channel.fetch_message(messageID)
	        userID = payload.user_id
	        member = discord.utils.get(message.guild.members, id= userID)
	        emoji = str(payload.emoji)
	        role = discord.utils.get(member.guild.roles, id=botconfig.roles[emoji])
	        await member.remove_roles(role)
	    else:
	        pass

def setup(client):
	client.add_cog(GiveRoles(client)) # 3