from gobelet import Gobelet

class Partie:
    def __init__(self, joueurs, nb_tours, gobe: Gobelet):
        self.joueurs= joueurs
        self.nb_tours =nb_tours
        self.gobe = gobe
        self.constructor()
    
    @property
    def joueurs(self):
        return self._joueurs
    
    @joueurs.setter
    def joueurs(self, joueurs):
        self._joueurs = joueurs
        
    @property
    def nb_tours(self):
        return self._nb_tours
    
    @nb_tours.setter
    def nb_tours(self, nb_tours):
        self._nb_tours = nb_tours
        
    @property
    def gobe(self):
        return self._gobe
    
    @gobe.setter
    def gobe(self, gobe):
        self._gobe = gobe
        
    def constructor(self, nb_tours, nb_des):
        pass
        
    def initialiser():
        pass
    
    def lancer():
        pass
    
    def afficher_gagnant():
        pass