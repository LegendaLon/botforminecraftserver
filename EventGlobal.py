import discord
from discord.ext import commands

from random import choice
import botconfig

class Event(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self): # Когда бот запущен и готов к работе
        channel = self.client.get_channel(botconfig.channel_start_bot_message) # Чат в который кидает данные о боте
        status= choice(botconfig.BOT_STATUS) # Рандомизирует статус с botconfig
        activity = activity = discord.Game(name=status) # Задает статус
        await self.client.change_presence(status=discord.Status.idle, activity=activity) # Применяет статус
        print("Ready? Gooo!") # Пишет сообщение в консоль что бот запущен
        await channel.send("It's start hosting") # Отправляет сообщение а потому удалит после 180 секунд

    @commands.Cog.listener()
    async def on_member_join(self, member): # Когда заходит новый пользователь
        channel = self.client.get_channel(botconfig.channel_message_join) # Чат в который будет оправляться сообщение о новых участниках
        print(f"{member.name}, присоединился к нам!") # Пишет в консоль о новом учатнике
        await channel.send(embed=discord.Embed(description= f'Пользователь ``{member.name}``, присоединился к нам!', color=orange)) # Пишет в чат сообщение
        await member.send(embed=discord.Embed(description=f':wave: Привет {member.name} тебя приняли :tada: :tada: , чтобы знать все мои команды напиши ``{botconfig.PREFIX_COMMAND}{botconfig.help_private_message_onejoin}`` в любой доступный чат, '
        f'а если нужна версия и IP-Адрес сервера напиши ``{botconfig.PREFIX_COMMAND}{botconfig.ip_private_message_onejoin}``', color=orange)) # Пишет новому пользователю в лс

def setup(client):
    client.add_cog(Event(client))