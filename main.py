import discord
import os
from dotenv import load_dotenv
import util

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    channel = client.get_channel(int(os.getenv('CHANNEL_ID')))

    if message.author == client.user:
        return

    mess = message.content.split(' ')
    mess = mess[0].strip()
    if message.channel == channel:
        lastMsg = util.readFile()
        if not mess.isnumeric():           
            await message.delete()
            prompt = f"Message sent by {message.author.mention} was deleted because it violated game rules.\nLast valid count: {lastMsg}"
            await channel.send(prompt)
        else:
            res = int(mess)- lastMsg
            if  res != 1:
                await message.delete()
                prompt = f"Message sent by {message.author.mention} was deleted because it violated game rules.\nLast valid count: {lastMsg}"
                await channel.send(prompt)
            else:
                util.writeFile(str(lastMsg+1))

client.run(os.getenv('BOT_TOKEN'))
