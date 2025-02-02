import subprocess
import sys

def ensure_imports():
    required_modules = [
        "webbrowser", 
        "sys", 
        "threading", 
        "os", 
        "colorama", 
        "time", 
        "json", 
        "random", 
        "requests", 
        "datetime"
    ]
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])

ensure_imports()

import os
import json
from src.utils.init import *
from src.utils.plugins import Free
from src.funcs.check_token import main as check_token_main

class Raider:
    THEME_FILE = "lita_theme.json"

    def __init__(self):
        os.system('cls')
        self.Free = Free()
        self.tokens = self.Free.tokens
        self.theme_colors = self.load_theme_colors()
        self.maincolor = self.theme_colors[4]

    def load_theme_colors(self):
        if os.path.exists(self.THEME_FILE):
            with open(self.THEME_FILE, 'r') as file:
                data = json.load(file)
                theme = data.get("theme", "purple")
                return self.get_theme_colors(theme)
        else:
            return self.get_theme_colors("purple")

    def save_theme(self, theme):
        input(f"                        {self.maincolor}[{WHITE}LITA{self.maincolor}] {WHITE}| {self.maincolor}[{WHITE}PRESS ENTER TO CONTINUE...{self.maincolor}] {WHITE}>{self.maincolor} ")
        with open(self.THEME_FILE, 'w') as file:
            json.dump({"theme": theme}, file, indent=4)
        self.theme_colors = self.get_theme_colors(theme)
        self.maincolor = self.theme_colors[4]
        os.system('cls')

    def get_theme_colors(self, theme):
        colors = {
        "blood": [f"\033[38;2;75;0;0m", f"\033[38;2;85;10;10m", f"\033[38;2;95;20;20m", f"\033[38;2;105;30;30m", f"\033[38;2;115;40;40m"],
        "forest": [f"\033[38;2;0;65;0m", f"\033[38;2;10;75;10m", f"\033[38;2;20;85;20m", f"\033[38;2;30;95;30m", f"\033[38;2;40;105;40m"],
        "midnight": [f"\033[38;2;0;0;75m", f"\033[38;2;10;10;85m", f"\033[38;2;20;20;95m", f"\033[38;2;30;30;105m", f"\033[38;2;40;40;115m"],
        "violet": [f"\033[38;2;75;0;140m", f"\033[38;2;85;10;180m", f"\033[38;2;95;20;220m", f"\033[38;2;105;30;230m", f"\033[38;2;115;40;240m"],
        "ocean": [f"\033[38;2;0;128;255m", f"\033[38;2;30;144;255m", f"\033[38;2;70;164;255m", f"\033[38;2;100;184;255m", f"\033[38;2;130;204;255m"],
        "peach": [f"\033[38;2;255;127;80m", f"\033[38;2;255;135;90m", f"\033[38;2;255;145;100m", f"\033[38;2;255;155;110m", f"\033[38;2;255;165;120m"],
        "lime": [f"\033[38;2;50;205;50m", f"\033[38;2;60;215;60m", f"\033[38;2;70;225;70m", f"\033[38;2;80;235;80m", f"\033[38;2;90;245;90m"],
    }
        return colors.get(theme, colors["violet"])

    def theme_changer(self):
        print("")
        theme = input(f"                        {self.maincolor}[{WHITE}LITA{self.maincolor}] {WHITE}| {self.maincolor}[{WHITE}violet, midnight, blood, forest, lime, ocean, peach{self.maincolor}] {WHITE}>{self.maincolor} ").strip().lower()
        if theme in ["violet", "midnight", "blood", "forest", "lime", "ocean", "peach"]:
            self.save_theme(theme)
        else:
            print(f"                        {self.maincolor}[{WHITE}LITA{self.maincolor}] {WHITE}| {self.maincolor}[{WHITE}INVALID OPTION{self.maincolor}]")
            input(f"                        {self.maincolor}[{WHITE}LITA{self.maincolor}] {WHITE}| {self.maincolor}[{WHITE}PRESS ENTER TO CONTINUE...{self.maincolor}] {WHITE}>{self.maincolor} ")
            os.system('cls')

    def main(self):
        while True:
            self.Free.optionsascii(self.theme_colors)
            userinput = input(f"                        {self.maincolor}[{WHITE}LITA{self.maincolor}] {WHITE}| {self.maincolor}[{WHITE}INPUT{self.maincolor}] {WHITE}>{self.maincolor} ")
            
            options = {
                "1": lambda: channel_spammer(self.tokens, self.maincolor),
                "01": lambda: channel_spammer(self.tokens, self.maincolor),
                "2": lambda: name_switcher(self.tokens, self.maincolor),
                "02": lambda: name_switcher(self.tokens, self.maincolor),
                "3": lambda: check_token_main(self.tokens, self.maincolor),
                "03": lambda: check_token_main(self.tokens, self.maincolor),
                "4": lambda: reply_spammer(self.tokens, self.maincolor),
                "04": lambda: reply_spammer(self.tokens, self.maincolor),
                "5": lambda: pron_switcher(self.tokens, self.maincolor),
                "05": lambda: pron_switcher(self.tokens, self.maincolor),
                "6": lambda: thread_spammer(self.tokens, self.maincolor),
                "06": lambda: thread_spammer(self.tokens, self.maincolor),
                "7": lambda: reaction_spammer(self.tokens, self.maincolor),
                "07": lambda: reaction_spammer(self.tokens, self.maincolor),
                "8": lambda: bio_switcher(self.tokens, self.maincolor),
                "08": lambda: bio_switcher(self.tokens, self.maincolor),
                "9": self.theme_changer,
                "09": self.theme_changer,
                "X": self.Free.exit,
                "x": self.Free.exit,
                "?": self.Free.discord,
                "#": self.Free.website,
            }

            if userinput in options:
                options[userinput]()
            else:
                print("")
                print(f"                        {self.maincolor}[{WHITE}LITA{self.maincolor}] {WHITE}| {self.maincolor}[{WHITE}INVALID OPTION{self.maincolor}]")
                input(f"                        {self.maincolor}[{WHITE}LITA{self.maincolor}] {WHITE}| {self.maincolor}[{WHITE}PRESS ENTER TO CONTINUE...{self.maincolor}] {WHITE}>{self.maincolor} ")
                os.system('cls')

if __name__ == "__main__":
    raider = Raider()
    raider.main()
