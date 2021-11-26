import random

class De:
    def __init__(self, valeur=0):
        self.valeur = valeur
        
    @property
    def valeur(self):
        return self._valeur
        
    @valeur.setter
    def valeur(self, valeur):
        self._valeur = valeur
    
    #Génération de la valeur d'un lancer de dé    
    def lancerDe(self):
        self.valeur = random.randint(1, 6)
    
    #renvoie la valeur du dé qui vient d'être lancé    
    def get_valeurDe(self):
        return self.valeur
    
# De1 = De()
# De1.lancer()
# print(De1.valeur)