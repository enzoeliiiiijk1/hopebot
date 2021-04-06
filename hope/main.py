import discord
import asyncio
import json
import os, sys
import datetime
from discord import Game, user
from discord.ext import commands, tasks
from discord.utils import get
from itertools import cycle
from time import sleep
from colorama import Fore, Style

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
Prefix = config.get('prefix')

players = {}
queues = {}

client = commands.Bot(command_prefix = Prefix, case_insensitive = True, intents = discord.Intents.all())
client.remove_command('help')

def Clear():
    os.system("cls" if os.name == "nt" else "clear")
Clear()

def owners_only(ctx):
    return ctx.author.id == 815648488574025728, 776126371440754698

@client.event
async def on_ready():
    print(f'''{Fore.RESET}
        {Fore.RED}{Style.BRIGHT}        
        {Fore.RED}{Style.BRIGHT}        ██╗░░██╗░█████╗░██████╗░███████╗  ██████╗░░█████╗░███╗░░██╗███████╗██╗░░░░░
        {Fore.RED}{Style.BRIGHT}        ██║░░██║██╔══██╗██╔══██╗██╔════╝  ██╔══██╗██╔══██╗████╗░██║██╔════╝██║░░░░░
        {Fore.RED}{Style.BRIGHT}        ███████║██║░░██║██████╔╝█████╗░░  ██████╔╝███████║██╔██╗██║█████╗░░██║░░░░░
        {Fore.RED}{Style.BRIGHT}        ██╔══██║██║░░██║██╔═══╝░██╔══╝░░  ██╔═══╝░██╔══██║██║╚████║██╔══╝░░██║░░░░░
        {Fore.RED}{Style.BRIGHT}        ██║░░██║╚█████╔╝██║░░░░░███████╗  ██║░░░░░██║░░██║██║░╚███║███████╗███████╗
        {Fore.RED}{Style.BRIGHT}        ╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚══════╝  ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝╚══════╝
        {Fore.RED}{Style.BRIGHT}           
        {Fore.RED}{Style.BRIGHT}    Client ID: {Fore.MAGENTA}{Style.BRIGHT}{client.user.id}
        {Fore.RED}{Style.BRIGHT}    Servers:{Fore.MAGENTA}{Style.BRIGHT} {len(client.guilds)}
        {Fore.RED}{Style.BRIGHT}    Prefix:{Fore.MAGENTA}{Style.BRIGHT} >
        {Fore.RED}{Style.BRIGHT}
        {Fore.RED}{Style.BRIGHT}
    '''+Fore.RESET)

async def ch_pr():
    await client.wait_until_ready()

    while not client.is_closed():
        
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(set(client.get_all_members()))} Members"))

        await asyncio.sleep(5)

        await client.change_presence(activity=discord.Game(name=">help"))

        await asyncio.sleep(5)
                                                
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} servers"))

        await asyncio.sleep(5)

client.loop.create_task(ch_pr())

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(description = "Command Not Found. Type ``>help`` For A List Of Commands.", color =0xFF0000)
        await ctx.send(embed=embed)
        return
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description = "Bad Arguements. Please Try Again.", color =0xFF0000)
        await ctx.send(embed=embed)
        return
    if isinstance(error, commands.CommandOnCooldown):
        return
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description = "Missing Required Arguements. Please Try Again.", color =0xFF0000)
        await ctx.send(embed=embed)
        return
    else:
        raise error

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(f'{token}')
