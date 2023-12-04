import discord
import random
import requests
import datetime
import asyncio
import aiohttp


url = 'x' #buraya urlyi gir

intents = discord.Intents.all()
intents.members = True

client = discord.Client(intents=intents)

async def site_check():
    while True:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    date_time = datetime.datetime.now().strftime('%d %m %Y %H:%M')
                    await client.wait_until_ready()
                    channel = client.get_channel(1086391661262815242)
                    await channel.send(f" {date_time}\doldur burayi :white_check_mark:") #istedigini yazabilirsin
                    with open("image.png", "rb") as f:
                        picture = discord.File(f)
                    await channel.send(file=picture)
        await asyncio.sleep(7200)



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="istedigin yazi"))
    print('online')
    client.loop.create_task(site_check())




client.run('MTA4OTE1MDA4NTY2Mjc4MTQ2MA.G8j31q.nWI853oqnZiwXHWzarDQW2cd_gHjlpTlgu9TYg')
