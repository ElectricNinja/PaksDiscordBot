import discord
from discord.ext import commands
import random

TOKEN = DISCORD-TOKEN

intents=discord.Intents.all()

client = commands.Bot(command_prefix='!', intents=intents)

@client.command()
async def threaten(ctx, user:discord.Member, *, message=None):

    message = str(random.randint(1,10)) + " days"
    print("sent " + str(message) + "to " + str(user))
    embed=discord.Embed(title=message)

    await ctx.send(f'Uh Oh')
    await user.send(embed=embed)
@client.command(name='things')
async def send_img(ctx):

	await ctx.send("it me",file=discord.File('Recognizing_Things.png'))
@client.command(name='resetmine')
async def changeStuff(ctx):
    global mine
    mine = 100

    await ctx.send("reset")

@client.command(name='mine')
async def msg(ctx):
    global mine
    response = "you just mined my mine, structural integrity is at %" + str(mine) + '!'
    mine = mine - 10
    if (mine < 0):
        await ctx.send(f'you broke my mine and now I have no source of income :(')
    else:
        await ctx.send(response)


client.run(TOKEN)