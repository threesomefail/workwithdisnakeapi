import asyncio
import disnake
from disnake.ext import commands


bot = commands.Bot(command_prefix='', intents = disnake.Intents.all(), activity = disnake.Game('IN DEVELOPING', status = disnake.Status.online))
bot.remove_command('help')


@bot.event
async def on_ready():
    print("BOT IS READY FOR USE")


@bot.slash_command(description="Показывает информацию о сервере")
async def serverinfo(inter):
    embed = disnake.Embed(title = "Информация о сервере", description = f"Название сервера:`` {inter.guild.name} ``\nКоличество участников: `` {inter.guild.member_count} ``\nКоличество ролей на сервере: `` {len(inter.guild.roles)} ``", color= 3092790)
    await inter.send(embed=embed)


token = open('token.txt', 'r').readline()
bot.run(token)
