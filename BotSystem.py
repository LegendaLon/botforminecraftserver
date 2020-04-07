import discord
from discord.ext import commands

from main import module

from random import choice
import config

class Start(commands.Cog):
    def __init__(self, client):
        self.client = client

        self.BotStatus = config.BOT_STATUS

        self.serverid = None

    @commands.Cog.listener()
    async def on_ready(self):
        BotCreator = self.client.get_user(518766156790890496)
        # Статус
        status = choice(self.BotStatus)
        activity = discord.Game(name=status)
        await self.client.change_presence(status=discord.Status.online, activity=activity)
        # запуск
        await BotCreator.send(embed=discord.Embed(description=f'Bot {self.client.user.name}, is start', color=config.orange))
        print(f'[INFO] Бот запущен успешно. \n[INFO] Модули: {module}. \n[INFO] Количество загруженых модулей: {len(module)}')

    @commands.command(aliases = ["Status", "Статус", "статус"])
    async def status(self, ctx, command=None, *, value=None):
        if command == "reg" or command == 'рег':
            status = choice(self.BotStatus)
            author = ctx.message.author

            embed = discord.Embed(title=f'{author.name}, статус бота был перегенерирован! =D', color=config.orange)
            embed.add_field(name='Новый статус: **{status}**', value='', inline=True)

            await self.client.change_presence(activity=discord.Game(name=status))
            await ctx.send(embed=embed)

        elif command == "список" or command == 'list':
            num = 1
            embed = discord.Embed(title='**Все статусы бота:**', color=config.orange)
            for x in self.BotStatus:
                embed.add_field(name=f'**Номер: {num}**',value=f'**{x}**',inline=False)
                num += 1

            await ctx.send(embed=embed)

        elif command == None:
            await ctx.send(embed=discord.Embed(f'Введите команду'))

        else:
            await ctx.send(embed=discord.Embed(f'Неизвесная команда'))

    @commands.command(aliases = ["Астатус", "астатус", "Astatus"])
    @commands.has_permissions(administrator=True)
    async def astatus(self, ctx, command=None, *, value=None):
        author = ctx.message.author
        if command == 'add' or command == 'добавить': 
            if value == None:
                await ctx.send(embed=discord.Embed(f'{author.name}, Вы не ввели статус.', color=config.orange))
            else:
                if value == self.BotStatus:
                    await ctx.send(embed=discord.Embed(f'Вы ввели уже существующий статус.', color=config.orange))
                else:
                    self.BotStatus.append(value)

                    await self.client.change_presence(activity=discord.Game(name=value))
                    await ctx.send(f'{author.name}, статус бота был добавлен и применен! =D')
                    await ctx.send(f'Новый статус: **{value}**')

        elif command == 'del' or command == 'удалить':
            if type(value).__name__ == type(1).__name__:
                if value == None:
                    await ctx.send(embed=discord.Embed(f'{author.name}, Вы не ввели номер статуса чтобы удалить его.', color=config.orange))
                else:
                    if value > len(self.BotStatus)+1:
                        del self.BotStatus[value]

                        await ctx.send(f'{author.name}, статус бота был удаллен! =D')
                        await ctx.send(f'Удалленый статус: **{value}**')
                    else:
                        await ctx.send(embed=discord.Embed(f'{author.name}, Вы ввели номер статуса которого не существует.', color=config.orange))
            else:
                await ctx.send(embed=discord.Embed(
                        f'{author.name}, введите номер статуса чтобы удалить его.\n'
                        f'Чтобы узнать все статусы введите ``{config.PREFIX_COMMAND}статус список``', color=config.orange
                        ))

        elif command == 'help' or command == 'помощь':
            embed = discord.Embed(title='', color=config.orange)
            embed.add_field(name='**Добавление статуса**', value=f'Чтобы добавить статус: ``{config.PREFIX_COMMAND}astatus add [Статус]``', inline=True)
            embed.add_field(name='**Удаление статуса**', value=f'Чтобы удалить статус: ``{config.PREFIX_COMMAND}astatus del [Номер статуса]``', inline=True)
            await ctx.send(embed=embed)
        
        elif command == None:
            await ctx.send(embed=discord.Embed(description=f'{author.name}, Вы забыли ввести команду.', color=config.orange))
        
        else:
            await ctx.send(embed=discord.Embed(description=f'{author.name}, Вы ввели неизвесную команду.', color=config.orange))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild.id
        if guild == 645564398378680332:
            channel = self.client.get_channel(config.channel_message_join)
            await channel.send(embed=discord.Embed(description= f'Пользователь ``{member.name}``, присоединился к нам!', color=config.orange))
        else:
            print(f"New member: {member}, in guild: {guild.name}")
        print(f"{member.name}, присоединился к нам!")
        
class JoinGroun(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.BotCreator = self.client.get_user(518766156790890496)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        embed = discord.Embed(title=f'Бот присоединился к: **{guild.name}**', color=config.orange)
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(name="**Сейчас людей на сервере:**", value=f"{guild.member_count}", inline=True)
        embed.add_field(name="**Регион:**", value=guild.region, inline=True)
        embed.add_field(name="**Создатель сервера:**", value=guild.owner, inline=True)
        embed.add_field(name=f"**Количество чатов[{len(guild.channels)}]: **", value=f'Текстовых: **{len(guild.text_channels)}**\nГолосовых: **{len(guild.voice_channels)}**', inline=True)
        embed.add_field(name=f"**Количество ролей:**",value=len(guild.roles), inline=True)
        embed.add_field(name=f"**Сервер был создан:**",value=guild.created_at, inline=True)
        embed.set_footer(text=f"Все права на бота пренадлежат: {config.BOT_AUTHOR}")
        await self.BotCreator.send(embed=embed)

class GiveRoles(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        msgID = int(payload.message_id)
        if msgID == int(config.message_id):
            emoji = str(payload.emoji)
            member = payload.member 
            role = discord.utils.get(member.guild.roles, id=config.roles[emoji])
            await member.add_roles(role)
        else:
            pass

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        msgID = int(payload.message_id)
        if msgID == int(config.message_id):
            channelID = payload.channel_id
            channel = clibotent.get_channel(channelID)
            messageID = payload.message_id
            message = await channel.fetch_message(messageID)
            userID = payload.user_id
            member = discord.utils.get(message.guild.members, id= userID)
            emoji = str(payload.emoji)
            role = discord.utils.get(member.guild.roles, id=config.roles[emoji])
            await member.remove_roles(role)
        else:
            pass

def setup(client):
    try:
        client.add_cog(Start(client))
        client.add_cog(JoinGroun(client))
    except Exception as e:
        print(f'[ERROR] File BotSystem.py not work because: "{e}"')
    