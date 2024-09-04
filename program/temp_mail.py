import webbrowser
import os
from colorama import Fore, Style, init

init()

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_red(text):
    print(f"{Fore.RED}{text}{Style.RESET_ALL}")

# Clear the screen and set color for Windows
clear_screen()
os.system("color d")

print_red("""
▄▄▄█████▓   ▓█████     ███▄ ▄███▓    ██▓███      ███▄ ▄███▓    ▄▄▄          ██▓    ██▓       
▓  ██▒ ▓▒   ▓█   ▀    ▓██▒▀█▀ ██▒   ▓██░  ██▒   ▓██▒▀█▀ ██▒   ▒████▄       ▓██▒   ▓██▒       
▒ ▓██░ ▒░   ▒███      ▓██    ▓██░   ▓██░ ██▓▒   ▓██    ▓██░   ▒██  ▀█▄     ▒██▒   ▒██░       
░ ▓██▓ ░    ▒▓█  ▄    ▒██    ▒██    ▒██▄█▓▒ ▒   ▒██    ▒██    ░██▄▄▄▄██    ░██░   ▒██░       
  ▒██▒ ░    ░▒████▒   ▒██▒   ░██▒   ▒██▒ ░  ░   ▒██▒   ░██▒    ▓█   ▓██▒   ░██░   ░██████▒   
  ▒ ░░      ░░ ▒░ ░   ░ ▒░   ░  ░   ▒▓▒░ ░  ░   ░ ▒░   ░  ░    ▒▒   ▓▒█░   ░▓     ░ ▒░▓  ░   
    ░        ░ ░  ░   ░  ░      ░   ░▒ ░        ░  ░      ░     ▒   ▒▒ ░    ▒ ░   ░ ░ ▒  ░   
  ░            ░      ░      ░      ░░          ░      ░        ░   ▒       ▒ ░     ░ ░      
               ░  ░          ░                         ░            ░  ░    ░         ░  ░   
""")

url = "https://temp-mail.org/fr/"
webbrowser.open(url)

print_red("""
[1] Back to menu
""")

choice = int(input(f'{Fore.MAGENTA}[+] Choose >> {Style.RESET_ALL}'))

def execute_script(choice):
    if choice == 1:
        os.system('python main.py')

execute_script(choice)
