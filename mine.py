#!/usr/bin/python -tt

from bitcoin import *
from urllib.request import urlopen
import json
from rich.console import Console
import time
import random
import pyfiglet

console = Console()

ascii_banner = pyfiglet.figlet_format("MyEcoria")

console.print("[bold cyan]" + ascii_banner + "[/bold cyan]")
print ("===============================================================================================")
console.print("[bold magenta] Ce script génére automatiquement des wallet, si il y a de la moulaga, \n il enregistre les informations dans le fichier adresses.txt à la racine \n du script sinon il l'enregistre dans nopes.txt [/bold magenta]")
print ("===============================================================================================")
while 0 < 1:

    # Generation de l'adresse
    priv = random_key()
    pub = privtopub(priv)
    addr = pubtoaddr(pub)
    h = history(addr)

    # Récupération de la solde
    url = "https://blockchain.info/rawaddr/" + addr
    response = urlopen(url)
    data_json = json.loads(response.read())
    balance = str(data_json["final_balance"])
    text = "\n Clef privé: " + priv + ", clef publique: " + \
        pub + ", Adresse: " + addr + ", Solde: " + balance

    if int(balance) > 0:
        with open("adresses.txt", "a") as fichier:
            fichier.write(text)
            fichier.close

    if int(balance) == 0:
        with open("nopes.txt", "a") as fichier:
            fichier.write(text)
            fichier.close

    console.print("[bold cyan]Adresse:[/bold cyan] " + addr + " [bold magenta]=>[/bold magenta] " + balance)
    
    time.sleep(5)
