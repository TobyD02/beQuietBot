import discord

users = {"Toby": 239721016358731776, "Huw": 234751513266880512, "Tommy": 234752682978574336,
         "Adam": 186801742220886016, "Ben": 727195647912050860, "Cas": 261218381129187339,
         "Summer": 781317430991388683, "Ella": 781317430991388683, "Joe": 467324781184811018,
         "Jacob": 766318299726217236, "Sam": 706159503724511373, "Leon": 494563916903350273}

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