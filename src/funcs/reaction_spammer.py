import requests
from colorama import Fore, Style
from threading import Thread
import os
import datetime

PURPLE_1 = "\033[38;2;75;0;140m"
PURPLE_2 = "\033[38;2;85;10;180m"
PURPLE_3 = "\033[38;2;95;20;220m"
PURPLE_4 = "\033[38;2;105;30;230m"
PURPLE_5 = "\033[38;2;115;40;240m"
GREY = "\033[38;2;128;128;128m"
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
BLUE = Fore.BLUE
RED = Fore.RED
WHITE = Fore.WHITE
RESET = Style.RESET_ALL

def reaction_spammer(tokens, maincolor):
    channel_id = input(f"                        {maincolor}[{WHITE}LITA{maincolor}] {WHITE}| {maincolor}[{WHITE}CHANNEL ID{maincolor}] {WHITE}>{maincolor} ")
    message_id = input(f"                        {maincolor}[{WHITE}LITA{maincolor}] {WHITE}| {maincolor}[{WHITE}MESSAGE ID{maincolor}] {WHITE}>{maincolor} ")
    emoji = input(f"                        {maincolor}[{WHITE}LITA{maincolor}] {WHITE}| {maincolor}[{WHITE}EMOJI{maincolor}] {WHITE}>{maincolor} ")

    def add_reaction(token, maincolor):
        url = f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me'
        headers = {
            'Authorization': token
        }

        try:
            response = requests.put(url, headers=headers)
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            if response.status_code == 204:
                    print(f"                        {maincolor}[{WHITE}LITA{maincolor}] {maincolor}[{WHITE}{current_time}{maincolor}] {GREY} | {GREEN}[+]{maincolor} SUCCESS     {GREY} | {maincolor}{token[:30]}... {GREY}|{maincolor} 200{RESET}          ")
            elif response.status_code == 429:
                print(f"                        {maincolor}[{WHITE}LITA{maincolor}] {maincolor}[{WHITE}{current_time}{maincolor}] {GREY} | {YELLOW}[-]{maincolor} RATE LIMITED{GREY} | {maincolor}{token[:30]}... {GREY}|{maincolor} 429{RESET}          ")
            else:
                print(f"                        {maincolor}[{WHITE}LITA{maincolor}] {maincolor}[{WHITE}{current_time}{maincolor}] {GREY} | {RED}[-]{maincolor} FAILED      {GREY} | {maincolor}{token[:30]}... {GREY}|{maincolor} {response.status_code}{RESET}          ")
        except requests.exceptions.RequestException as e:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"                        {maincolor}[{WHITE}LITA{maincolor}] {maincolor}[{WHITE}{current_time}{maincolor}] {GREY} | {RED}[-]{maincolor} ERROR       {GREY} | {maincolor}{token[:30]}... {GREY}| {str(e)}{RESET}          ")

    threads = [Thread(target=add_reaction, args=(token, maincolor)) for token in tokens]

    for i in range(0, len(threads), 15):
        batch = threads[i:i + 15]

        for thread in batch:
            thread.start()

        for thread in batch:
            thread.join()

    input(f"                        {maincolor}[{WHITE}LITA{maincolor}] {WHITE}| {maincolor}[{WHITE}PRESS ENTER TO CONTINUE...{maincolor}] {WHITE}>{maincolor} ")
    os.system('cls')
