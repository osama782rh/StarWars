# Déclaration de la classe personnage
class Personnage:
    # Déclaration du constructeur

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    # Déclaration des getteurs et setteurs
    def get_nom(self):
        print("getter method called")
        return self.nom

    def set_nom(self, x):
        print("setter method called")
        self.nom = x

    def get_prenom(self):
        print("getter method called")
        return self.prenom

    def set_prenom(self, x):
        print("setter method called")
        self.prenom = x

    # Déclaration des méthodes
    def __str__(self):
        return f"Le nom est : {self.nom} et le prénom est : {self.prenom}"
