import requests
import os
import base64
from colorama import Fore, Style, init

init()

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class Color:
    RED = Fore.RED + Style.BRIGHT
    WHITE = Fore.WHITE + Style.BRIGHT
    RESET = Fore.RESET + Style.RESET_ALL

ASCII_ART = r"""
                   ███████╗███╗   ██╗██╗   ██╗███████╗██████╗  █████╗ ███████╗███████╗
                   ██╔════╝████╗  ██║██║   ██║██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝
                   ███████╗██╔██╗ ██║██║   ██║███████╗██████╔╝███████║███████╗█████╗  
                   ╚════██║██║╚██╗██║██║   ██║╚════██║██╔══██╗██╔══██║╚════██║██╔══╝  
                   ███████║██║ ╚████║╚██████╔╝███████║██████╔╝██║  ██║███████║███████╗
                   ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝
                                                                                                                  


                                     ╔═══════════════════════════╗
                                     ║      Snusbase Tool        ║
                                     ║        by scared          ║
                                     ╚═══════════════════════════╝


      ════════════════════════════════════════════════════════════════════════════════════════════════  
         [1] -> Search une email                  ║  [4] -> Search un mot de passe
         [2] -> Search un pseudo                  ║  [5] -> Search un mot de passe hasher
         [3] -> Search un prenom nom              ║  [6] -> Search une adresse ip 
    ═════════════════════════════════════════════════════════════════════════════════════════════════════
                            ║                                            ║
                            ╚════════════════════════════════════════════╝ 
"""

SEARCH_TYPES = ["email", "username", "name", "password", "hash", "lastip"]

def search(search_input, search_type):
    if not search_input:
        print(f"{Color.RED}[!] Please enter a search term{Color.RESET}")
        return

    key = 'c2J5anRoa29mdDR5YWltYndjanFwbXhzOGh1b3Zk'

    mensaje_base64_bytes = key.encode('utf-8')
    mensaje_decodificado_bytes = base64.b64decode(mensaje_base64_bytes)
    apiKey = mensaje_decodificado_bytes.decode('utf-8')

    url = 'https://api-experimental.snusbase.com/data/search'
    headers = {
        'Auth': apiKey,
        'Content-Type': 'application/json'
    }
    payload = {
        'terms': [search_input],
        'types': [search_type],
        'wildcard': False
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        display_results(response.json().get('results', {}))
    else:
        print(f"{Color.RED}Error: {response.text}{Color.RESET}")

def display_results(results):
    if not results:
        print(f"{Color.RED}\n[+] No results found in the DB{Color.RESET}")
    else:
        for database, entries in results.items():
            for entry in entries:
                for key, value in entry.items():
                    if key == 'lastip':
                        print(f"{Color.WHITE}[+] {key}: {value} (Get Location){Color.RESET}")
                    else:
                        print(f"[+] {Color.WHITE}{key}: {value}{Color.RESET}")
                print('-' * 50)

def get_location(ip):
    url = f'http://ip-api.com/json/{ip}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"{Color.WHITE}[+] Location for IP {ip}: {data['city']}, {data['region']}, {data['country']}{Color.RESET}")
    else:
        print(f"{Color.RED}[!] Error: {response.text}{Color.RESET}")

def main():
    clear()
    title = f"{Color.RED}{ASCII_ART}[+] SnusBase Search Engine{Color.RESET}"
    print(title)
    
    search_type_choice = int(input(f"{Color.WHITE}[+] Enter the number corresponding to the search type: {Color.RESET}"))
    search_type = SEARCH_TYPES[search_type_choice - 1]

    search_input = input(f"{Color.WHITE}[+] Enter search term: {Color.RESET}")

    search(search_input, search_type)

    while True:
        ip = input(f"{Color.RED}[+] Enter IP to get location or '7' to return to menu: {Color.RESET}")
        if ip.lower() == '7':
            print(f"{Color.RESET}")
            os.system('cls')
            os.system('python Main.py')
            break
        get_location(ip)
        
if __name__ == "__main__":
    main()
