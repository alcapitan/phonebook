print("Phonebook  - by alcapitan")
print("Released : 12 Nov 2021")
print()

# Chargement de la database

def loaddata():
    liste=[]
    with open("data.txt","r") as fichier:
        for ligne in fichier:
            ligne=ligne.replace("\n","")
            liste.append(ligne)
        repertoire=[]
        for element in liste:
            repertoire+=element.split("/")
    return repertoire

# Boot
def boot():
    while True:
        choix=menu()
        repertoire=loaddata()

# Menu du répertoire téléphone
def menu():
	while True:
		print("")
		print("MENU OF PHONEBOOK")
		print("0 - Aide")
		print("1 - Ajouter un contact")
		print("2 - Rechercher un contact")
		print("3 - Supprimer un contact")
		print("4 - Modifier un contact")
		print("5 - Importer des contacts")
		print("Tout autre touche - Quitter le programme")
        
		choix=input("Que voulez vous faire : ")
		print("")
		if choix == "0":
			return "help"
		elif choix == "1":
			return "add"
		elif choix == "2":
			search()
		elif choix == "3":
			return "remove"
		elif choix == "4":
			return "edit"
		elif choix == "5":
			return "import"
		else:
			close()

# Close the program
def close():
    print("CLOSE THE PROGRAM")
    exit()
    
# Search a contact
def search():
    print("SEARCH A CONTACT")
    request=input("Who are you search : ")
    repertoire = loaddata()
    print(repertoire)
    try:
    	recherche_nom=repertoire.index(request)
    except ValueError:
        print("Contact wanted not found")
    if request in repertoire:
    	print(f"{request} : {repertoire[recherche_nom+1]}")


# Fonction pour l'écriture
def ecriture_repertoire(repertoire):
    print("Ecriture en cours")
    while True:
        nom=input("Nom de la personne (0 pour quitter): ")

        if nom=="0" or nom==" " or nom=="":
            print("Vous n'avez pas entré un nom \nRetour au menu principal...\n")
            break
        
        elif nom in repertoire:
            print("Cette personne existe déjà \nRetour au menu principal...\n")
            break
        tel=input("Le numéro de téléphone : ")
        
        if tel=="0" or tel==" " or tel=="":
            print("Vous n'avez pas entré un numéro de téléphone \nRetour au menu principal...\n")
            break
        
        with open("data.txt","a")as fichier:   
            fichier.write(nom+"/"+tel+"\n")
            fichier.close()

boot() 