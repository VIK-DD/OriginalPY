import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '/')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('Streaming RubyBoT'))
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
