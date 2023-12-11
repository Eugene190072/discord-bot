import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return
    
        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def привет(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def help(ctx):
    await ctx.send(f'$привет ; $on_ready ; $roll ; $add')

bot.run("MTE4MDE3OTA5NDE2NDQ4ODI3Mw.G9zwNw.4cks14uINEgKIdYm8R3YEAKNJW0NRD94XLP-WUd")
