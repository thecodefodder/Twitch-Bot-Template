import os
from dotenv import load_dotenv
from twitchio.ext import commands
import requests

load_dotenv()
client_token = os.getenv('TOKEN')

def generateJoke():
    r = requests.get('https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,political,racist,sexist')
    joke_data = r.json()

    if joke_data['type'] == 'single':
        joke = joke_data['joke']
    elif joke_data['type'] == 'twopart':
        joke = f"{joke_data['setup']} {joke_data['delivery']}"
    else:
        joke = 'Oops! Something went wrong while fetching the joke.'

    return joke

class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=client_token, prefix='!', initial_channels=['thecodefodder1'])

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Send a hello back!
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command()
    async def github(self, ctx: commands.Context):
        await ctx.send(f'https://github.com/thecodefodder')

    @commands.command()
    async def joke(self, ctx: commands.Context):
        joke = generateJoke()
        await ctx.send(joke)

bot = Bot()
bot.run()
