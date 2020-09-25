import discord
import random
from config import discord_token

client = discord.Client()  # Connect to Discord


@client.event
async def on_ready():  # Lets the server know that the bot is logged in and ready to be used
    print('{0.user} is ready'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:  # Lets the bot actually talk
        return

    if message.content.startswith('!bower'):  # Listens for the !bower command
        await message.channel.send('Hello World?')

    if message.content.startswith('!bin'):
        send_message = message.content
        send_message = send_message.replace('!bin', '')
        try:
            send_message = int(send_message)
            send_message = format(send_message, "06b")
            await message.channel.send(send_message)
        except TypeError:
            await message.channel.send("Please try again with a valid number")

    if message.content.startswith('!hex'):
        send_message = message.content
        send_message = send_message.replace('!hex', '')
        try:
            send_message = int(send_message)
            send_message = hex(send_message)
            await message.channel.send(send_message)
        except TypeError:
            await message.channel.send("Please try again with a valid number")

    if message.content.startswith('!b2d'):
        send_message = message.content
        send_message = send_message.replace('!b2d', '')
        try:
            send_message = int(send_message, 2)
            await message.channel.send(send_message)
        except TypeError:
            await message.channel.send("Please try again with a valid number")

    if message.content.startswith('!h2d'):
        send_message = message.content
        send_message = send_message.replace('!h2d', '')
        try:
            send_message = int(send_message, 16)
            await message.channel.send(send_message)
        except TypeError:
            await message.channel.send("Please try again with a valid number")

    if message.content.startswith('!quote'):
        quote_list = ["Remember the double? We will do that in chapter 12 - Brower",
                      "Can't put a double number in an integer register - Brower",
                      "32 zeros, 32 ones - Brower",
                      "ECX is a fixed loop, E.G. counting loop (For loop) - Brower",
                      "ESP is your stack pointer - Brower",
                      "Don't touch ESP - Brower",
                      "Did anyone ever tell you couldn't do any harm? Don't touch ESP. - Brower",
                      "EAX, EBX, ECX, and EDX are most commonly used - Brower",
                      "You got the rare quote! You lucky duck."]

        quote = random.choice(quote_list)
        await message.channel.send(quote)

    if message.content.startswith('!help'):
        help_string = "!bin n - Converts n into its binary value. \n" \
                      "!hex n - Converts n into its hex value. \n" \
                      "!b2d n - Converts binary n into its decimal value \n" \
                      "!h2d n - Converts hex n into its decimal value \n" \
                      "!quote - Returns a quote from Prof. Brower himself. \n" \
                      "You also could DM me if you want, I won't judge."
        await message.channel.send(help_string)


client.run(discord_token)  # Runs the bot with its token
