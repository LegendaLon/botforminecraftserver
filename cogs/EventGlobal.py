import discord
from discord.ext import commands

from random import choice
from botforminecraftserver.botconfig import *

class Event(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self): # Когда бот запущен и готов к работе
        channel = self.client.get_channel(channel_start_bot_message) # Чат в который кидает данные о боте
        status= choice(BOT_STATUS) # Рандомизирует статус с botconfig
        activity = activity = discord.Game(name=status) # Задает статус
        await self.client.change_presence(status=discord.Status.idle, activity=activity) # Применяет статус
        embed = discord.Embed(title="**Енот Бот** запущен", description="", color=green) # Создает красивый вывод с заголовком title и цветом green 
        embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url) # Задает автора name и аватар бота icon_url
        embed.add_field(name='**Статус**', value=f"Статус бота - **{status}**.", inline=True) # Создает строку
        embed.add_field(name='**Статус**', value=f"Все статусы - **{BOT_STATUS}**.", inline=True) # Создает строку
        embed.add_field(name='**Версия**', value=f'Версия - **{version}**', inline=False) # Создает красивый вывод с заголовком title и цветом green 
        embed.add_field(name='**Все хорошо**', value='Все функции работают хорошо!', inline=False) # Создает строку
        embed.set_footer(text=f"Все права на бота пренадлежат: {BOT_AUTHOR}") # Подвал сообщения
        print("Ready? Gooo!") # Пишет сообщение в консоль что бот запущен
        await channel.send(embed=embed, delete_after=180) # Отправляет сообщение а потому удалит после 180 секунд

    @commands.Cog.listener()
    async def on_member_join(self, member): # Когда заходит новый пользователь
        channel = self.client.get_channel(channel_message_join) # Чат в который будет оправляться сообщение о новых участниках
        print(f"{member.name}, присоединился к нам!") # Пишет в консоль о новом учатнике
        await channel.send(embed=discord.Embed(description= f'Пользователь ``{member.name}``, присоединился к нам!', color=orange)) # Пишет в чат сообщение
        await member.send(embed=discord.Embed(description=f':wave: Привет {member.name} тебя приняли :tada: :tada: , чтобы знать все мои команды напиши ``{botconfig.PREFIX_COMMAND}{botconfig.help_private_message_onejoin}`` в любой доступный чат, '
        f'а если нужна версия и IP-Адрес сервера напиши ``{PREFIX_COMMAND}{ip_private_message_onejoin}``', color=orange)) # Пишет новому пользователю в лс

def setup(client):
    client.add_cog(Event(client)) # 7