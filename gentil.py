from personnage import Personnage


class Gentil(Personnage):
    def __init__(self, nom, prenom, force):
        # Appelez au constructeur de la classe mère (Personnage)
        # pour attribuer la valeur au attribut 'nom' et 'prenom' de la classe mère.
        super().__init__(nom, prenom)
        self.force = force
        
    def get_force(self):
        print("getter method called")
        return self.force

    def set_force(self, x):
        print("setter method called")
        self.force = x

    def __str__(self):
        return f"Le personnage {self.nom} , {self.prenom} est Gentil, sa force est : {self.force}"


