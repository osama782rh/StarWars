from personnage import Personnage


# La classe Mechant est étendue (extends) de la classe Personnage.
class Mechant(Personnage):

    # Déclaration du constructeur
    def __init__(self, nom, prenom, coteObscur):
        # Appelez au constructeur de la classe mère (Personnage)
        # pour attribuer la valeur au attribut 'nom' et 'prenom' de la classe mère.
        super().__init__(self, nom, prenom)  # super().__init__(nom, prenom)
        self.coteObscur = coteObscur

    # Déclaration des getteurs et setteurs
    def get_coteObscur(self):
        print("getter method called")
        return self.coteObscur

    def set_coteObscur(self, x):
        print("setter method called")
        self.coteObscur = x

    # Méthode string
    def __str__(self):
        return f"Le personnage {self.nom} , {self.prenom} est méchant son coté obscure est : {self.coteObscur}"
