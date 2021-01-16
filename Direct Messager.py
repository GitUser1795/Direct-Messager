import discord

@bot.command(pass_context=True)
async def DM(message):
    await client.send_message(client.message.author, '')
