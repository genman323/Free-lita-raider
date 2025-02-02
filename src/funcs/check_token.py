import requests
import threading
from colorama import Fore, Style
import datetime
import os

YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
RED = Fore.RED
WHITE = Fore.WHITE
GREY = Fore.LIGHTBLACK_EX
RESET = Style.RESET_ALL

url = "https://discord.com/api/v9/users/@me/library"
valid_tokens = []
lock = threading.Lock()

def check_token(token, maincolor):
    headers = {
        "Authorization": token
    }
    try:
        response = requests.get(url, headers=headers)
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

def process_batch(tokens, maincolor):
    for token in tokens:
        check_token(token, maincolor)

def main(tokens, maincolor):
    if not tokens:
        print(f"                        {RED}[{WHITE}LITA{RED}] {WHITE}| {RED}[{WHITE}No Tokens Found in 'Input/Tokens.txt'{RED}]{RESET}")
        input(f"                        {maincolor}[{WHITE}LITA{maincolor}] {WHITE}| {maincolor}[{WHITE}PRESS ENTER TO CONTINUE...{maincolor}] {WHITE}>{maincolor} ")
        os.system('cls')
        return

    threads = []
    for i in range(0, len(tokens), 15):
        token_batch = tokens[i:i + 15]
        thread = threading.Thread(target=process_batch, args=(token_batch, maincolor))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "tokens.txt")

    with open(output_file, "w") as f:
        f.write("          ".join(valid_tokens))
    print(f"\n                        {GREEN}[+]{maincolor} Valid tokens saved to output/tokens.txt{RESET}")

    input(f"                        {maincolor}[{WHITE}LITA{maincolor}] {WHITE}| {maincolor}[{WHITE}PRESS ENTER TO CONTINUE...{maincolor}] {WHITE}>{maincolor} ")
    os.system('cls')

if __name__ == "__main__":
    input_file = "Input/Tokens.txt"
    main_color = Fore.MAGENTA

    if os.path.exists(input_file):
        with open(input_file, "r") as file:
            tokens = [line.strip() for line in file if line.strip()]
    else:
        tokens = []
