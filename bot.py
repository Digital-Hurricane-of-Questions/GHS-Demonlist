import discord, os, token

bot = discord.Client()

@client.event
async def on_message(message):
    text = message.content
    if text[:3] = "!ds":
        text = "!demonlist show" + text[3:]
    if message.author == client.user:
        return
    if text.startswith("!demonlist"):
        space_point = text.find(" ")+1
        command = text[space_point: text[space_point+1:].find(" ")]
        await message.channel.send(os.system("python demonlist.py" + text[text.find(" ")+1:]))

bot.run(os.getenv(token.token))