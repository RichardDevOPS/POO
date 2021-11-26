from joueur import Joueur
from gobelet import Gobelet

class Partie:
    def __init__(self, joueurs, nb_tours, nb_de):
        self.joueurs= joueurs
        self.nb_tours = nb_tours
        self.nb_de = nb_de
    
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
    def nb_de(self):
        return self._nb_de
    
    @nb_tours.setter
    def nb_de(self, nb_de):
        self._nb_de = nb_de
    
    def get_NbrDe(self):
        return self.nb_de
     
    #On créé un tableau qui vont contenir nos joueurs et on les envoie à la méthode lancer    
    @staticmethod    
    def initialiser(joueurs, nb_tours, nb_de):
        listeJoueurs =[]
        for i in joueurs:
            listeJoueurs.append(Joueur(i))
        Partie.lancer(listeJoueurs, nb_tours, nb_de)
  
    #On lance notre partie, on fait une boucle de lancement de dé (nb_tours) avec un gobelet contenant le nombre de dé (nb_de) et quand la boucle est finie, on l'nevoie à la méthode affichier gagnant
    @staticmethod    
    def lancer(listeJoueurs,nb_tours, nb_de):
        for i in range(int(nb_tours)):
            print(f"\nLancée {i+1}\n")
            for j in listeJoueurs:
                gob = Gobelet(int(nb_de))
                j.jouer(gob)
                print (j.afficher_score())
        Partie.afficher_gagnant(listeJoueurs)    
    
    
    #On extrait le nom et le score des objets joueurs de notre tableau, on les mets dans une liste que l'on va trier par ordre décroissant et on affiche le premier de la liste. Amélioration à faire: vérifier que le deuxième et les suivants ne sont pas ex-equo via une fonction récursive.
    @staticmethod
    def afficher_gagnant(listeJoueurs):
        tabjoueurs=[]
        for k in listeJoueurs:
            listscore = [k.get_nom(),k.get_score()]
            tabjoueurs.append(listscore)
        classement = sorted(tabjoueurs, key=lambda x: x[1], reverse=True)
        print(f"\nLe gagnant est {classement[0][0]}\n")
    
