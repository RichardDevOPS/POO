from gobelet import Gobelet

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.score = 0
        
    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self, nom):
        self._nom = nom
        
    @property
    def score(self):
        return self._score
        
    @score.setter
    def score(self, score):
        self._score = score
        
    def get_nom(self):
        return self.nom
    
    def get_score(self):
        return self.score
    
    def jouer(self, gob: Gobelet):
        gob.lancer()
        self.score = self.score + gob.get_valeur()
        
    def afficher_score(self):
        print(f"Le score de {self.nom} est de {self.score}")
        
# J1=Joueur("Richard")
# gob=Gobelet(3)
# J1.jouer(gob)
# print(J1.get_score())