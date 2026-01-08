
# ============================== Creation de la fonction consulter_solde =====================
def consulter_solde():
    solde = 20000000
    print(f"Votre solde Orange Money est: {solde} FCFA")
    print("9.Acceuil")
    print("0. Annuler")
    choix = int(input('Choix'))
    if choix==1:
        menu_principal()
    else:
        exit()
    print("")

# ============================== Creation de la fonction achat_credit ========================
def achat_credit():
    print("Je souhaite acheter du credit telephone: ")
    print("9.Acceuil")
    print("0. Annuler")
    choix = int(input('Choix'))
    if choix==1:
        menu_principal()
    else:
        exit()
    print("")
         

# ============================== Creation de la fonction achat_credit ========================
def transfert():
    print("Vous souhaitez effectuer un transfert: ")
    print("9.Aceuil")
    print("0. Annuler")
    choix = int(input('Choix'))
    if choix==1:
        menu_principal()
    else:
        exit()
    print("")

# ============================== Creation de la fonction affichage_menu_principal =====================
def affiche_menu_principal():
    
    acces_menu = '#144#'
    while True:
        acces_menu =str(input("Afficher les differents services en utilisant #144#"))
        if acces_menu=='#144#':
            menu_principal()
            break
        else:
            print("code USSD invalide")
           
# ============================== Creation de la fonction menu_principal =====================
def menu_principal():
    while True:
        print("***********************MENU-PRINCIPAL*********************")
        print("1. Consulter le solde")
        print("2. Acheter du credit")
        print("3. Effectuer un transfert")
        print("0. Quitter")
        option = int(input("Option: "))

        if option == 1:
            consulter_solde()

        elif option == 2:

            achat_credit()

        elif option == 3:
            transfert()

        elif option == 4:
            return
        
        else:
            print(" option non valide")
            break
    print("")

affiche_menu_principal()
