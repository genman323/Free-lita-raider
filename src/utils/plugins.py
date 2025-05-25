import webbrowser
import sys
import threading
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

WHITE = Fore.WHITE
RESET = Style.RESET_ALL


class Free:
    def __init__(self):
        self.nofile = False
        self.notokens = False
        self.tokens = self.load_tokens()

    def load_tokens(self):
        try:
            with open("input/tokens.txt", "r") as f:
                tokens = [token.strip() for token in f if token.strip()]
            self.notokens = not bool(tokens)
            return tokens
        except FileNotFoundError:
            self.nofile = True
            return []

    def exit(self):
        sys.exit()

    def discord(self):
        webbrowser.open("https://discord.gg/R7ppWY83ak")
        os.system('cls' if os.name == 'nt' else 'clear')

    def website(self):
        webbrowser.open("https://getlita.xyz")
        os.system('cls' if os.name == 'nt' else 'clear')

    def run_task_in_thread(self, task):
        task_thread = threading.Thread(target=task)
        task_thread.start()
        task_thread.join()
        self.optionsascii([])

    def format_option(self, code, label, color):
        return f"{color}[{WHITE}{code}{color}] {WHITE}{label}"

    def optionsascii(self, theme_colors):
        if not theme_colors or len(theme_colors) < 5:
            theme_colors = [
                "\033[38;2;75;0;140m",
                "\033[38;2;85;10;180m",
                "\033[38;2;95;20;220m",
                "\033[38;2;105;30;230m",
                "\033[38;2;115;40;240m"
            ]

        ascii_art = fr"""
{theme_colors[0]}                                                                                                   
{theme_colors[1]}                                              
{theme_colors[2]}               ░██████╗███████╗██████╗░███████╗███╗░░██╗██╗████████╗██╗░░░██╗
                                ██╔════╝██╔════╝██╔══██╗██╔════╝████╗░██║██║╚══██╔══╝╚██╗░██╔╝
                                ╚█████╗░█████╗░░██████╔╝█████╗░░██╔██╗██║██║░░░██║░░░░╚████╔╝░
                                ░╚═══██╗██╔══╝░░██╔══██╗██╔══╝░░██║╚████║██║░░░██║░░░░░╚██╔╝░░
                                ██████╔╝███████╗██║░░██║███████╗██║░╚███║██║░░░██║░░░░░░██║░░░
                                ╚═════╝░╚══════╝╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝╚═╝░░░╚═╝░░░░░░╚═╝░░░
{theme_colors[3]}                                                                                                   
{theme_colors[4]}                                                                                                                                                                                                  
"""
        print(ascii_art)

        if self.nofile:
            print()
            print(f"                        {Fore.RED}[{WHITE}LITA{Fore.RED}] {WHITE}| {Fore.RED}[{WHITE}'input/tokens.txt' Not Found!{Fore.RED}]{RESET}")
        elif self.notokens:
            print()
            print(f"                        {Fore.RED}[{WHITE}LITA{Fore.RED}] {WHITE}| {Fore.RED}[{WHITE}No Tokens Found in 'input/tokens.txt'{Fore.RED}]{RESET}")

        print("\n")
        options = f"""                                                
                        {self.format_option('01', 'Channel Spammer', theme_colors[4])}    {self.format_option('04', 'Reply Spammer', theme_colors[4])}        {self.format_option('07', 'Reaction Bomber', theme_colors[4])}
                        {self.format_option('02', 'Name Switcher', theme_colors[4])}      {self.format_option('05', 'Pronouns Switcher', theme_colors[4])}    {self.format_option('08', 'Bio Switcher', theme_colors[4])}
                        {self.format_option('03', 'Token Checker', theme_colors[4])}      {self.format_option('06', 'Thread Bomber', theme_colors[4])}        {self.format_option('09', 'Theme Changer', theme_colors[4])}
"""
        print(options)
