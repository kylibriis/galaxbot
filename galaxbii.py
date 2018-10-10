import discord
from discord.ext import commands
import random
import json
import os

TOKEN = "BOT_TOKEN"

bot = commands.Bot(command_prefix="b!")

print('galaxbot is online')

@bot.command()
async def niko():
    await bot.change_presence(game=discord.Game(name='having sex w/ niko'))
    await bot.send_message('got it, chief')

@bot.command()
async def notniko():
    await bot.change_presence(game=discord.Game(name='not having sex w/ niko'))
    await bot.send_message('got it, chief')

@bot.command(pass_context=True)
async def alex(ctx):
    channel = ctx.message.channel
    await bot.send_message(channel, 'https://cdn.discordapp.com/attachments/482590853223940103/496099926976102420/90012321_istanbul.png')

@bot.command(pass_context=True)
async def diceroll(ctx):
    channel = ctx.message.channel
    numbers = ('1','2','3','4','5','6')
    await bot.send_message(channel, random.choice(numbers))

@bot.command(pass_context=True)
async def roulette(ctx):
    channel = ctx.message.channel
    authorID = ctx.message.author.mention
    possibilities = ('1','2','3','4','5','6')
    outcome = random.choice(possibilities)
    if(outcome == '1'):
        await bot.send_message(channel, authorID+ ' has been shot')
        await bot.kick(ctx.message.author)
    if (outcome != '1'):
        await bot.send_message(channel, authorID + ' is safe')

@bot.command(pass_context=True)
async def roulettehard(ctx):
    channel = ctx.message.channel
    authorID = ctx.message.author.mention
    possibilities = ('1','2','3','4','5','6')
    outcome = random.choice(possibilities)
    if(outcome != '1'):
        await bot.send_message(channel, authorID+ ' has been shot')
        await bot.kick(ctx.message.author)
    if (outcome == '1'):
        await bot.send_message(channel, authorID + ' is safe')

@bot.command(pass_context=True)
async def name(ctx):
    alphabetv0 = ['a', 'e', 'i', 'o', 'u'];

    alphabetc0 = ['ch', 'br', 'sh', 'th', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's',
                  's', 't', 'v', 'w', 'z'];

    alphabetv = ['a', 'e', 'ee', 'i', 'o', 'u', 'y'];

    alphabetc = ['ch', 'br', 'sh', 'th', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 's',
                 't', 'v', 'w', 'z'];

    alphabetv2 = ['a', 'e', 'i', 'ee', 'o', 'u', 'y', ''];

    alphabetc2 = ['ch', 'sh', 'th', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 's', 't',
                  'v', 'w', 'z', ''];

    alphabetv3 = ['a', 'e', 'i', 'o'];

    alphabetc3 = ['b', 'c', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 't', 'v', 'w', 'z', ''];

    pee = ["1", "2"]
    z = random.choice(pee)

    if (z == "1"):
        a = random.choice(alphabetv0);
    if (z == "2"):
        a = random.choice(alphabetc0);

    if (z == "1"):
        b = random.choice(alphabetc);
    if (z == "2"):
        b = random.choice(alphabetv);

    if (z == "1"):
        c = random.choice(alphabetv);
    if (z == "2"):
        c = random.choice(alphabetc);

    if (z == "1"):
        d = random.choice(alphabetc);
    if (z == "2"):
        d = random.choice(alphabetv);

    if (d != ''):
        if (z == "1"):
            e = random.choice(alphabetv2);
        if (z == "2"):
            e = random.choice(alphabetc2);
    else:
        e = ''

    if (e != ''):
        if (z == "1"):
            f = random.choice(alphabetc2);
        if (z == "2"):
            f = random.choice(alphabetv2);
    else:
        f = '';

    if (f != ''):
        if (z == "1"):
            g = random.choice(alphabetv3);
        if (z == "2"):
            g = random.choice(alphabetc3);
    else:
        g = '';

    await bot.send_message(ctx.message.channel, a + b + c + d + e + f + g);

@bot.command(pass_context=True)
async def on_message(ctx):
    await bot.send_message(ctx.message.channel, ctx.message.content)

bot.run(process.env.TOKEN)
