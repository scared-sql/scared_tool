import os
import colorama
import threading
import requests
import sys
from colorama import Fore

colorama.init()

os.system('cls')

print(Fore.RED)

def dos(target):
    while True:
        try:
            res = requests.get(target)
            print("Request sent!")
        except requests.exceptions.ConnectionError:
            print("[!!!] " + "Connexion interrompue!")

threads = 20

print(Fore.RED + """
██╗██████╗     ██████╗ ██╗███╗   ██╗ ██████╗ ███████╗██████╗ 
██║██╔══██╗    ██╔══██╗██║████╗  ██║██╔════╝ ██╔════╝██╔══██╗
██║██████╔╝    ██████╔╝██║██╔██╗ ██║██║  ███╗█████╗  ██████╔╝
██║██╔═══╝     ██╔═══╝ ██║██║╚██╗██║██║   ██║██╔══╝  ██╔══██╗
██║██║         ██║     ██║██║ ╚████║╚██████╔╝███████╗██║  ██║
╚═╝╚═╝         ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                             
           """)

print('-' * 60)

print(Fore.RED + 'ip pinger')

print('-' * 60)

ip_to_check = input(Fore.RED + 'Veuillez mettre une adresse IP à ping : ')

print('-' * 60)
os.system('ping -n 5 {}'.format(ip_to_check))
print('-' * 60)

import time
time.sleep(4)
os.system('cls')
os.system("python Main.py")
print(Fore.RED + "vous serez rediriger vers le multi tools dans 3 seconde")
