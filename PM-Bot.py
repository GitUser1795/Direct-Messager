import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='-') #You can change the command prefix here. I have inputted - .

@bot.event
async def on_ready():
    print("The bot is ready!") #If you see this message on your prompt, the bot is ready to be deployed.

@bot.command()
async def PM(ctx, user: discord.User, *, value):
    await user.send(f"**Sent by {ctx.author.display_name}**: ") #Shows who sent the message to the recipient.
    await user.send(f"{value}") #Shows the message itself.

bot.run('') #Input your own bot's token, but I would suggest using dotenv to hide it in a file.