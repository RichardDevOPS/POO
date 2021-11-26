from de import De

class Gobelet:
    def __init__(self,nbDeDes):
        self.nbDeDes = nbDeDes
        self.creerListeDe()
        
    @property
    def nbDeDes(self):
        return self._nbDeDes
        
    @nbDeDes.setter
    def nbDeDes(self, nbDeDes):
        self._nbDeDes = nbDeDes
        
    # Avec  creerListeDe(), on créé une liste d'objet De correspondant aux nombre de dés passé en paramètre
    def creerListeDe(self):
        self.valeur = 0
        self.des = [ De() for i in range(self.nbDeDes)]
    
    #On calcule la somme des dès du lancé
    def lancer(self):
        for i in self.des:
            i.lancerDe()
            self.valeur += i.valeur
    
    #On renvoie la valeur du lancé    
    def get_valeur(self):
        return self.valeur
    
    #On affiche la valeur du lancé    
    def afficher_score(self):
        print(f"Le résultat du lancer est {self.valeur}")
            
# Gob1= Gobelet(3)
# Gob1.lancer()
# Gob1.get_valeur()
# Gob1.afficher_score()
