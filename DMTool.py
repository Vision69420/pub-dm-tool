# if u skid i will fucking rape u :3
import discord
from discord.ext import commands
import random
from discord import Client, Permissions
from colorama import Back, Fore as F, Style
from pystyle import Colorate, Colors as C, Write
import asyncio
import time
import json
from terminut import BetaConsole, Console, printf, init
import os

Console.init(debug=True)

os.system('cls')

Console.printf("[DEBUG] Should Not Show")
Console.printf("[INFO] Should Show")

c = BetaConsole(speed=2)
intents = discord.Intents.all()

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

tokens = []
try:
    with open('tokens.txt', 'r') as file:
        print(f"{C.pink}Reading Tokens...{C.reset}")
        tokens = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    print("tokens.txt file not found make sure it exists and has valid tokens")
    exit()

async def dm_spam(token, user_id, message):
    Vision = commands.Bot(command_prefix=".", intents=discord.Intents.all())

    @Vision.event
    async def on_ready():
        asyncio.sleep(1)
        print(f"Logged in as {user.name}")
        asyncio.sleep(1)
        try:
            user = await Vision.fetch_user(user_id)
            print(f"Fetched user {user.name}")
        except Exception as e:
            print(f"Error fetching user >> {e}")
            await Vision.close()
            return

        print(f"Starting to DM {user.name}")

        while True:
            try:
                await user.send(message)
                timestamp = c.getTimestamp()
                c.alphaPrint(" [ INF ]", f"[{timestamp}] {C.green}Sent Message{C.reset} {user.name} {C.green} ({C.reset}{user.id}{C.green}){C.reset}")
                await asyncio.sleep(0.5)
            except discord.Forbidden:
                timestamp = c.getTimestamp()
                c.alphaPrint(" [ ERROR ]", f"[{timestamp}] DMs are closed lulz {C.green} ({C.reset}{user.id}{C.green}){C.reset}")
                break

    try:
        await Vision.start(token)
    except Exception as e:
        print(f"Failed to login with token {token}: {e}")

randomtimes = [4, 5, 3, 6]

banner = """ 
                                     __   _  _  ____  ____  _  _  _  _  ____  ____    ____  _  _ 
                                    / _\ ( \/ )(  __)(_  _)/ )( \( \/ )/ ___)(_  _)  (    \( \/ )
                                   /    \/ \/ \ ) _)   )(  ) __ ( )  / \___ \  )(     ) D (/ \/ \ 
                                   \_/\_/\_)(_/(____) (__) \_)(_/(__/  (____/ (__)   (____/\_)(_/


"""

async def main():
    delay = random.choice(randomtimes)
    await asyncio.sleep(delay)
    os.system('cls'); os.system(f'title Amethyst DM V2 by Vision Tokens: {len(tokens)}'); print(Colorate.Vertical(C.blue_to_purple, banner))

    user_id = input(f"{C.gray}({C.purple}?{C.gray}){C.reset} Enter the user ID to send messages to >> ")
    message = input(f"{C.gray}({C.purple}?{C.gray}){C.reset} Enter the message to spam >> ")

    tasks = [dm_spam(token, user_id, message) for token in tokens]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
# if u skid i will fucking rape u :3
