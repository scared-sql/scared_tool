import os
import base64
from colorama import Fore, init

init()

banner = (Fore.RED + """
████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗
╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║
   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║
   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║
   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝
                                            
""" + Fore.LIGHTCYAN_EX)

print(banner)

userid = input(Fore.WHITE + " [INPUT] id discord : ")

encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")

print(Fore.RED + f'\n [LOGS] moitié du token : {encodedStr}')
print(" vous reviendrez sur main.py dans 4 seconde")

import time
time.sleep(4)

os.system('cls' if os.name == 'nt' else 'clear')
os.system("python Main.py")