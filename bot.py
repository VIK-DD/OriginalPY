import discord
from discord.ext import commands
import os
import datetime

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Support"))
    print('Logged in as {0} ({0.id})'.format(client.user))
    print('-----------------------------------------')

@client.command()
async def ping(ctx):
    await ctx.send(" 🏓 Pinging")
    await ctx.send(f'Server/Bot ping is {round(client.latency * 1000)}ms')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, ammount=1):
    await ctx.channel.purge(limit=ammount)

@client.command()
async def prefix(ctx):
    await ctx.send('My prefix is "!"')
    
@client.command()
async def invite(ctx):
    await ctx.send('https://discord.gg/BVfYJHa')

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@client.command()
async def unban(ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {member.mention}')
                return

@client.command()
async def mute(ctx, member : discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "Muted":
            await member.add_roles(role)
            await ctx.send("{} was muted by {}" .format(member.mention,ctx.author.mention))
            return

            overwrite = discord.PermissionsOverwrite(send_messages=False)
            newRole = await guild.create_role(name="Muted")

            for channel in guild.text_channels:
                await channel.set_Permissions(newRole,overwrite=overwrite)

                await member.add_roles(newRole)
                await ctx.send("{} was muted by {}" .format(member.mention,ctx.author.mention))

@client.command()
async def unmute(ctx, member : discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "Muted":
            await member.remove_roles(role)
            await ctx.send("{} was unmuted by {}" .format(member.mention,ctx.author.mention))
            return

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')
    embed = discord.Embed(colour=0x95efcc, description=f"Welcome to ™Prime LFG™! You are the {len(list(member.guild.members))} member!", timestamp=datetime.datetime.utcfromtimestamp(1553629094))
    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
    embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    embed.timestamp = datetime.datetime.utcnow()

    channel = client.get_channel(id=684096171874189561)

    await channel.send(embed=embed)

    role = discord.utils.get(member.guild.roles, name="Membru")
    await member.add_roles(role)

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')
    embed = discord.Embed(colour=0x95efcc, description=f"{member.name} Just left our server, We are now {len(list(member.guild.members))} member!", timestamp=datetime.datetime.utcfromtimestamp(1553629094))
    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
    embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    embed.timestamp = datetime.datetime.utcnow()

    channel = client.get_channel(id=684097193820553236)

    await channel.send(embed=embed)

client.run(os.getenv('TOKEN'))
