import webbrowser
import sys
import threading
import os
from colorama import Fore, Style, init
init()

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

            if not tokens:
                self.notokens = True
            else:
                self.notokens = False
            return tokens
        except FileNotFoundError:
            self.nofile = True
            return []

    def exit(self):
        sys.exit()

    def discord(self):
        webbrowser.open("https://discord.gg/R7ppWY83ak")
        os.system('cls')

    def website(self):
        webbrowser.open("https://getlita.xyz")
        os.system('cls')

    def run_task_in_thread(self, task):
        task_thread = threading.Thread(target=task)
        task_thread.start()
        task_thread.join()
        self.optionsascii([])

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
{theme_colors[2]}                                  
{theme_colors[3]}                                                                                                   
{theme_colors[4]}                                                                                                                                                                                                  
        
        print(ascii_art)

        if self.nofile:
            print("")
            print(fr"                        {Fore.RED}[{WHITE}LITA{Fore.RED}] {WHITE}| {Fore.RED}[{WHITE}'Input/Tokens.txt' Not Found!{Fore.RED}]{Fore.RED}")
        elif self.notokens:
            print("")
            print(f"                        {Fore.RED}[{WHITE}LITA{Fore.RED}] {WHITE}| {Fore.RED}[{WHITE}No Tokens Found in 'Input/Tokens.txt'{Fore.RED}]{Fore.RED}")

        options = fr"""                                                
                        {theme_colors[4]}[{WHITE}01{theme_colors[4]}] {WHITE}Channel Spammer    {theme_colors[4]}[{WHITE}04{theme_colors[4]}] {WHITE}Reply Spammer        {theme_colors[4]}[{WHITE}07{theme_colors[4]}] {WHITE}Reaction Bomber
                        {theme_colors[4]}[{WHITE}02{theme_colors[4]}] {WHITE}Name Switcher      {theme_colors[4]}[{WHITE}05{theme_colors[4]}] {WHITE}Pronouns Switcher    {theme_colors[4]}[{WHITE}08{theme_colors[4]}] {WHITE}Bio Switcher
                        {theme_colors[4]}[{WHITE}03{theme_colors[4]}] {WHITE}Token Checker      {theme_colors[4]}[{WHITE}06{theme_colors[4]}] {WHITE}Thread Bomber        {theme_colors[4]}[{WHITE}09{theme_colors[4]}] {WHITE}Theme Changer"""
        
        print(options)
