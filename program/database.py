import os
import webbrowser
import subprocess
import fade

database_all = """
# <!DOCTYPE html>
# <html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Texte en Rouge</title>
    <style>
        .red-text {
            color: red;
            font-family: monospace;
            white-space: pre-wrap; /* Conserve les espaces et les retours à la ligne */
        }
    </style>
</head>
<body>
    <pre class="red-text">







































































    






























    
██████╗  █████╗ ████████╗ █████╗ ██████╗  █████╗ ███████╗███████╗
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
██║  ██║███████║   ██║   ███████║██████╔╝███████║███████╗█████╗  cela vous amenera vers votre naviguateur
██║  ██║██╔══██║   ██║   ██╔══██║██╔══██╗██╔══██║╚════██║██╔══╝  
██████╔╝██║  ██║   ██║   ██║  ██║██████╔╝██║  ██║███████║███████╗
╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝
│━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━│
│[01] -> Credit                         │
│[02] -> NazApi                         │ 
│[03] -> Fivem (2024)                   │ 
│[04] -> Minecraft                      │       
│[05] -> Discord                        │                                
│[06] -> Fbi                            │                                
│[07] -> paypal                         │                                
│[08] -> Snapchat                       │                                
│[09] -> Gmod                           │                               
│[10] -> Valorant                       │                                
│[11] -> Orange                         │                                
│[12] -> Instagram                      │                            
│[13] -> Doxbin                         │       
│[14] -> Retourner Au Multitool         │
│━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━│



"""

database_all = fade.pinkred(database_all)

def main():
    print(database_all)
    choice = input("entrée votre choix : ").strip()

    if choice.isdigit():
        choice = int(choice)

        if choice == 1:
            subprocess.run(['python', 'program\\credit.py'])

        elif choice == 2:
            webbrowser.open('https://mega.nz/file/trFkXIAY#sUM3Fi0L9QkshiY0uKc_nhUIkbyJ58qix3OaqcZjSlI')
            os.system('cls')
            os.system('python Main.py')

        elif choice == 3:
            webbrowser.open('https://gofile.io/d/a6c9dc16-e3df-4f05-a5b0-32be55612468')
            os.system('cls')
            os.system('python Main.py')

        elif choice == 4:
            webbrowser.open('https://gofile.io/d/EggYGD')
            os.system('cls')
            os.system('python Main.py')

        elif choice == 5:
            webbrowser.open('https://gofile.io/d/rXKCqi')
            os.system('cls')
            os.system('python Main.py')

        elif choice == 6:
            webbrowser.open('https://gofile.io/d/be14eafa-19b9-479b-9f23-bef63df37b1d')
            os.system('cls')
            os.system('python Main.py')

        elif choice == 7:
            webbrowser.open('https://gofile.io/d/c370dd37-c6d1-4e26-b2b6-619abeb28141')
            os.system('cls')
            os.system('python Main.py')

        elif choice == 8:
            webbrowser.open('https://gofile.io/d/QzYzDt')
            os.system('cls')
            os.system('python Main.py')

        elif choice == 9:
            webbrowser.open('https://mega.nz/folder/gT0R3SzA#kK1GkNUvnEo4XYwRjbdiIg/folder/AP1wnSRK')
            os.system('cls')
            os.system('python Main.py')

        elif choice == 10:
            webbrowser.open('https://gofile.io/d/b390578a-b8bd-4c57-b5d8-1893133e405d')
            os.system('cls')
            os.system('python Main.py')

        elif choice == 11:
            webbrowser.open('https://gofile.io/d/8f16421b-ca85-44ad-b436-8934ce47aaff')
            os.system('cls')
            os.system('python Main.py')

        elif choice == 12:
            webbrowser.open('https://gofile.io/d/cpVHO3')
            os.system('cls')
            os.system('python Main.py')

        elif choice == 13:
            webbrowser.open('https://gofile.io/d/jQQkKW')
            os.system('cls')
            os.system('python Main.py')

        elif choice == 14:
            os.system('cls')
            os.system('python Main.py')

        else:
            print('error')
            os.system('cls')
            os.system('python database.py')
    else:
        print('Invalid input. Please enter a number between 1 and 14.')
        os.system('cls')
        os.system('python Main.py')

if __name__ == "__main__":
    main()
