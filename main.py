import os
import discord

client = discord.Client()

@client.event
async def on_ready():
  print('I am online as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Guten Tag!')

client.run(os.environ['bot_key'])

