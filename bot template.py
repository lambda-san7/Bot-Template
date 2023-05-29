import discord
import os

os.system("title Bot")

intents = discord.Intents(messages=True)

client = discord.Client(intents=discord.Intents.all())

previous = "default"
  
@client.event
async def on_ready():
  print(f'<bot> I\'m online')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  else:
    if "hi" in message.content.lower():
      await message.channel.send("hi")


client.run("your Token")
