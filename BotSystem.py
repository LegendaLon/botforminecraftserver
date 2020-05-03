import discord
from discord.ext import commands

from main import module, db

from random import choice
import config

class JoinAndLeaveMemberInGroup(commands.Cog):
    def __init__(self, client):
        self.client = client

        self.allguildid = []

    def RandomStatus(self):
        data = db._select_order_by('status', 'id')
        dataR = choice(data)
        return dataR[1]

    def LenGuilds(self):
        self.allguildid = []
        data = db._select_all('guild')

        for a in data:
            self.allguildid.append(a[1])

        print(self.allguildid)

    @commands.Cog.listener()
    async def on_ready(self):
        BotCreator = self.client.get_user(518766156790890496)
        # Статус
        status = self.RandomStatus()
        activity = discord.Game(name=status)
        await self.client.change_presence(status=discord.Status.online, activity=activity)

        # запуск
        await BotCreator.send(embed=discord.Embed(description=f'Bot {self.client.user.name}, is start', color=config.orange))
        print(f'[INFO] Модули: {module}.\n[INFO] Бот запущен успешно.')


    @commands.Cog.listener()
    async def on_member_join(self, member):
        # Сообщение в определенный чат
        self.LenGuilds()
        guild = member.guild
        guild_id = guild.id

        if guild_id in self.allguildid:
            data = db._select_where('guild', 'guild_id', int(guild_id))[0]
            if data[1] in self.allguildid:
                if data[2] != 0:
                    print(data[2])
                    channel = self.client.get_channel(int(data[2]))
                    await channel.send(embed=discord.Embed(description= f'Пользователь ``{member.name}``, присоединился к нам!', color=config.orange))
                else:
                    pass
            else:
                pass
        else:
            pass

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        # Сообщение в определенный чат
        self.LenGuilds()
        guild = member.guild
        guild_id = guild.id

        if guild_id in self.allguildid:
            data = db._select_where('guild', 'guild_id', int(guild_id))[0]
            if data[1] in self.allguildid:
                if data[2] != 0:
                    channel = self.client.get_channel(data[2])
                    await channel.send(embed=discord.Embed(description= f'Пользователь ``{member.name}`` решил покинуть нас. =(', color=config.orange))
                else:
                    pass
            else:
                pass
        else:
            pass

class StatusInBot(commands.Cog):
    def __init__(self, client):
        self.client = client

        self.lenStatus = []
        self.nameStatus = []

    def RandomStatus(self):
        self.lenStatus = []
        self.nameStatus = []
        data = db._select_order_by('status', 'id')
        for a in data:
            self.lenStatus.append(int(a[0]))

        for x in data:
            self.nameStatus.append(str(x[1]))

        print(self.lenStatus)
        dataR = choice(data)
        return dataR[1]

    @commands.command(
        aliases = ["Status", "Статус", "статус"],
        help = '',
        description = '',
        hidden = True,
        )
    async def status(self, ctx, command:str=None, *, value:str=None):
        if command == "reg" or command == 'рег':
            status = self.RandomStatus()
            author = ctx.message.author

            embed = discord.Embed(title=f'{author.name}, статус бота был перегенерирован! =D', color=config.orange)
            embed.add_field(name='Новый статус: **{status}**', value='', inline=True)

            await self.client.change_presence(activity=discord.Game(name=status))
            await ctx.send(embed=embed)

        elif command == "список" or command == 'list':
            embed = discord.Embed(title='**Все статусы бота:**', color=config.orange)
            data = db._select_order_by('status', 'id')
            for x in data:
                embed.add_field(name=f'**Номер: {x[0]}**\n**Автор: {x[2]}**',value=f'**{x[1]}**',inline=False)

            await ctx.send(embed=embed) 

        elif command == None:
            await ctx.send(embed=discord.Embed(f'Введите команду'))

        else:
            await ctx.send(embed=discord.Embed(f'Неизвесная команда'))

    @commands.command(
        aliases = ["Астатус", "астатус", "Astatus"],
        help = '',
        description = '',
        hidden = True,
        )
    @commands.is_owner()
    async def astatus(self, ctx, command:str=None, *, value=None):
        author = ctx.message.author
        if command == 'add' or command == 'добавить': 
            if value == None:
                await ctx.send(embed=discord.Embed(description=f'{author.name}, Вы не ввели статус.', color=config.orange))
            else:
                data = db._select_order_by('status', 'id')
                if value == self.nameStatus:
                    await ctx.send(embed=discord.Embed(description=f'Вы ввели уже существующий статус.', color=config.orange))
                else:
                    db.insert_status(value, author.name)

                    await self.client.change_presence(activity=discord.Game(name=value))
                    await ctx.send(embed=discord.Embed(description=f'{author.name}, статус бота был добавлен и применен! =D\nНовый статус: **{value}**', color=config.orange))

        elif command == 'set' or command == 'установить': 
            if value == None:
                await ctx.send(embed=discord.Embed(description=f'{author.name}, Вы не ввели статус.', color=config.orange))
            else:
                db.insert_status(value, author.name)

                await self.client.change_presence(activity=discord.Game(name=value))
                await ctx.send(embed=discord.Embed(description=f'{author.name}, статус бота применен! =D\nНовый статус: **{value}**', color=config.orange))

        elif command == 'del' or command == 'удалить':
            if type(int(value)).__name__ == type(1).__name__:
                if value == None:
                    await ctx.send(embed=discord.Embed(description=f'{author.name}, Вы не ввели номер статуса чтобы удалить его.', color=config.orange))
                else:
                    
                    try:    
                        value = int(value)
                        
                        db.delete_status(value)

                        status = self.RandomStatus() 
                        await self.client.change_presence(activity=discord.Game(name=status))
                        await ctx.send(embed=discord.Embed(description=f'{author.name}, статус под айди {value} успешно удален', color=config.orange))
                    except Exception as e:
                        print("[ERROR] " + e)
                        await ctx.send(embed=discord.Embed(description=f'{author.name}, что-то пошло не так', color=config.orange))
            else:
                await ctx.send(embed=discord.Embed(description=f'{author.name}, введите номер статуса чтобы удалить его.\nЧтобы узнать все статусы введите ``{config.PREFIX_COMMAND}статус список``', color=config.orange))


        elif command == 'help' or command == 'помощь':
            embed = discord.Embed(title='', color=config.orange)
            embed.add_field(name='**Добавление статуса**', value=f'Чтобы добавить статус: ``{config.PREFIX_COMMAND}astatus add [Статус]``', inline=True)
            embed.add_field(name='**Удаление статуса**', value=f'Чтобы удалить статус: ``{config.PREFIX_COMMAND}astatus del [Номер статуса]``', inline=True)
            await ctx.send(embed=embed)
        
        elif command == None:
            await ctx.send(embed=discord.Embed(description=f'{author.name}, Вы забыли ввести команду.', color=config.orange))
        
        else:
            await ctx.send(embed=discord.Embed(description=f'{author.name}, Вы ввели неизвесную команду.', color=config.orange))
        
class JoinGroun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        BotCreator = self.client.get_user(518766156790890496)

        # Оповищеное о конекте к группе
        embed = discord.Embed(title=f'Бот присоединился к: **{guild.name}**', color=config.orange)
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(name="**Сейчас людей на сервере:**", value=f"{guild.member_count}", inline=True)
        embed.add_field(name="**Регион:**", value=guild.region, inline=True)
        embed.add_field(name="**Создатель сервера:**", value=guild.owner, inline=True)
        embed.add_field(name=f"**Количество чатов[{len(guild.channels)}]: **", value=f'Текстовых: **{len(guild.text_channels)}**\nГолосовых: **{len(guild.voice_channels)}**', inline=True)
        embed.add_field(name=f"**Количество ролей:**",value=len(guild.roles), inline=True)
        embed.add_field(name=f"**Сервер был создан:**",value=guild.created_at, inline=True)
        embed.add_field(name=f"**Id:**", value=guild.id, inline=True)
        embed.set_footer(text=f"Все права на бота пренадлежат: {config.BOT_AUTHOR}")
        await BotCreator.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        BotCreator = self.client.get_user(518766156790890496)
        # Удаление из базы
        # Оповищеное об уходе из группы
        embed = discord.Embed(title=f'Бот вышел из: **{guild.name}**', color=config.orange)
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(name="**Сейчас людей на сервере:**", value=f"{guild.member_count}", inline=True)
        embed.add_field(name="**Регион:**", value=guild.region, inline=True)
        embed.add_field(name="**Создатель сервера:**", value=guild.owner, inline=True)
        embed.add_field(name=f"**Количество чатов[{len(guild.channels)}]: **", value=f'Текстовых: **{len(guild.text_channels)}**\nГолосовых: **{len(guild.voice_channels)}**', inline=True)
        embed.add_field(name=f"**Количество ролей:**",value=len(guild.roles), inline=True)
        embed.add_field(name=f"**Сервер был создан:**",value=guild.created_at, inline=True)
        embed.add_field(name=f"**Id:**", value=guild.id, inline=True)
        embed.set_footer(text=f"Все права на бота пренадлежат: {config.BOT_AUTHOR}")
        await BotCreator.send(embed=embed)


def setup(client):
    try:
        client.add_cog(JoinAndLeaveMemberInGroup(client))
        client.add_cog(StatusInBot(client))
        client.add_cog(JoinGroun(client))
    except Exception as e:
        print(f'[ERROR] File BotSystem.py not work because: "{e}"')