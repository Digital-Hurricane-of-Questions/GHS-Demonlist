import discord, os, token

bot = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!demonlist") or message.content.startswith("!ds"):
        await message.channel.send(os.system("python demonlist.py" + message.content[message.content.find(" ")+1:]))

bot.run(os.getenv(token.token))