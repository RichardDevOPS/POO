from partie import Partie

x = input("Saisissez la liste des jours séparés par des espaces : ").split(' ')
y = input("Saisissez le nombre de round : ")
z = input("Saisissez le nombre de dès : ")

# print(x)
Game = Partie(x, y, z)
Partie.initialiser(x)
