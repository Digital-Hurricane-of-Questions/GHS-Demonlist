import discord, os, discord-token, discord-lists

def do(text):
    os.system("python demonlist.py" + text[text.find(" ")+1:])

bot = discord.Client()

@client.event
async def on_message(message):
    text = message.content
    if text[:3] == "!ds":
        text = "!demonlist show" + text[3:]
    if message.author == client.user:
        return
    if text.startswith("!demonlist"):
        space_point = text.find(" ")+1
        command = text[space_point: text[space_point+1:].find(" ")]
        if command in lists.user_commands:
            send_text = await do
        elif command in lists.admin_commands:
            if lists.admin_role in message.author.roles():
                send_text = await do
            else:
                send_text = "You don't have enough rights!"
        elif command in lists.owner_commands:
            if lists.owner_role in message.author.roles():
                send_text = await do
            else:
                send_text = "You don't have enough rights!"
        
        message.channel.send(send_text)

bot.run(os.getenv(d_token.token))