from partie import Partie

x = input("Saisissez la liste des joueurs séparés par des espaces : ").split(' ')
y = input("Saisissez le nombre de round : ")
z = input("Saisissez le nombre de dès : ")

# On crée notre partie. Correction à faire, supprimer les paramètres y et z (nbre de round et de dé), vu qu'on les renvoie dans la méthode suivante
Game = Partie(x, y, z)
#On l'initialise
Partie.initialiser(x, y, z)
