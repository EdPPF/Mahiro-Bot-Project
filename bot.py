import os
import discord
from discord.ext import commands
import responses
from dotenv import load_dotenv


def run_discord_bot():
    load_dotenv()
    TOKEN = os.getenv('TOKEN')

    intents = discord.Intents.default()
    intents.message_content = True
    
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print(f'Mahiro está online como {bot.user.name}!')

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        
        # Process commands defined bellow this event.
        await bot.process_commands(message)
        
        username = str(message.author)
        user_message = str(message.content)
        print(f'{username} said: "{user_message}".')  # For debugging

        '''
        This is a prototype of a more "complex" chat with the bot.
        The ideia is for the bot to respond only when it's name is mentioned.
        '''
        if "mahiro" in user_message.lower():  # checking if the user calls for Mahiro
            try:
                if user_message[0] == '?':
                    user_message = user_message[1:]
                    response = responses.handle_response(user_message)  # handle_response has only call, for now
                    await message.author.send(response)
                else:
                    response = responses.handle_response(user_message)
                    await message.channel.send(response)
            except Exception as e:
                print(e)
    
    @bot.command()
    async def about(ctx):
        aboutm = "Mahiro Bot V 1.0\nPor enquanto eu só respondo a comandos específicos e ao meu nome... mas em breve terá mais!\n- Código disponível em:\nhttps://github.com/EdPPF/Mahiro-Bot-Project.git"
        await ctx.send(aboutm)

    @bot.command()
    async def coms(ctx):
        lcoms = ["`!about`", "`!coms`", "`!ajuda`"]
        await ctx.send(lcoms)

    @bot.command()
    async def ajuda(ctx):
        helpm = "Para uma lista de comandos, digite `!coms`. Para receber uma resposta minha no privado, inicie sua mensagem com `?`."
        await ctx.send(helpm)

    @bot.command()
    async def image(ctx):  # For testing
        await ctx.send(file=discord.File('imgs\oopsie.png'))

    bot.run(TOKEN)
