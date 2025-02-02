import requests
from colorama import Fore, Style
from threading import Thread
import os
import datetime

YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
RED = Fore.RED
WHITE = Fore.WHITE
GREY = Fore.LIGHTBLACK_EX
RESET = Style.RESET_ALL

def name_switcher(tokens, maincolor):
    guild_id = input(f"                        {maincolor}[{WHITE}LITA{maincolor}] {WHITE}| {maincolor}[{WHITE}GUILD ID{maincolor}] {WHITE}>{maincolor} ")
    new_name = input(f"                        {maincolor}[{WHITE}LITA{maincolor}] {WHITE}| {maincolor}[{WHITE}NICKNAME{maincolor}] {WHITE}>{maincolor}")

    def process_token(token, maincolor):
        url = f'https://discord.com/api/v9/guilds/{guild_id}/members/@me'
        headers = {
            'Authorization': token
        }
        data = {
            'nick': new_name
        }
        try:
            response = requests.patch(url, headers=headers, json=data)
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            if response.status_code == 200:
                    print(f"                        {maincolor}[{WHITE}LITA{maincolor}] {maincolor}[{WHITE}{current_time}{maincolor}] {GREY} | {GREEN}[+]{maincolor} SUCCESS     {GREY} | {maincolor}{token[:30]}... {GREY}|{maincolor} 200{RESET}          ")
            elif response.status_code == 429:
                print(f"                        {maincolor}[{WHITE}LITA{maincolor}] {maincolor}[{WHITE}{current_time}{maincolor}] {GREY} | {YELLOW}[-]{maincolor} RATE LIMITED{GREY} | {maincolor}{token[:30]}... {GREY}|{maincolor} 429{RESET}          ")
            else:
                print(f"                        {maincolor}[{WHITE}LITA{maincolor}] {maincolor}[{WHITE}{current_time}{maincolor}] {GREY} | {RED}[-]{maincolor} FAILED      {GREY} | {maincolor}{token[:30]}... {GREY}|{maincolor} {response.status_code}{RESET}          ")
        except requests.exceptions.RequestException as e:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"                        {maincolor}[{WHITE}LITA{maincolor}] {maincolor}[{WHITE}{current_time}{maincolor}] {GREY} | {RED}[-]{maincolor} ERROR       {GREY} | {maincolor}{token[:30]}... {GREY}| {str(e)}{RESET}          ")

    threads = [Thread(target=process_token, args=(token, maincolor)) for token in tokens]

    for i in range(0, len(threads), 15):
        batch = threads[i:i + 15]
        for thread in batch:
            thread.start()
        for thread in batch:
            thread.join()

    input(f"                        {maincolor}[{WHITE}LITA{maincolor}] {WHITE}| {maincolor}[{WHITE}PRESS ENTER TO CONTINUE...{maincolor}] {WHITE}>{maincolor} ")
    os.system('cls')
