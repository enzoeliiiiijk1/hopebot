import discord
from discord.ext import commands
from urllib.parse import urlparse
import datetime
import asyncio
import psutil
import random
import pip
import json
import os
import io
import time

class INFO(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(no_pm=True)
    async def channels(self, ctx, serverid:int = None):
        """Shows ALL channels, use wisely!"""

        if serverid is None:
            server = ctx.guild
        else:
            server = discord.utils.get(self.client.guilds, id=serverid)
            if server is None:
                return await ctx.send('Server not found!')

        e = discord.Embed(color=0x000000)

        voice = ''
        text = ''
        categories = ''

        for channel in server.voice_channels:
            voice += f'\U0001f508 {channel}\n'
        for channel in server.categories:
            categories += f'\U0001f4da {channel}\n'
        for channel in server.text_channels:
            text += f'\U0001f4dd {channel}\n'
        
        if len(server.text_channels) > 0:
            e.add_field(name='Text Channels', value=f'```{text}```')
        if len(server.categories) > 0:
            e.add_field(name='Categories', value=f'```{categories}```')
        if len(server.voice_channels) > 0:
            e.add_field(name='Voice Channels', value=f'```{voice}```')

        try:
            await ctx.send(embed=e)
        except discord.HTTPException:
            em_list = await embedtobox.etb(e)
            for page in em_list:
                await ctx.send(page)

    @commands.command(aliases=["ri","role"], no_pm=True)
    @commands.guild_only()
    async def roleinfo(self, ctx, *, role: discord.Role):
        '''Shows information about a role'''
        guild = ctx.guild

        since_created = (ctx.message.created_at - role.created_at).days
        role_created = role.created_at.strftime("%d %b %Y %H:%M")
        created_on = "{} ({} days ago!)".format(role_created, since_created)
        members = ''
        i = 0
        for user in role.members:
            members += f'{user.name}, '
            i+=1
            if i > 30:
                break

        if str(role.colour) == "#000000":
            colour = "default"
            color = ("#%06x" % random.randint(0, 0xFFFFFF))
            color = int(colour[1:], 16)
        else:
            colour = str(role.colour).upper()
            color = role.colour

        em = discord.Embed(color=0x000000)
        em.set_author(name=role.name)
        em.add_field(name="Users", value=len(role.members))
        em.add_field(name="Mentionable", value=role.mentionable)
        em.add_field(name="Hoist", value=role.hoist)
        em.add_field(name="Position", value=role.position)
        em.add_field(name="Managed", value=role.managed)
        em.add_field(name="Colour", value=colour)
        em.add_field(name='Creation Date', value=created_on)
        em.add_field(name='Members', value=members[:-2], inline=False)
        em.set_footer(text=f'Role ID: {role.id}')

        await ctx.send(embed=em)

    @commands.command()
    async def av(self, ctx):
        em = discord.Embed(description='**\n{0}**'.format(ctx.author))
        em.set_image(url=ctx.author.avatar_url)

        await ctx.send(embed=em)

    @commands.command()
    async def avatar(self, ctx):
        em = discord.Embed(description='**\n{0}**'.format(ctx.author))
        em.set_image(url=ctx.author.avatar_url)

        await ctx.send(embed=em)

    @commands.command()
    async def serverinfo(self, ctx):
      name = str(ctx.guild.name)
      owner = str(ctx.guild.owner)
      region = str(ctx.guild.region)
      memberCount = str(ctx.guild.member_count)

      icon = str(ctx.guild.icon_url)
       
      embed = discord.Embed(
      embed = discord.Embed(title=f"hope", color=0x08fffb)
    )
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/822131201501560853/827024393288810516/unknown.png')
      embed.add_field(name="Owner", value=owner, inline=False)
      embed.add_field(name="Region", value=region, inline=False)
      embed.add_field(name="Member Count", value=memberCount, inline=False)

      await ctx.send(embed=embed)

    @commands.command(aliases=['ui'], no_pm=True)
    @commands.guild_only()
    async def userinfo(self, ctx, *, member : discord.Member=None):
        '''Get information about a member of a server'''
        server = ctx.guild
        user = member or ctx.message.author
        avi = user.avatar_url
        roles = sorted(user.roles, key=lambda c: c.position)

        for role in roles:
            if str(role.color) != "#000000":
                color = role.color
        if 'color' not in locals():
            color = 0

        rolenames = ', '.join([r.name for r in roles if r.name != "@everyone"]) or 'None'
        time = ctx.message.created_at
        desc = '{0} is chilling in {1} mode.'.format(user.name, user.status)
        member_number = sorted(server.members, key=lambda m: m.joined_at).index(user) + 1

        em = discord.Embed(colour=color, description=desc, timestamp=time)
        em.add_field(name='Nick', value=user.nick, inline=True)
        em.add_field(name='Member No.',value=str(member_number),inline = True)
        em.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y'))
        em.add_field(name='Join Date', value=user.joined_at.__format__('%A, %d. %B %Y'))
        em.add_field(name='Roles', value=rolenames, inline=True)
        em.set_footer(text='User ID: '+str(user.id))
        em.set_thumbnail(url=avi)
        em.set_author(name=user, icon_url=server.icon_url)

        try:
            await ctx.send(embed=em)
        except discord.HTTPException:
            em_list = await embedtobox.etb(em)
            for page in em_list:
                await ctx.send(page)
    
    @commands.command(aliases=['client', 'info'])
    async def about(self, ctx):
        '''See information about the client.'''

        embed = discord.Embed()

        embed.add_field(name='Author', value='enzo#0004 - Pulse#8888')
        embed.add_field(name='Guilds', value=len(self.client.guilds))
        embed.add_field(name='Members', value=f'{len(set(self.client.get_all_members()))}')
        embed.add_field(name='Discord', value="https://discord.gg/Tw2BG5umB9")
        embed.set_footer(text=f'Powered by discord.py {discord.__version__}')
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong! my latency is: {0}'.format(round(self.client.latency, 1)))

    
    @commands.command()
    async def status(self, ctx):

      icon = str(ctx.guild.icon_url)
       
      embed = discord.Embed(
      embed = discord.Embed(title=f"hope", color=0x08fffb)
    )
      embed.add_field(name="Online!", value='My commands are functional and working!', inline=False)
    

      await ctx.send(embed=embed)

def setup(client):
    client.add_cog(INFO(client))
