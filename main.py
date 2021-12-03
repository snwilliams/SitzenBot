import os
import discord
from discord.ext import tasks

client = discord.Client()



@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Guten Tag!')
  
  if message.content.startswith('$sit'):
    slow_count.start(message.channel)


@tasks.loop(seconds=5.0, count=5)
async def slow_count(channel):
    print(slow_count.current_loop)
    await channel.send('test')

@slow_count.after_loop
async def after_slow_count():
    print('done!')
    

client.run(os.environ['bot_key'])

