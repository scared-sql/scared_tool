import os
import colorama
import subprocess
import webbrowser
import fade
from colorama import Fore, init

init(autoreset=True)

ascii_art = """                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
   ▄████████  ▄████████    ▄████████    ▄████████    ▄████████ ████████▄  
  ███    ███ ███    ███   ███    ███   ███    ███   ███    ███ ███   ▀███ 
  ███    █▀  ███    █▀    ███    ███   ███    ███   ███    █▀  ███    ███ 
  ███        ███          ███    ███  ▄███▄▄▄▄██▀  ▄███▄▄▄     ███    ███ 
▀███████████ ███        ▀███████████ ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     ███    ███ 
         ███ ███    █▄    ███    ███ ▀███████████   ███    █▄  ███    ███ 
   ▄█    ███ ███    ███   ███    ███   ███    ███   ███    ███ ███   ▄███ 
 ▄████████▀  ████████▀    ███    █▀    ███    ███   ██████████ ████████▀  
                                       ███    ███                                
│━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━│
│[01] -> Proxy Scrapper                 │ [14] -> FIvem Scrapper         │
│[02] -> Python obfuscator              │ [15] -> Discord Id Info        │
│[03] -> discord id to first part token │ [16] -> Join the discord       │
│[04] -> Ip Tools                       │ [17] -> Download Database      │
│[05] -> Ip Pinger                      │ [18] -> Webh Spam              │ 
│[06] -> Webhooks tools                 │ [19] -> encrypter              │
│[07] -> Nitro Generator                │ [20] -> pc Info                │
│[08] -> Snusbase Search Tools          │ [21] -> temp mail              │
│[09] -> username tracker (osint)       │ [22] -> raid Bot               │
│[10] -> Osint Sites                    │ [23] -> linkvertise Bypasser   │
│[11] -> Dos Tools                      │ [24] -> account Disabler       │
│[12] -> Ip Port Scanner                │        MOOR SOON               │
│[13] -> Database Searcher              │                                │  
│━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━│                                                                     
"""

root = (Fore.RED + """
┌──(User@root)-[~Menu]│
└─$>""" + Fore.RED)

ascii_art = Fore.RED + ascii_art
print(ascii_art)

choice = input(root)
if "01" in choice.lower():
    os.system("python checker.py")

def options():
    commandes = [str(i) for i in range(1, 16)]

while True:
    gg = choice
    if gg.isdigit():
        gg = int(gg)

    if gg == 1:
        subprocess.run(['python', 'program\\checker.py'])
    elif gg == 2:
        subprocess.run(['python', 'program\\obfuscator.py'])
    elif gg == 3:
        subprocess.run(['python', 'program\\idtotoken.py'])
    elif gg == 4:
        subprocess.run(['python', 'program\\ipinfo.py'])
    elif gg == 5:
        subprocess.run(['python', 'program\\ippinger.py'])
    elif gg == 6:
        subprocess.run(['python', 'program\\webhooktool.py'])
    elif gg == 7:
        subprocess.run(['python', 'program\\nitrogen.py'])
    elif gg == 8:
        subprocess.run(['python', 'program\\snustool.py'])
    elif gg == 9:
        subprocess.run(['python', 'program\\usernametracker.py'])
    elif gg == 10:
        subprocess.run(['python', 'program\\osintsites.py'])
    elif gg == 11:
        subprocess.run(['python', 'program\\ddos.py'])
    elif gg == 12:
        subprocess.run(['python', 'program\\portcheck.py'])
    elif gg == 13:
        subprocess.run(['python', 'output\\dbsearcher.py'])
    elif gg == 14:
        subprocess.run(['python', 'FivemScrapper\\main.py'])
    elif gg == 15:
        subprocess.run(['python', 'program\\idinfo.py'])
    elif gg == 16:
        webbrowser.open('https://discord.gg/freeforreal')
        os.system('cls')
        os.system('python Main.py')
    elif gg == 17:
        subprocess.run(['python', 'program\\database.py'])
    elif gg == 18:
        subprocess.run(['python', 'program\\webhspam.py'])
    elif gg == 19:
        subprocess.run(['python', 'program\\encrypter.py'])
    elif gg == 20:
        subprocess.run(['python', 'program\\pc_info.py'])
    elif gg == 21:
        subprocess.run(['python', 'program\\temp_mail.py'])   
    elif gg == 22:
        subprocess.run(['python', 'program\\Raid_bot.py'])
    elif gg == 23:
        subprocess.run(['python', 'program\\linkvertise_bypasser.py'])
    elif gg == 24:
        subprocess.run(['python', 'program\\accountdisabler.py'])
    else:
        print('Mauvais choix...')
        os.system('cls')
        os.system('python Main.py')
