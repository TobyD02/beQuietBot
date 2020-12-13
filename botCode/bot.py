import discord
import json

with open("poultonpeeps.json") as json_file:
    pp = json.load(json_file)

users = pp["Users"]
TOKEN = pp["Token"]

client = discord.Client()

@client.event
async def on_message(message):
    if message.author.id not in [users["Tommy"], users["Huw"]]:
        await message.delete()
    if message.author.id not in [users["Tommy"], users["Huw"]]:
        await client.get_channel(777630408438448171).send("shut up", tts = False)

@client.event
async def on_voice_state_update(member, before, after):
    if(member.id not in [users["Tommy"], users["Huw"]]):
        if(after.mute == False):
            await member.edit(mute=True)

client.run(TOKEN)