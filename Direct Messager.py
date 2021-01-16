import discord

@bot.command(pass_context=True)
async def poke(ctx, message):
    await client.send_message(ctx.message.author, '')