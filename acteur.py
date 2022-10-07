#Déclaration de la classe Acteur
from personnage import Personnage


class Acteur:

    #Déclaration du constructeur
    def __init__(self, nom: str, prenom: str, personnages):
        self.nom = nom
        self.prenom = prenom
        self.personnages = personnages

    #Déclaration des getteurs et setteurs
    def get_nom(self):
        print("getter method called")
        return self.nom

    def set_nom(self, nom):
        print("setter method called")
        self.nom = nom

    def get_prenom(self):
        self.prenom

    def set_prenom(self, prenom):
        print("setter method called")
        self.prenom = prenom

    # Méthode string
    def __str__(self):
        strpersonnage = ""
        i = 1
        for personnage in self.personnages:
            strpersonnage += str(i) +" "+ personnage.__str__() +"\n"
            i+=1
        return f'Nom : {self.nom} \nPrénom : {self.prenom}\nPersonnnages :\n{strpersonnage}'

    #Méthode qui retourne le nombre de personnage incarnés par cet acteur
    def nbPersonnage(self):
        nbPersonnage = len(self.personnages)
        return nbPersonnage




