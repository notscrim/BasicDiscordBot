import discord
import os

os.system("cls")

token = input("Token :")
print("Prefix 'b!'     first command 'b!test' you can edit it.")

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('b!test'):
        await message.channel.send('Working')

client.run("" + token + "")