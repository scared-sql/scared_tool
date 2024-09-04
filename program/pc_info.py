import re
import socket
import uuid
import subprocess
import platform
import os

from colorama import Fore, init

init()

os.system('color D')
os.system('cls' if os.name == 'nt' else 'clear')

print(Fore.RED + f"""
                    ██▓███   ▄████▄      ██▓ ███▄    █   █████▒▒█████  
                    ▓██░  ██▒▒██▀ ▀█     ▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒
                    ▓██░ ██▓▒▒▓█    ▄    ▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒
                    ▒██▄█▓▒ ▒▒▓▓▄ ▄██▒   ░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░
                    ▒██▒ ░  ░▒ ▓███▀ ░   ░██░▒██░   ▓██░░▒█░   ░ ████▓▒░
                    ▒▓▒░ ░  ░░ ░▒ ▒  ░   ░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░ 
                    ░▒ ░       ░  ▒       ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░ 
                    ░░       ░            ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒  
                             ░ ░          ░           ░            ░ ░  

""" + Fore.RESET)

class PCInfo:
    def __init__(self):
        self.IP = input(Fore.RED + "Entrez l'adresse IP de votre cible >>> " + Fore.RESET)
        while not self.validate_ip(self.IP):
            print(Fore.RED + "Adresse IP invalide. Veuillez réessayer." + Fore.RESET)
            self.IP = input(Fore.RED + "Entrez l'adresse IP de votre cible : " + Fore.RESET)

    def validate_ip(self, ip):
        pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        return pattern.match(ip) is not None

    def get_username(self):
        return os.getenv("USERNAME") or os.getenv("USER")

    def get_pc_name(self):
        return socket.gethostname()

    def get_mac_address(self):
        mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        return mac

    def get_ip_addresses(self):
        ipv4 = socket.gethostbyname(socket.gethostname())
        ipv6 = socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET6)
        ipv6 = [addr[4][0] for addr in ipv6 if addr[1] == socket.SOCK_STREAM]
        return ipv4, ipv6[0] if ipv6 else None

    def get_uuid(self):
        if platform.system() == "Windows":
            command = "wmic csproduct get uuid"
            uuid_str = subprocess.check_output(command, shell=True).decode().split("\n")[1].strip()
        else:
            uuid_str = subprocess.check_output('cat /proc/sys/kernel/random/uuid', shell=True).decode().strip()
        return uuid_str

    def display_info(self):
        print(Fore.RED + f"Nom d'utilisateur : {self.get_username()}" + Fore.RESET)
        print(Fore.RED + f"Nom du PC : {self.get_pc_name()}" + Fore.RESET)
        print(Fore.RED + f"Adresse MAC : {self.get_mac_address()}" + Fore.RESET)
        ipv4, ipv6 = self.get_ip_addresses()
        print(Fore.RED + f"Adresse IPv4 : {ipv4}" + Fore.RESET)
        print(Fore.RED + f"Adresse IPv6 : {ipv6}" + Fore.RESET)
        print(Fore.RED + f"UUID du PC : {self.get_uuid()}" + Fore.RESET)
        print(Fore.RED + """
        [1] back to menu
        """ + Fore.RESET)
        choice = int(input(Fore.RED + '\033[0;35m Choose >>> ' + Fore.RESET))
        def execute_script(choice):
            if choice == 1:
                os.system('python main.py')
            elif choice == 2:
                os.system('python whois_lookup.py')

        execute_script(choice)

if __name__ == "__main__":
    pc = PCInfo()
    pc.display_info()
