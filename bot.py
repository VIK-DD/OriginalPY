import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '*')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="@RubyBoT", url="https://www.twitch.tv/ninja"))
    print('Logged in as {0} ({0.id})'.format(client.user))
    print('-----------------------------------------------')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="Member")
    await member.add_roles(role)
    
@client.command()
async def invite(ctx):
    await ctx.send('https://discord.gg/8GuPrQ8')
 
@client.event
async def on_member_join(member):
    embed = discord.Embed(colour=0x95efcc, description=f"Welcome to First Class Gaming! You are the {len(list(member.guild.members))} member!", timestamp=datetime.datetime.utcfromtimestamp(1553629094))
    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
    embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    embed.timestamp = datetime.datetime.utcnow()

    channel = client.get_channel(id=668385254561677322)

    await channel.send(embed=embed)

client.run(os.getenv('TOKEN'))
