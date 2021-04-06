import discord
from discord.ext import commands
import requests
import asyncio
import aiohttp

class NSFW(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def hentai(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as session:
                async with session.get('https://nekos.life/api/v2/img/Random_hentai_gif') as r:
                    if r.status == 200:
                        js = await r.json()
                        embed = discord.Embed(title=f"Hentai NSFW", color=0x08fffb)
                        embed.set_image(url=js['url'])
                        await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"Error, Current Channel Doesnt Have NSFW enabled.", description="You can enable it by going into ``channel settings``", color=0xff0008)
            embed.set_image(url='https://i.imgur.com/oe4iK5i.gif')
            await ctx.send(embed=embed)

    @commands.command()
    async def lesbian(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as session:
                async with session.get('https://nekos.life/api/v2/img/les') as r:
                    if r.status == 200:
                        js = await r.json()
                        embed = discord.Embed(title=f"Lesbian NSFW", color=0x08fffb)
                        embed.set_image(url=js['url'])
                        await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"Error, Current Channel Doesnt Have NSFW enabled.", description="You can enable it by going into ``channel settings``", color=0xff0008)
            embed.set_image(url='https://i.imgur.com/oe4iK5i.gif')
            await ctx.send(embed=embed)


    @commands.command()
    async def blowjob(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as session:
                async with session.get('https://nekos.life/api/v2/img/blowjob') as r:
                    if r.status == 200:
                        js = await r.json()
                        embed = discord.Embed(title=f"Blowjob NSFW", color=0x08fffb)
                        embed.set_image(url=js['url'])
                        await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"Error, Current Channel Doesnt Have NSFW enabled.", description="You can enable it by going into ``channel settings``", color=0xff0008)
            embed.set_image(url='https://i.imgur.com/oe4iK5i.gif')
            await ctx.send(embed=embed)

    @commands.command()
    async def anal(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as session:
                async with session.get('https://nekos.life/api/v2/img/anal') as r:
                    if r.status == 200:
                        js = await r.json()
                        embed = discord.Embed(title=f"Anal NSFW", color=0x08fffb)
                        embed.set_image(url=js['url'])
                        await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"Error, Current Channel Doesnt Have NSFW enabled.", description="You can enable it by going into ``channel settings``", color=0xff0008)
            embed.set_image(url='https://i.imgur.com/oe4iK5i.gif')
            await ctx.send(embed=embed)


    @commands.command(pass_context=True)
    async def fuck(self, message, member: discord.Member = None):
            member = message.author if not member else member
            embed = discord.Embed(title=f"{message.author} Fucking The Shit Outa {member} Mom :kissing_heart:", description="", color=0x08fffb)
            embed.set_image(url="https://thumb-p4.xhcdn.com/a/R292lF5ESNf4icujFKO4Aw/000/116/650/774_450.gif"),
            await message.send(embed=embed)
            await message.message.delete()

    @commands.command()
    async def feet(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as session:
                async with session.get('https://nekos.life/api/v2/img/feetg') as r:
                    if r.status == 200:
                        js = await r.json()
                        embed = discord.Embed(title=f"Feet NSFW", color=0x08fffb)
                        embed.set_image(url=js['url'])
                        await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"Error, Current Channel Doesnt Have NSFW enabled.", description="You can enable it by going into ``channel settings``", color=0xff0008)
            embed.set_image(url='https://i.imgur.com/oe4iK5i.gif')
            await ctx.send(embed=embed)
    
    @commands.command()
    async def yuri(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as session:
                async with session.get('https://nekos.life/api/v2/img/yuri') as r:
                    if r.status == 200:
                        js = await r.json()
                        embed = discord.Embed(title=f"Yuri NSFW", color=0x08fffb)
                        embed.set_image(url=js['url'])
                        await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"Error, Current Channel Doesnt Have NSFW enabled.", description="You can enable it by going into ``channel settings``", color=0xff0008)
            embed.set_image(url='https://i.imgur.com/oe4iK5i.gif')
            await ctx.send(embed=embed)

    @commands.command()
    async def trap(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as session:
                async with session.get('https://nekos.life/api/v2/img/trap') as r:
                    if r.status == 200:
                        js = await r.json()
                        embed = discord.Embed(title=f"Trap NSFW", color=0x08fffb)
                        embed.set_image(url=js['url'])
                        await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"Error, Current Channel Doesnt Have NSFW enabled.", description="You can enable it by going into ``channel settings``", color=0xff0008)
            embed.set_image(url='https://i.imgur.com/oe4iK5i.gif')
            await ctx.send(embed=embed)

    @commands.command()
    async def futanari(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as session:
                async with session.get('https://nekos.life/api/v2/img/futanari') as r:
                    if r.status == 200:
                        js = await r.json()
                        embed = discord.Embed(title=f"Futanari NSFW", color=0x08fffb)
                        embed.set_image(url=js['url'])
                        await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"Error, Current Channel Doesnt Have NSFW enabled.", description="You can enable it by going into ``channel settings``", color=0xff0008)
            embed.set_image(url='https://i.imgur.com/oe4iK5i.gif')
            await ctx.send(embed=embed)

    @commands.command()
    async def hololewd(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as session:
                async with session.get('https://nekos.life/api/v2/img/hololewd') as r:
                    if r.status == 200:
                        js = await r.json()
                        embed = discord.Embed(title=f"Hololewd NSFW", color=0x08fffb)
                        embed.set_image(url=js['url'])
                        await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"Error, Current Channel Doesnt Have NSFW enabled.", description="You can enable it by going into ``channel settings``", color=0xff0008)
            embed.set_image(url='https://i.imgur.com/oe4iK5i.gif')
            await ctx.send(embed=embed)

    @commands.command()
    async def lewdkemo(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as session:
                async with session.get('https://nekos.life/api/v2/img/lewdkemo') as r:
                    if r.status == 200:
                        js = await r.json()
                        embed = discord.Embed(title=f"Lewdkemo NSFW", color=0x08fffb)
                        embed.set_image(url=js['url'])
                        await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"Error, Current Channel Doesnt Have NSFW enabled.", description="You can enable it by going into ``channel settings``", color=0xff0008)
            embed.set_image(url='https://i.imgur.com/oe4iK5i.gif')
            await ctx.send(embed=embed)

    @commands.command()
    async def solo(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as session:
                async with session.get('https://nekos.life/api/v2/img/solog') as r:
                    if r.status == 200:
                        js = await r.json()
                        embed = discord.Embed(title=f"Solo NSFW", color=0x08fffb)
                        embed.set_image(url=js['url'])
                        await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"Error, Current Channel Doesnt Have NSFW enabled.", description="You can enable it by going into ``channel settings``", color=0xff0008)
            embed.set_image(url='https://i.imgur.com/oe4iK5i.gif')
            await ctx.send(embed=embed)

    @commands.command()
    async def cum(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as session:
                async with session.get('https://nekos.life/api/v2/img/cum') as r:
                    if r.status == 200:
                        js = await r.json()
                        embed = discord.Embed(title=f"Cum NSFW", color=0x08fffb)
                        embed.set_image(url=js['url'])
                        await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"Error, Current Channel Doesnt Have NSFW enabled.", description="You can enable it by going into ``channel settings``", color=0xff0008)
            embed.set_image(url='https://i.imgur.com/oe4iK5i.gif')
            await ctx.send(embed=embed)

    @commands.command()
    async def neko(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as session:
                async with session.get('https://nekos.life/api/v2/img/nsfw_neko_gif') as r:
                    if r.status == 200:
                        js = await r.json()
                        embed = discord.Embed(title=f"Neko NSFW", color=0x08fffb)
                        embed.set_image(url=js['url'])
                        await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"Error, Current Channel Doesnt Have NSFW enabled.", description="You can enable it by going into ``channel settings``", color=0xff0008)
            embed.set_image(url='https://i.imgur.com/oe4iK5i.gif')
            await ctx.send(embed=embed)
    
    @commands.command()
    async def eroneko(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as session:
                async with session.get('https://nekos.life/api/v2/img/eron') as r:
                    if r.status == 200:
                        js = await r.json()
                        embed = discord.Embed(title=f"Ero Neeko NSFW", color=0x08fffb)
                        embed.set_image(url=js['url'])
                        await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"Error, Current Channel Doesnt Have NSFW enabled.", description="You can enable it by going into ``channel settings``", color=0xff0008)
            embed.set_image(url='https://i.imgur.com/oe4iK5i.gif')
            await ctx.send(embed=embed)

    @commands.command()
    async def smallboobs(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as session:
                async with session.get('https://nekos.life/api/v2/img/smallboobs') as r:
                    if r.status == 200:
                        js = await r.json()
                        embed = discord.Embed(title=f"Small Boobs NSFW", color=0x08fffb)
                        embed.set_image(url=js['url'])
                        await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"Error, Current Channel Doesnt Have NSFW enabled.", description="You can enable it by going into ``channel settings``", color=0xff0008)
            embed.set_image(url='https://i.imgur.com/oe4iK5i.gif')
            await ctx.send(embed=embed)        

    @commands.command()
    async def boobs(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as session:
                async with session.get('https://nekos.life/api/v2/img/tits') as r:
                    if r.status == 200:
                        js = await r.json()
                        embed = discord.Embed(title=f"Tits NSFW", color=0x08fffb)
                        embed.set_image(url=js['url'])
                        await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"Error, Current Channel Doesnt Have NSFW enabled.", description="You can enable it by going into ``channel settings``", color=0xff0008)
            embed.set_image(url='https://i.imgur.com/oe4iK5i.gif')
            await ctx.send(embed=embed)  

    @commands.command()
    async def waifu(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as session:
                async with session.get('https://nekos.life/api/v2/img/Waifu') as r:
                    if r.status == 200:
                        js = await r.json()
                        embed = discord.Embed(title=f"Waifu NSFW", color=0x08fffb)
                        embed.set_image(url=js['url'])
                        await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"Error, Current Channel Doesnt Have NSFW enabled.", description="You can enable it by going into ``channel settings``", color=0xff0008)
            embed.set_image(url='https://i.imgur.com/oe4iK5i.gif')
            await ctx.send(embed=embed) 

    @commands.command()
    async def pussy(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as session:
                async with session.get('https://nekos.life/api/v2/img/pussy') as r:
                    if r.status == 200:
                        js = await r.json()
                        embed = discord.Embed(title=f"Pussy NSFW", color=0x08fffb)
                        embed.set_image(url=js['url'])
                        await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"Error, Current Channel Doesnt Have NSFW enabled.", description="You can enable it by going into ``channel settings``", color=0xff0008)
            embed.set_image(url='https://i.imgur.com/oe4iK5i.gif')
            await ctx.send(embed=embed)   

    @commands.command()
    async def finger(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as session:
                async with session.get('https://nekos.life/api/v2/img/pwankg') as r:
                    if r.status == 200:
                        js = await r.json()
                        embed = discord.Embed(title=f"Finger NSFW", color=0x08fffb)
                        embed.set_image(url=js['url'])
                        await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"Error, Current Channel Doesnt Have NSFW enabled.", description="You can enable it by going into ``channel settings``", color=0xff0008)
            embed.set_image(url='https://i.imgur.com/oe4iK5i.gif')
            await ctx.send(embed=embed)   

    @commands.command()
    async def pussylick(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as session:
                async with session.get('https://nekos.life/api/v2/img/kuni') as r:
                    if r.status == 200:
                        js = await r.json()
                        embed = discord.Embed(title=f"Pussy Lick NSFW", color=0x08fffb)
                        embed.set_image(url=js['url'])
                        await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"Error, Current Channel Doesnt Have NSFW enabled.", description="You can enable it by going into ``channel settings``", color=0xff0008)
            embed.set_image(url='https://i.imgur.com/oe4iK5i.gif')
            await ctx.send(embed=embed)   

    @commands.command()
    async def erokemo(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as session:
                async with session.get('https://nekos.life/api/v2/img/erokemo') as r:
                    if r.status == 200:
                        js = await r.json()
                        embed = discord.Embed(title=f"Erokemo NSFW", color=0x08fffb)
                        embed.set_image(url=js['url'])
                        await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"Error, Current Channel Doesnt Have NSFW enabled.", description="You can enable it by going into ``channel settings``", color=0xff0008)
            embed.set_image(url='https://i.imgur.com/oe4iK5i.gif')
            await ctx.send(embed=embed)   

    @commands.command()
    async def holo(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as session:
                async with session.get('https://nekos.life/api/v2/img/holo') as r:
                    if r.status == 200:
                        js = await r.json()
                        embed = discord.Embed(title=f"Holo NSFW", color=0x08fffb)
                        embed.set_image(url=js['url'])
                        await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"Error, Current Channel Doesnt Have NSFW enabled.", description="You can enable it by going into ``channel settings``", color=0xff0008)
            embed.set_image(url='https://i.imgur.com/oe4iK5i.gif')
            await ctx.send(embed=embed)   

    @commands.command()
    async def keta(self, ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as session:
                async with session.get('https://nekos.life/api/v2/img/keta') as r:
                    if r.status == 200:
                        js = await r.json()
                        embed = discord.Embed(title=f"Keta NSFW", color=0x08fffb)
                        embed.set_image(url=js['url'])
                        await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"Error, Current Channel Doesnt Have NSFW enabled.", description="You can enable it by going into ``channel settings``", color=0xff0008)
            embed.set_image(url='https://i.imgur.com/oe4iK5i.gif')
            await ctx.send(embed=embed)  

def setup(client):
    client.add_cog(NSFW(client))