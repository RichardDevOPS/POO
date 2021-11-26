from joueur import Joueur
from gobelet import Gobelet

class Partie:
    def __init__(self, joueurs, nb_tours, nb_de):
        self.joueurs= joueurs
        self.nb_tours =nb_tours
        self.nb_de = nb_de
        self.gobe = Gobelet
    
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
    
    @staticmethod    
    def initialiser(joueurs):
        listeJoueurs =[]
        for i in joueurs:
            listeJoueurs.append(Joueur(i))
        Partie.lancer(listeJoueurs)
  
        
    @staticmethod    
    def lancer(listeJoueurs):
      for j in listeJoueurs:
            j.jouer(Gobelet(3))
            print(j.get_score())
            
    
    def afficher_gagnant(self):
        pass
    
