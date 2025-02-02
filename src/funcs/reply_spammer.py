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
 
def reply_spammer(tokens, maincolor):

    channel_id = input(f"                        {maincolor}[{WHITE}LITA{maincolor}] {WHITE}| {maincolor}[{WHITE}CHANNEL ID{maincolor}] {WHITE}>{maincolor} ")

    message = input(f"                        {maincolor}[{WHITE}LITA{maincolor}] {WHITE}| {maincolor}[{WHITE}MESSAGE{maincolor}] {WHITE}>{maincolor} ")

    message_id = input(f"                        {maincolor}[{WHITE}LITA{maincolor}] {WHITE}| {maincolor}[{WHITE}MESSAGE ID{maincolor}] {WHITE}>{maincolor} ")

    amount = int(input(f"                        {maincolor}[{WHITE}LITA{maincolor}] {WHITE}| {maincolor}[{WHITE}AMOUNT PER TOKEN{maincolor}] {WHITE}>{maincolor} "))

    thread_count = int(input(f"                        {maincolor}[{WHITE}LITA{maincolor}] {WHITE}| {maincolor}[{WHITE}THREADS{maincolor}] {WHITE}>{maincolor} "))

    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
    data = {
        'content': message,
        'message_reference': {
            'message_id': message_id
        }
    }

    def send_message(token, maincolor):
        headers = {
            'Authorization': token
        }
        for _ in range(amount):
            try:
                response = requests.post(url, headers=headers, json=data)
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

    threads = []
    for token in tokens:
        thread = Thread(target=send_message, args=(token, maincolor))
        threads.append(thread)

    for i in range(0, len(threads), thread_count):
        batch = threads[i:i + thread_count]

        for thread in batch:
            thread.start()

        for thread in batch:
            thread.join()

    input(f"                        {maincolor}[{WHITE}LITA{maincolor}] {WHITE}| {maincolor}[{WHITE}PRESS ENTER TO CONTINUE...{maincolor}] {WHITE}>{maincolor} ")
    os.system('cls')
