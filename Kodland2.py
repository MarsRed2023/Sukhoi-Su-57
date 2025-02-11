import discord
from discord.ext import commands
import time
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$Crash'):
        await message.channel.send("Terrorist bombing")
    elif message.content.startswith("$eos"):
        await message.channel.send("English or Spanish")
    if message.content.startswith("English"):
        await message.channel.send("Whoever moves first is gay")
        time.sleep(5)
        await message.channel.send("Done")
    elif message.content.startswith("Spanish"):
        await message.channel.send("El que se mueva primero es gay")
        time.sleep(5)
        await message.channel.send("Ya")
    elif message.content.startswith("French"):
        await message.channel.send("Celui qui bouge en premier est gay")
        time.sleep(5)
        await message.channel.send("Ya")
    elif message.content.startswith("German"):
        await message.channel.send("Wer sich zuerst bewegt, ist schwul")
        time.sleep(5)
        await message.channel.send("Ya")
    elif message.content.startswith("Que hora es"):
        await message.channel.send("La misma de ayer")
    elif message.content.startswith("Terrorismo"):
        await message.channel.send("es malo")
    elif message.content.startswith("Clear for take off"):
        await message.channel.send("Clear for take off indeed!")
    elif message.content.startswith("discord"):
        await message.channel.send("Estamos en discord")
    
    elif message.content.startswith("$planepedia"):
        await message.channel.send("https://planepediacrashesandemergencylandings.fandom.com/wiki/Planepedia_Wiki")

    elif message.content.startswith("$audio"):
        await message.channel.send(file=discord.File("C:/Users/cior2/Downloads/japan-eas-alarm-1945-made-with-Voicemod.mp3"))

    elif message.content.startswith("$video"):
        await message.channel.send(file=discord.File("C:/Users/cior2/Downloads/92abc012-86d5-4b7e-9e45-1441c1f2552c.mp4"))

    elif message.content.startswith("$list"):
        await message.channel.send("Alright Im gonna count my slaves now")
        time.sleep(2.5)
        n = 1
        while True: 
            if n < 100:
                await message.channel.send(f"Nigga #{n}")
                n += 1
                time.sleep(0.2)
            else:
                break
    else:
        await message.channel.send(message.content)
    
client.run('EL TOKEN FUE REMOVIDO POR SEGURIDAD')
