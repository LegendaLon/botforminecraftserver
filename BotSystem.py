import discord
from discord.ext import commands

from main import module

from random import choice
import config

class Start(commands.Cog):
    def __init__(self, client):
        self.client = client

        self.BotStatus = config.BOT_STATUS

    @commands.Cog.listener()
    async def on_ready(self):
        # Чат
        channel = self.client.get_channel(config.channel_start_bot_message)
        # Статус
        status = choice(self.BotStatus)
        activity = discord.Game(name=status)
        await self.client.change_presence(status=discord.Status.online, activity=activity)
        # запуск
        print("===============================================")
        print("|              Бот запущен успешно            |")
        print("|               Рабочие модули:               |")
        print(module)
        print("===============================================")
        await channel.send("Bot is start")

    @commands.command(aliases = ["Status", "Статус", "статус"])
    async def status(self, ctx, command=None, *, value=None):
        if command == "reg":
            status = choice(self.BotStatus)
            author = ctx.message.author
            await self.client.change_presence(activity=discord.Game(name=status))
            await ctx.send(f'{author.name}, статус бота был перегенерирован! =D')
            await ctx.send(f'Новый статус: **{status}**')

        elif command == "список":
            num = 1
            embed = discord.Embed(title='**Все статусы бота:**', color=config.orange)
            for x in self.BotStatus:
                embed.add_field(name=f'**Номер: {num}**',value=f'**{x}**',inline=False)
                num += 1

            await ctx.send(embed=embed)

        elif command == None:
            await ctx.send(f'Введите команду')

        else:
            await ctx.send(f'Неизвесная команда')

    @commands.command(aliases = ["Астатус", "астатус", "Astatus"])
    @commands.has_permissions(administrator=True)
    async def astatus(self, ctx, command=None, *, value=None):
        author = ctx.message.author
        if command == 'help':       
            self.BotStatus.append(value)

            await self.client.change_presence(activity=discord.Game(name=value))
            await ctx.send(f'{author.name}, статус бота был добавлен и применен! =D')
            await ctx.send(f'Новый статус: **{value}**')
        elif command == 'help':
            await ctx.send(embed=discord.Embed(description=f'{author.name}, чтобы добавить статус: ``{config.PREFIX_COMMAND}astatus add [Статус]``'))
        elif command == None:
            await ctx.send(f'Введите команду')
        else:
            await ctx.send(f'Неизвесная команда')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.client.get_channel(config.channel_message_join)
        print(f"{member.name}, присоединился к нам!")
        await channel.send(embed=discord.Embed(description= f'Пользователь ``{member.name}``, присоединился к нам!', color=config.orange)) # Пишет в чат сообщение
        await member.send(embed=discord.Embed(description=f':wave: Привет {member.name} тебя приняли :tada: :tada: , чтобы знать все мои команды напиши ``{config.PREFIX_COMMAND}{config.help_private_message_onejoin}`` в любой доступный чат, '
        f'а если нужна версия и IP-Адрес сервера напиши ``{config.PREFIX_COMMAND}{config.ip_private_message_onejoin}``', color=config.orange)) # Пишет новому пользователю в лс

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
    client.add_cog(Start(client))