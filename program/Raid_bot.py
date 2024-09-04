# par pitié ne pas volé mon code et ne rien modiffié svp sah
import discord
import asyncio
from colorama import Fore


ascii_art = """
██████╗  █████╗ ██╗██████╗ 
██╔══██╗██╔══██╗██║██╔══██╗
██████╔╝███████║██║██║  ██║
██╔══██╗██╔══██║██║██║  ██║
██║  ██║██║  ██║██║██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═════╝ 
"""

async def verify_token(token):

    print(Fore.BLUE + "[Debug] Initialisation du client Discord...")
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    try:
        print(Fore.BLUE + "[Debug] Tentative de connexion avec le token...")
        await client.login(token)  
        await client.close()
        print(Fore.GREEN + "[Debug] Connexion réussie, fermeture du client...")
        return True, None
    except discord.errors.LoginFailure:
        print(Fore.RED + "Token invalide.")
        return False, "Token invalide."
    except discord.errors.PrivilegedIntentsRequired:
        print(Fore.RED + "Le bot manque d'intents requis.")
        return False, "Le bot manque d'intents requis."
    except Exception as e:
        print(Fore.RED + f"Erreur lors de la connexion : {e}")
        return False, str(e)
    finally:
        if client.is_closed() is False:
            print(Fore.YELLOW + "[Debug] Forcer la fermeture du client Discord...")
            await client.close()

async def select_guild(client):
    print(Fore.CYAN + "[*] Serveurs disponibles :")
    for index, guild in enumerate(client.guilds, start=1):
        print(Fore.WHITE + f"{index}. {guild.name} (ID: {guild.id})")

    while True:
        try:
            choice = int(input(Fore.WHITE + "[?] Sélectionnez le numéro du serveur : "))
            if 1 <= choice <= len(client.guilds):
                return client.guilds[choice - 1]
            else:
                print(Fore.RED + "Numéro invalide, veuillez réessayer.")
        except ValueError:
            print(Fore.RED + "Veuillez entrer un numéro valide.")

async def run():
    token = input(Fore.WHITE + "Entrez le token du bot Discord : ")

    # Vérification du token
    print(Fore.BLUE + "[&] Vérification du token...")
    is_valid, error_message = await verify_token(token)

    if is_valid:
        print(Fore.GREEN + "[+] Token valide !")
        client = discord.Client(intents=discord.Intents.default())

        @client.event
        async def on_ready():
            print(Fore.GREEN + ascii_art)
            print(Fore.WHITE + f"> Status : En ligne")
            print(Fore.WHITE + f"> Nom du bot Discord : {client.user.name}")
            print(Fore.WHITE + f"> Sur {len(client.guilds)} serveur(s)")


            await client.change_presence(activity=discord.Game(name="By Roner tools"))


            guild = await select_guild(client)

            print(Fore.CYAN + f"[*] Serveur sélectionné : {guild.name}")
            print(Fore.CYAN + "Commandes disponibles :")
            print(Fore.CYAN + "  nuke - Supprimer tous les channels du serveur")
            print(Fore.CYAN + "  create [nombre] [nom du channel] - Créer des channels")
            print(Fore.CYAN + "  spam [message] - Envoyer un message dans tous les channels")
            print(Fore.CYAN + "  dmall [message] - Bientôt disponible pour la v2")
            print(Fore.CYAN + "  stop - Déconnecter le bot")

            while True:
                command = input(Fore.WHITE + "> Commande : ").strip()
                if command.startswith("nuke"):
                    for channel in guild.channels:
                        try:
                            await channel.delete()
                            print(Fore.RED + f"[-] Channel supprimé : {channel.name}")
                        except Exception as e:
                            print(Fore.RED + f"Erreur lors de la suppression du channel {channel.name} : {e}")
                elif command.startswith("create"):
                    try:
                        _, count, channel_name = command.split(maxsplit=2)
                        count = int(count)
                        for i in range(1, count + 1):
                            full_channel_name = f"{channel_name}-{i}"
                            await guild.create_text_channel(full_channel_name)
                            print(Fore.GREEN + f"[+] Channel créé : {full_channel_name}")
                    except Exception as e:
                        print(Fore.RED + f"Erreur lors de la création des channels : {e}")
                elif command.startswith("spam"):
                    message = ' '.join(command.split()[1:])
                    for channel in guild.text_channels:
                        try:
                            await channel.send(message)
                            print(Fore.GREEN + f"[+] Message envoyé dans le channel : {channel.name}")
                        except Exception as e:
                            print(Fore.RED + f"Erreur lors de l'envoi du message dans le channel {channel.name} : {e}")
                elif command.startswith("dmall"):
                    print(Fore.YELLOW + "Bientôt disponible pour la v2")
                elif command == "stop":
                    print(Fore.YELLOW + "Déconnexion du bot...")
                    await client.close()
                    break
                else:
                    print(Fore.RED + "Commande inconnue.")

        await client.start(token)
    else:
        print(Fore.RED + f"[-] {error_message}")

# principale
asyncio.run(run())
# Merci de laisser le bot raid dans ce tools, c'est un de nos meilleur code !
