print("Phonebook  - by alcapitan")
print("Released : 13 Nov 2021")
print()

# Load database
def loaddata():
    liste=[]
    with open("data.txt","r") as fichier:
        for ligne in fichier:
            ligne=ligne.replace("\n","")
            liste.append(ligne)
        repertoire=[]
        extract = []
        for element in liste:
            element = element.lower()
            extract+=element.split(";")
            print(extract)
        dataChecked = 0
        dataProcess = ""
        for dataChecked in range(len(extract)):
        	while dataProcess != "end":
        		'''repertoire.append("a")
        		print(repertoire)'''
        		dataProcess = extract[dataChecked]
        		print(dataProcess)
        		print(dataChecked)
        		print(len(extract))
        		dataChecked += 1
        	dataChecked += 1
        	dataProcess = extract[dataChecked]
        	print("x")
    return repertoire
loaddata()
# Boot
def boot():
    while True:
        choix=menu()
        repertoire=loaddata()

# Menu
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
		print("6 - Paramètres")
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
		elif choix == "6":
			return "settings"
		else:
			close()

# Help


# Add a contact


# Search a contact
def search():
    print("SEARCH A CONTACT")
    request = input("Who are you search : ")
    request = request.lower()
    repertoire = loaddata()
    try:
    	request=repertoire.index(request)
    	if repertoire[request] in repertoire:
    		print(f"{repertoire[request].capitalize()} : ")
    		print(f"\tTéléphone : {repertoire[request+1]}")
    except ValueError:
        print("Contact wanted not found")

# Remove a contact


# Edit a contact
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

# Import a contact


# Settings
''' Language, Reset '''

# Close the program
def close():
    print("CLOSE THE PROGRAM")
    exit()

boot() 