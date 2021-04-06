import discord
from discord.ext import commands
import requests
import getopt
import sys

class HELP(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def Help(self, ctx, choice = None):
        if choice == None:
            embed = discord.Embed(title=f"• Help Commands •", color=0x000000)
            embed.add_field(name=":smirk: nsfw", value="``>help nsfw``", inline=True)
            embed.add_field(name=":video_game: fun", value="``>help fun``", inline=True)
            embed.add_field(name=":information_source: info", value="``>help info``", inline=True)
            embed.add_field(name=":tools: util", value="``>help util``", inline=True)
            await ctx.send(embed=embed)
            await ctx.message.delete()
        elif choice == 'nsfw':
            embed = discord.Embed(title=f"• NSFW Commands •", description='''
            ``feet``, ``yuri``, ``trap``, ``futanari``, ``hololewd``, ``lewdkemo``, 
            ``cum``, ``erokemo``, ``lesbian``, ``lewd``, ``eroyuri``, ``eroneko``, 
            ``blowjob``, ``neko``, ``solo``, ``anal``, ``hentai``, ``erofeet``, 
            ``holo``, ``keta``, ``blowjob``, ``pussy``, ``tits``, ``finger``,
             ``pussylick``, ``waifu``, ``smallboobs``''', color=0x000000)
            await ctx.send(embed=embed)
            await ctx.message.delete()
            return
        elif choice == 'fun':
            embed = discord.Embed(title=f"• Fun Commands •", description='''
            ``ttt`` :regional_indicator_x:\n ``rps`` :rock: ''', color=0x000000)
            await ctx.send(embed=embed)
            await ctx.message.delete()
            return
        elif choice == 'util':
            embed = discord.Embed(title=f"• Utility/Admin Commands •", description='''
            ``ban`` <:PlayBoyRed:797168261346623559>\n ``unban`` <:PlayBoyBlue:797168304946675772>\n ``kick`` <a:PlayBoyGlitterPink:797168291847340052>\n ``purge`` <:PlayBoyPurple:797168270447869973>''', color=0x000000)
            await ctx.send(embed=embed)
            await ctx.message.delete()
            return
        elif choice == 'info':
            embed = discord.Embed(title=f"• Information Commands •", description='''
            ``channels`` <a:VerifyPink:797168125367681024>\n ``roleinfo {@role}`` <a:VerifyPink1:797168119084089375>\n ``avatar \ av`` <a:VerifyOrange:797168130560098304>\n ``serverlogo`` <a:VerifyGreen:797168141498843156>\n ``serverinfo`` <a:VerifyBlue:797168149945778227>\n ``userinfo`` <a:VerifyPurple:797168108845924352>\n ``about`` <a:VerifyBlack:797168209441587240>\n ``ping`` <a:VerifyYellow:797168103955234886> ''', color=0x000000)
            await ctx.send(embed=embed)
            await ctx.message.delete()
            return
    @commands.command()
    async def invite(self, ctx):
        inv = "https://discord.com/api/oauth2/authorize?client_id=825080679795523584&permissions=8&scope=bot"
        joinz = "https://discord.gg/Tw2BG5umB9"
        embed = discord.Embed(title=f"Helpful links", description=f"[Official Discord]({joinz})\n[Invite link]({inv})", color=0x000000)
        await ctx.author.send(embed=embed)
        await ctx.send(f"{ctx.author.mention} Invite link sent! <:sweat2:826677711346729010>")

def setup(client):
    client.add_cog(HELP(client))
