import os
import discord
import responses
from dotenv import load_dotenv

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_message(message):
        if message.author == client.user: # client.user == bot. Não queremos que o bot responda a si mesmo
            return # Impede interação infinita entre bot e ele mesmo
        
        username =     str(message.author)
        user_message = str(message.content)
        channel =      str(message.channel)

        print(f'{username} excreveu: "{user_message}" ({channel})') # Para debbugging

        if user_message[0] == "?":
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord! weeeee')

    client.run(TOKEN)
