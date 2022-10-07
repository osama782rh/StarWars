"""Des personnages sont incarnés par des acteurs dans ces films correspondant aux classes suivantes,
Certains personnages sont des méchants, ils font partie du côté obscur, et certains sont gentils et ils
font partie de la force.
"""
from film import Film
import random
from personnage import Personnage
from acteur import Acteur
from mechant import Mechant
from gentil import Gentil

confirmation = 'o'
cout = random.randint(100, 300)
recette = random.randint(100, 300)


def creer_film():
    res = ""
    while res == "":
        titre = input("Nom du film que vous voulez créer : ")
        print("Le nom est :", titre)
        annee_sortie = input("Année de sortie du film que vous voulez créer : ")
        print("L\'année de sortie est : ", annee_sortie)
        numero_episode = input("Numéro épisode que vous voulez créer : ")
        print("Le numéro d'épisode est :", numero_episode)
        res = input(
            f"Si vous confirmez la création tapez sur 'o' si vous voulez recommencez appuyer sur 'n' : {titre},"
            f"{annee_sortie}, {numero_episode} : ")

        if res.lower() == confirmation and titre != "" and annee_sortie != "" and numero_episode != "":
            film3 = Film(titre, annee_sortie, numero_episode, cout, recette)
            break
        else:
            print('Error : VOUS DEVEZ REMPLIR CORRECTEMENT LES CHAMPS ET CONFIRMER LA CREATION')
            res = ""
    return film3


film1 = Film('Star Wars, Un nouvel espoir', '177', 'Episode IV', cout, recette)
film2 = Film('Star Wars, L\'Empire contre-attaque', '1980', 'Episode V', cout, recette)
film3 = creer_film()
collectionFilms = [film1, film2, film3]


# Partie Personnage

def creer_personnage():
    res = ""
    while res == "":
        # demander des noms de personnes
        nom: str = input("Saisir le nom du personnage que vous voulez créer : ")
        print("Le nom est :", nom)
        prenom = input("Saisir le prenom du personnage que vous voulez créer : ")
        print("Le nom est : ", prenom)
        # seulement à la fin afficher tous les noms
        if res.lower() == confirmation and nom != "" and prenom != "":
            mon_personnage = Personnage(nom, prenom)
        else:
            print('Error : VOUS DEVEZ REMPLIR CORRECTEMENT LES CHAMPS ET CONFIRMER LA CREATION')
            res = ""
    return mon_personnage


personnage1 = creer_personnage()
personnage2 = Personnage('George', 'Lucas')
personnage3 = Personnage('Irvin', 'Kershner')
collectionPersonnage = [personnage1, personnage2, personnage3]


def afficher_films():
    for n in range(0, len(collectionFilms)):
        print(collectionFilms[n])


# Donnez le code pour créer un acteur incarnant deux personnages
def creer_acteur():
    """Méthode qui fonctionne pas correctement"""

    personnageActeur = ""
    nom = input("Saisissez le nom de l'acteur que vous voulez créér : ")
    prenom = input("Saisissez le prénom de l'acteur que vous voulez créér : ")
    for i in range(1, 3):
        while personnageActeur == "":
            print('Personnage de l\'acteur, ', nom, ' ,numéro', i, ' / 2')
            personnageActeur = str(
                input(" '1': Si votre personnage est gentil  \n '2' : Si votre personnage est méchant : \n "))
            if personnageActeur != '1' and personnageActeur != '2':
                personnageActeur = ""
                print("Veuillez saisir '1 ou '2'")
            else:
                if personnageActeur == '1':
                    collectionPersonnage.append(Gentil(nom, prenom))
                else:
                    collectionPersonnage.append(Mechant(nom, prenom))
    acteur = Acteur(nom, prenom, collectionPersonnage)


print(afficher_films())




