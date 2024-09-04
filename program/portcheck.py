import socket
from datetime import datetime
import threading
import os
from colorama import Fore, init

init()

# Imprimer le texte en rouge
print(Fore.RED + """
                                                   
  

                                                                               
██████╗  ██████╗ ██████╗ ████████╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██████╔╝██║   ██║██████╔╝   ██║       ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██╔═══╝ ██║   ██║██╔══██╗   ██║       ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║     ╚██████╔╝██║  ██║   ██║       ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝        ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                                                                                                                                                                                                                                               

                              PORT CHECKER
                                                       
""" + Fore.RESET)

def get_target():
    hostname = input(Fore.RED + "Enter your target hostname (or IP address) : " + Fore.RESET)
    target = socket.gethostbyname(hostname)
    print(Fore.RED + f'Scan Target  > {target}' + Fore.RESET)
    return target

def get_port_list():
    print(Fore.RED + 'Ports Range  > [1 – 1024]' + Fore.RESET)
    return range(1, 1024)

def scan_port(target, port):
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Test connection
        test = s.connect_ex((target, port))
        if test == 0:
            print(Fore.RED + f'Port {port} is [open]' + Fore.RESET)

def port_scanner():
    try:
        target = get_target()
        port_list = get_port_list()
        thread_list = list()
        start_time = datetime.now()

        for port in port_list:
            scan = threading.Thread(target=scan_port, args=(target, port))
            thread_list.append(scan)
            scan.daemon = True
            scan.start()

        for scan in thread_list:
            scan.join()
    except:
        print(Fore.RED + "Something went wrong !" + Fore.RESET)
    else:
        end_time = datetime.now()
        print(Fore.RED + "Scanning completed in", end_time - start_time + Fore.RESET)
        print(Fore.RED + "vous reviendrez au multitool dans 8 seconde." + Fore.RESET)
        import time
        time.sleep(8)
        os.system('cls')
        os.system('python Main.py')

if __name__ == '__main__':
    port_scanner()
