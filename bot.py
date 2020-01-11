import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '|')

@client.event
async def on_ready():
    await bot.change_presence(activity=discord.Status.idle.Activity(type=discord.ActivityType.listening, name="a song"))
    print('Logged in as {0} ({0.id})'.format(client.user))
    print('-----------------------------------------------')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="Member")
    await member.add_roles(role)
 
client.run(os.getenv('TOKEN'))
