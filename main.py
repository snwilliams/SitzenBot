import os
import discord
from discord.ext import tasks

client = discord.Client()


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if client.user.mentioned_in(message):
      await message.channel.send("You can type `$help` to see what I can do!")
      print('someone mentioned me!!')
  
  if message.content.startswith('$help'):
      await message.channel.send("I am a reminder bot."
      + "\nType $sit, and I'll remind you to stand in one hour"
      + "\nType $stand, and I'll remind you to stand in one hour")
  
  if message.content.startswith('$sit'):
    await message.channel.send("I'll remind you to stand in one hour")
    slow_count_sit.start(message.channel)

  if message.content.startswith('$stand'):
    await message.channel.send("I'll remind you to sit in one hour")
    slow_count_stand.start(message.channel)


@tasks.loop(seconds=36000, count=1)
async def slow_count_sit(channel):
    print(slow_count_sit.current_loop)

@slow_count_sit.after_loop
async def after_slow_count():
    channel = client.get_channel(917806862534053958)
    print('done!')
    await channel.send("It's time to stand!")

@tasks.loop(seconds=36000, count=1)
async def slow_count_stand(channel):
    print(slow_count_sit.current_loop)

@slow_count_sit.after_loop
async def after_slow_count_stand():
    channel = client.get_channel(917806862534053958)
    print('done!')
    await channel.send("It's time to sit!")
    

client.run(os.environ['bot_key'])

