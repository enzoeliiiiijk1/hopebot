import discord
from discord.ext import commands
import requests
import random

class ADMIN(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await ctx.message.delete()
        await member.ban(reason=reason)
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Sorry you are not allowed to use this command, to use this command you need to have ``Ban Members``')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
    	banned_users = await ctx.guild.bans()
    	member_name, member_discriminator = member.split('#')

    	for ban_entry in banned_users:
    		user = ban_entry.user

    		if (user.name, user.discriminator) == (member_name, member_discriminator):
    			await ctx.guild.unban(user)
    			await ctx.send(f'Unbanned {user.mention}')
    			return
    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Sorry you are not allowed to use this command, to use this command you need to have ``Ban Members``')


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await ctx.message.delete()
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Sorry you are not allowed to use this command, to use this command you need to have ``Kick Members``')

    @commands.command()
    @commands.has_permissions(manage_channels = True)
    async def purge(self, ctx, amount=0):
        await ctx.channel.purge(limit= amount+1)
    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Sorry you are not allowed to use this command, to use this command you need to have ``Manage Channels``')
    

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def nuke(self, ctx):
        channel = discord.utils.get(ctx.guild.channels, name=ctx.channel.name)
        new_channel = await channel.clone(reason=f'Channel nuked by: {ctx.author}')
        await channel.delete()
        await new_channel.edit(position=ctx.channel.position)
        embed = discord.Embed(title="Attention", description=f"This Channel Was Nuked", color=0x000000,)
        embed.set_image(url="https://cdn.discordapp.com/attachments/785513180491284490/785513662869143552/image0.gif")
        embed.set_footer(text="Hope")
        await new_channel.send(embed=embed)
        # print(f'{Fore.LIGHTWHITE_EX}{Style.BRIGHT}Channels Nuked: {Fore.LIGHTRED_EX}{Style.BRIGHT}{count}'+Fore.RESET)
    @nuke.error
    async def nuke_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed=discord.Embed(title="Command Error", description="Hmm... It seems you don't have permission to use this comamnd!", color=0xFF0000)
            await ctx.send(embed=embed)
            return


def setup(client):
    client.add_cog(ADMIN(client)) 
