from bitcoin import *
from urllib.request import urlopen
import json
from rich.console import Console

console = Console()
while 0 < 1 :
	# Generation de l'adresse
        
	priv = sha256("truc")
	pub = privtopub(priv)
	addr = pubtoaddr(pub)
	h = history(addr)

	# Récupération de la solde
	url = "https://blockchain.info/rawaddr/" + addr
	response = urlopen(url)
	data_json = json.loads(response.read())
	balance = str(data_json["final_balance"])
	text = "\n Clef privé: " + priv + ", clef publique: " + pub + ", Adresse: " + addr + ", Solde: " + balance

	with open("adresses.txt", "a") as fichier:
		fichier.write(text)


	console.print ("[bold cyan]Adresse:[/bold cyan] " + addr + " [bold magenta]=>[/bold magenta] " + balance)
        
