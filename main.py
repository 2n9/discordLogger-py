# discord chat logging program
import discord
import os

token = open("token.txt", "r").read()
client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")

@client.event
async def on_message(message):
    if message.guild is None:
        return
    if message.author == client.user:
        return
    
    content = message.content
    author = message.author
    author_name = author.name
    author_id = author.id
    date = message.created_at
    channel = message.channel
    channel_name = channel.name
    channel_id = channel.id
    guild = message.guild
    guild_name = guild.name
    guild_id = guild.id

    file_name = str(guild_id) + os.sep + str(channel_name) + "-" + str(channel_id) + ".txt"

    if not os.path.exists(str(guild_id)):
        os.mkdir(str(guild_id))
    
    file = open(file_name, "at+", encoding="utf-8")
    file.write(str(date) + ": [" + str(author_name) + "] #" + str(author_id) + " > " + str(content) + "\n")
    file.close()

    # print console
    print("<" + str(guild_name) + "> <" + str(channel_name) + "> <" + str(author_name) + "> : " + content)

# run client
client.run(token)
