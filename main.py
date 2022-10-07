from film import Film
from acteur import Acteur
from personnage import Personnage
from mechant import Mechant
from gentil import Gentil

import random

# Variable de confirmation lors de la demande de confirmation pour l'utilisateur
confirmation = 'o'
# Déclaration de la varaible du menu pricipal
choix = ''
# Cout et recette valeur aléatoires !
cout = random.randint(100, 200)
recette = random.randint(200, 400)
# liste des acteurs
lesActeurs = list()

# Déclaration de la liste des films et création de deux films avec une liste vide d'acteurs
lesFilms = list()
film1 = Film('Star Wars, Un nouvel espoir', '1770', 'Episode IV', cout, recette, lesActeurs)
film2 = Film('Star Wars, L\'Empire contre-attaque', '1980', 'Episode V', cout, recette, lesActeurs)
# Ajout des deux films dans la liste
lesFilms.append(film1)
lesFilms.append(film2)

'''Méthodes'''


# Méthode qui permet de faire des sauts de ligne sans répétion du \n
def retour():
    print('\n' * 2)


#Méthode qui crée des films
def creerFilms():
    retour()
    res = ""
    acteurs = list()
    # Boule qui vérifie que l'utilisateur confirme bien la création du film sinon tourne en boucle
    while res == "":
        titre = input("Nom du film que vous voulez créer : ")
        print("Le nom est :", titre)
        annee_sortie = input("Année de sortie du film que vous voulez créer : ")
        print("L\'année de sortie est : ", annee_sortie)
        numero_episode = input("Numéro épisode que vous voulez créer : ")
        print("Le numéro d'épisode est :", numero_episode)
        retour()
        # res = confirmation de la création du film, s'il confirme il quitte la bocle
        res = input(
            f"Titre : {titre}\nAnnée de sortie : {annee_sortie} \nNuméro Episode : {numero_episode}\n"
            f"Si vous confirmez la création tapez sur 'o' si vous voulez recommencez appuyer sur 'n' [o/n] : ")

        # Vérifiation que les champs ne sont pas vides et que l'utilisateur confirme bien avec 'o
        if res.lower() == confirmation and titre != "" and annee_sortie != "" and numero_episode != "":
            film3 = Film(titre, annee_sortie, numero_episode, cout, recette, list())
            # Si l'utilisateur confirme la création des acteurs pour ce film je fais appel à la méthode pour créér
            # des acteur
            confAct = input("Voulez vous créer des acteurs pour ce film ? [o/n] : ")
            if confAct == 'o' or confAct == 'O':
                # le nombre d'acteurs souhaités
                nbActeurs = int(input('Combien d\'acteurs voulez vous ajouter à ce film ? : '))
                # si mauvaise saisi (autre qu'un chiffre), message d'erreur qui s'affiche et contraint de verifie
                nbActeurs = int(nbActeurs)
                # Boucle qui va de 1 jusq'au nombre d'acteurs souhaité
                for i in range(1, nbActeurs + 1):
                    print(f'Acteur numéro {i} / {nbActeurs}')
                    acteur = creerActeur()
                    acteurs.append(acteur)
            # Si l'utilisateur ne souhaite pas la création d'acteurs pour ce film
            elif confAct == 'n' or confAct == 'N':
                print(f'Vous n\'avez pas créer d\'acteurs pour le film {titre.upper()}')

            # Si l'utilisatuer saisi autre que 'o' ou 'n' message d'erreur qui s'affiche
            else:
                retour()
                print('ERREUR : Voulez vous créer des acteurs pour ce film ? [o/n] : ')
                confAct == ''
        else:
            retour()
            res = ""
            print('Vous avez annullé la création veuillez recommencer')
    # set_acteurs = méthode qui modifie les acteurs d'un film
    film3.set_acteurs(acteurs)

    return film3


#Méthode qui affiche les films
def afficherFilms():
    retour()
    for k, unFilm in enumerate(lesFilms, 1):
        print(k, ":", unFilm.__str__())
        print("\n" * 2)


# Instantiation du tuple des personnages et création de deux personnages
lesPersonnages = ()
personnage2 = Personnage('George', 'Lucas')
personnage3 = Personnage('Irvin', 'Kershner')
#Ajout des deux personnages au tuple
lesPersonnages += (personnage2, )
lesPersonnages += (personnage3, )


# Méthode pour creer un personnage
def creerPersonnage():
    retour()
    res = ""
    mon_personnage = ''
    while res == "":
        # demander des noms de personnes
        nom: str = input("Saisir le nom du personnage que vous voulez créer : ")
        print("Le nom est :", nom)
        prenom: str = input("Saisir le prenom du personnage que vous voulez créer : ")
        print("Le nom est : ", prenom)
        # seulement à la fin afficher tous les noms
        res = input(f"Nom : {nom} \nPrénom : {prenom} \nConfirmez-vous la création du personnage ? [o/n] : ")
        if res.lower() == confirmation and nom != "" and prenom != "":
            mon_personnage = Personnage(nom, prenom)
            retour()
            print("Vous avez créer le personnage avec succés !")
        elif res.lower() == 'n':
            retour()
            res = ""
            print('Vous avez annnuler la création du personnage : Veuillez recommencer :)')
        else:
            retour()
            print('ERREUR : Veuillez recommencer la création ! ')

    return mon_personnage


# Liste numérique pour afficher la liste des personnages
def afficherPersonnage():
    retour()
    print('Liste des personnages : \n')
    for k, unPersonnage in enumerate(lesPersonnages, 1):
        print(k, ":", unPersonnage.__str__())
        print("\n" * 2)


# Méthode pour créer un acteur avec minimum 2 personnages
def creerActeur():
    retour()
    personnageActeur = ""
    nom = input("Saisissez le nom de l'acteur que vous voulez créér : ")
    prenom = input("Saisissez le prénom de l'acteur que vous voulez créér : ")
    confPers = ''
    nbPers = 0
    while confPers == '':
        confPers = input("Voulez vous creer des personnages pour cet acteur ? [o/n] : ")
        if confPers == 'o' or confPers == 'O':
            while nbPers == 0:
                nbPers = input("Combien de personnages cet acteur incarne-t-il ? : ")
                try:
                    nbPers = int(nbPers)
                except:
                    print('Erreur saisisser un chiffre. Réessayez ')
                    nbPers = 0
                else:
                    if nbPers >= 2:
                        for i in range(1, int(nbPers + 1)):
                            print('Personnage de l\'acteur, ', nom, ' ,numéro', i, ' /', nbPers)
                            personnageActeur = str(
                                input("Si votre personnage est gentil ..........1\n"
                                      "Si votre personnage est méchant..........2\n"))
                            if personnageActeur == "1":
                                force = input('Quelle est la force de votre personnage ? : ')
                                mon_personnage = creerPersonnage()
                                lesPersonnages += (Gentil(mon_personnage.nom, mon_personnage.prenom, force), )
                            elif personnageActeur == "2":
                                coteObscur = input('Quelle est le coté obcur de votre personnage ? : ')
                                mon_personnage = creerPersonnage()
                                lesPersonnages += (Mechant(mon_personnage.nom, mon_personnage.prenom, coteObscur), )
                    elif nbPers < 2:
                        print('Vous devez créer minimum 2 personnages par acteur :)')
                        nbPers = 0
        elif confPers == 'n' or confPers == 'N':
            lesPersonnages = lesPersonnages + ()
        else:
            retour()
            print('ERREUR : Voulez vous créer des personnages pour cet acteur ? [o/n]')
            confPers = ''

    mon_acteur = Acteur(nom, prenom, lesPersonnages)
    return mon_acteur


# Méthode qui affiche la liste des acteurs
def afficherActeur():
    retour()
    print('Liste des acteurs: \n')
    for k, unActeur in enumerate(lesActeurs, 1):
        print(k, ":", unActeur.__str__())
        print("\n" * 2)


# Méthode qui prend en paramètre un dictionnaire de films l’année du film étant la clé et la valeur est l’objet)
# et qui écrit pour chaque film la ligne suivante :l’année – le titre – le bénéfice :
def MakeBackUp(dictioFilm):
    retour()
    for annee in list(dictioFilm.keys()):
        value = dictioFilm.get(annee)
        #Appel à la méthode calculbenefice qui m'envoie deux valeurs (True ou false) et (le montant du bénéfice
        beneficiaire, benefice = value.calculBenefice()
        print(value.annee_sortie, ' - ', value.titre, ' - ', benefice)


# Menu principal
while choix != "Q" and choix != "q":
    print("Créer des films..................1")
    print("Créer des acteurs................2")
    print("Créer des personnages............3")
    print("Quitter..........................Q")
    choix = input("Votre choix                      : ")

    # Création d'un film
    if choix == "1":
        #Ajout d'un film à la liste des films
        lesFilms.append(creerFilms())
        #Si l'utilisatuer veut afficher les films
        affiche_films = input('Voulez vous afficher les films ? [o/n] : ')
        if affiche_films == 'o' or affiche_films == 'O':
            afficherFilms()
        #Si l'utilisateur veut afficher le dictionnaire des films
        affiche_dictio = input('Voulez vous afficher le dictionnaire des films ? [o/n] : ')
        if affiche_dictio == 'o' or affiche_dictio == 'O':
            dictioFilm = {film.annee_sortie: film for film in lesFilms}
            MakeBackUp(dictioFilm)
        #Saut de ligne
        retour()

    #Création d'acteur
    elif choix == "2":
        monActeur = creerActeur()
        #Ajout d'acteur dans la liste des actuers
        lesActeurs.append(monActeur)
        #Si l'utilisateur veut afficher la liste des acteurs
        affiche_acteurs = input('Voulez vous afficher les acteurs ? [o/n] : ')
        if affiche_acteurs == 'o' or affiche_acteurs == 'O':
            for acteur in lesActeurs:
                print(acteur.__str__())
        #Saut de ligne
        retour()

    #Création de personnage
    elif choix == "3":
        #Ajout d'un personnage dans le tuple
        lesPersonnages += (creerPersonnage(),)
        #Si le personnage veut afficher les acteurs
        affiche_personnages = input('Voulez vous afficher les personnages ? [o/n] : ')
        if affiche_personnages == 'o' or affiche_personnages == 'O':
            afficherPersonnage()
        #Saut de ligne
        retour()
