#import dependencies
import discord
from discord.ext import commands
import os

#defines the input
os.system("cls")
input1 = input("Prefix > ")
input2 = input("Token > ")

#defines client
client = commands.Bot(command_prefix=f"{input1}", self_bot=True)

#when the selfbot is online
@client.event
async def on_ready():
 os.system("cls")
 print(f"Username: {client.user}")
 print(f"Prefix: {input1}")

#basic commmand (say)
@client.command()
async def say(ctx, msg=''):
 await ctx.send(f"{msg}")

#logs in with the token
client.run(f"{input2}", bot=False)
