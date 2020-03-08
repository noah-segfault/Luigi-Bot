import discord
import random
#import os
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = '.')
status = [
        'In the studio cookin up schmeats',
        'Uploadin to the hub',
        'Cleanin off the Gooigi',
        'Playing WiiU',
        'Waiting for Eternal Atake',
        'Writing 10 page essay for COM 1000',
        'Speedrunning Mii Maker Peter Griffin Mii',
        'Off da lokos!!!',
        'Watching Chew Jitsu',
        'Inventing something for Izaya',
        'Asking around for rides',
        'Bubsy 3D',
        "Everything Donkey, I love when it's hot!",
        'Recommending Die Lit to everyone',
        'Luigi wins again!'
    ]

@client.event
async def on_ready():
    print('You can now play as Luigi.')
    #change_status.start()
    await client.change_presence(status=discord.Status.online)
    await client.change_presence(activity=discord.Game(random.choice(status)))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Luigi doesn't have this on file... \n (Invalid command used)")

@client.command(aliases = ['A', 'a', 'A Button', 'a Button', 'A button', 'a button'])
async def portrait(ctx):
    await ctx.send('Me...You like?')
    await ctx.send('https://imgur.com/KhKa94U')

@client.command()
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit = amount)
    await ctx.send('Kingu Creamson!!!\n(Luigi has erased messages! And time!!!)')

@client.event
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Luigi is so confused rn. \n(Please specify amount of messages to be deleted)')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event 
async def on_member_remove(member):
    print(f'{member} has left a server')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ['As I see it, yes.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again.',
            'Don’t count on it.',
            'It is certain.',
            'It is decidedly so.',
            'Most likely.',
            'My reply is no.',
            'My sources say no.'
            'Outlook not so good.',
            'Outlook good.',
            'Reply hazy, try again.',
            'Signs point to yes.',
            'Very doubtful.',
            'Without a doubt.',
            'Yes.',
            'Yes – definitely.',
            'You may rely on it.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')





client.run('Njg1OTQyNTA0Mzk0MTk1MDkz.XmQAOg.TOBWwIelBR4WFzVHmgmgbLb08FM')

