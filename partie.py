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
        for i in range(10):
            print(f"\nLancée {i+1}\n")
            for j in listeJoueurs:
                gob = Gobelet(3)
                j.jouer(gob)
                # print(gob.get_valeur())
                print (j.afficher_score())
        Partie.afficher_gagnant(listeJoueurs)    
    
    
    @staticmethod
    def afficher_gagnant(listeJoueurs):
        tabjoueurs=[]
        for k in listeJoueurs:
            listscore = [k.get_nom(),k.get_score()]
            tabjoueurs.append(listscore)
            # tabjoueurs.append(k.get_nom())
            # tabjoueurs.append(k.get_score(),k.get_nom())
        classement = sorted(tabjoueurs, key=lambda x: x[1], reverse=True)
        print(f"\nLe gagnant est {classement[0][0]}")
    
