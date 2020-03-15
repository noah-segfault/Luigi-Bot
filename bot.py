#This bot is capable of posting an image of itself
#providing its status and play 8ball
#Noah Law


import discord
import random
import youtube_dl
import os

from discord.ext import commands, tasks
from discord.utils import get 
from itertools import cycle

TOKEN = 'Njg1OTQyNTA0Mzk0MTk1MDkz.XmwKNQ.4sFYVYI4attZM5XhXyKI-E5Y4g4'
players = {}
client = commands.Bot(command_prefix = '!')
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

#Sets the status and activates the bot
@client.event
async def on_ready():
    print('You can now play as Luigi.')
    await client.change_presence(status=discord.Status.online)
    await client.change_presence(activity=discord.Game(random.choice(status)))

#Allows the bot to join the voice channel you're in
@client.command(pass_context=True, aliases=['j', 'join'])
async def _join(ctx): 
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"The bot has connected to {channel}\n")
    
    await ctx.send(f"Joined {channel}")

#Allows the bot to leave the voice channel
@client.command(pass_context=True, aliases=['l', 'leave'])
async def _leave(ctx): 
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"The bot has left {channel}\n")
        await ctx.send(f"Left {channel}")
    else:
        print("Bot was told to leave but was not in one")
        await ctx.send("Don't think I'm in a channel")

#Plays audio from YouTube, you'll need to send the exact link
@client.command(pass_context=True, aliases=['p', 'play'])
async def _play(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    #This will create an mp3 file to play, or remove the old one when you play a new song
    try:
        if song_there:
            os.remove("song.mp3")
            print("Removed old song file")
    except PermissionError:
        #Unfortunetly you cannot play a new song until the old song finishes :(.....for now
        print("Trying to delete son file, but it's being played")
        await ctx.send("ERROR: Music playing")
        return
    
    await ctx.send("Getting ready...")

    voice = get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key':'FFmpegExtractAudio',
            'preferredcodec':'mp3',
            'preferredquality':'192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print('Downloading audio now\n')
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print("Renamed file {file}\n")
            os.rename(file, "song.mp3")
    
    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e:print(f"{name} has finished playing"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    nname = name.rsplit("-", 2)
    await ctx.send(f"Playing: {nname}")
    print("Playing\n")

#Outputs an error message if command is invalid
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

#Ask Luigi a question and he'll answer randomly
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


client.run(TOKEN)

