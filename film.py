import random
from acteur import Acteur


# Déclaration de la class Film
class Film:
    # Déclaration de la liste d'acteurs

    # Déclaration du tuple des personnage

    def __init__(self, titre: str, annee_sortie: str, num_episode: str, cout: int, recette: int, acteurs):
        # Avoir un ID acteur pour savoir à qui appartient le film
        self.titre = titre
        self.annee_sortie = annee_sortie
        self.num_episode = num_episode
        # Valeur inventé entre 100 et 300 pour le montant de la recette et du cout
        self.cout = cout
        self.recette = recette
        self.acteurs = acteurs

    # Déclaration des getteurs et setteurs
    def get_titre(self):
        return self.titre

    def set_titre(self, x):
        self.titre = x

    def get_annee_sortie(self):
        return self.annee_sortie

    def set_annee_sortie(self, x):
        self.annee_sortie = x

    def get_num_episode(self):
        return self.num_episode

    def set_num_episode(self, x):
        self.num_episode = x

    def get_cout(self):
        return self.cout

    def set_cout(self, x):
        self.cout = x

    def get_recette(self):
        return self.recette

    def set_recette(self, x):
        self.recette = x

    def get_acteurs(self):
        return self.acteurs

    def set_acteurs(self, x):
        self.acteurs = x

    # Méthode string
    def __str__(self):
        return f'Le titre du film est : {self.titre} \nL\'année de sortie est : {self.annee_sortie}  ' \
               f'\nLe numéro d\'épisode est : {self.num_episode}\nLe coût est : {self.cout}' \
               f'\nLa recette est de : {self.recette} '\


    #Méthode qui retourne le nombre d'acteurs par film
    def nbActeurParFilm(self):
        nbActeurs = len(self.acteurs)
        return nbActeurs

    #Méthode qui retourne le nombre de personnages dans le film
    '''Méthode pas sûre'''
    def nbPersonnagesFilm(self):
        for acteur in self.acteurs:
            nbPersonnages = len(acteur.personnages)
            # nbPersonnages = len(self.Acteur.personnages)
            return nbPersonnages

    #Méthode qui retourne le montant pour savoir si le film est bénéficiaire et si oui de combien
    def calculBenefice(self):
        benefice = self.recette - self.cout
        if benefice > 0:
            return True, benefice
        else:
            return False, benefice

    #Méthode qui retourn vrai si la date du film est avant le date passé en paramètre
    def isBefore(self, annee):
        if annee > self.annee_sortie:
            return True, f'Le film est sorti aprés l\'année {annee}'
        else:
            return False, f'Le film est sorti avant l\'année {annee}'

    #Méthode qui trie la liste par ordre alphabétique
    def sortedActeurs(self):
        sorted_list = sorted(self.acteurs)
        return sorted_list


# Méthode qui renvoie le nombre d'acteurs du film
'''
    def nbActeurs(self, titre):
        print("Nom des personnes")
        nombre = 0
        acteurs.sort()  # ordre alphabétique A-Z a-z
        for titre in acteurs:
            print("Pour le film " + titre, " Le nombre d'acteurs dans le film est : " nombre)



'''
