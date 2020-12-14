import discord
import json
import random

from discord.ext import commands

with open("poultonpeeps.json") as json_file:
    pp = json.load(json_file)

users = pp["Users"]
TOKEN = pp["Token"]
comebacks = pp["Comebacks"]
targets = pp["Targets"]

bot = commands.Bot('!')



@bot.command()
async def comeback(ctx, ):
    if ctx.message.author.id not in targets:
        index = random.randint(0, len(comebacks))
        await ctx.send(comebacks[index])


@bot.command()
async def target(ctx, member: discord.Member = None):
    if ctx.message.author.id not in targets:
        if member == None:
            await ctx.send("User not found")
            return
        targets.append(member.id)
        pp["Targets"] = targets
        with open("poultonpeeps.json", "w") as f:
            json.dump(pp, f)

@bot.command()
async def rmtarget(ctx, member: discord.Member = None):
    if ctx.message.author.id not in targets:
        if member == None:
            await ctx.send("User not found")
            return
        if member.id not in targets:
            await ctx.send("User not targeted")
            return
        else:
            targets.remove(member.id)
            with open("poultonpeeps.json", "w") as f:
                json.dump(pp, f)


@bot.event
async def on_message(message):
    if message.author.id in targets:
        await message.delete()
    if message.author.id in targets:
        channel = message.channel
        await channel.send("shut up", tts = False)
    await bot.process_commands(message)

@bot.event
async def on_voice_state_update(member, before, after):
    if(member.id in targets):
        if(after.mute == False):
            await member.edit(mute=True)




bot.run(TOKEN)