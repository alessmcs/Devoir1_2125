#Océane HAYS, 20240742
#Alessandra MANCAS, 20249098

# cette classe sert a créer les cartes du jeu dans le fichier cartes.txt
# this class is used to create the game cards in the cartes.txt file

import random  # pour le melange des symboles sur chaque carte # for mixing symbols on each card
from random import shuffle


class Generator():
    def __init__(self, order=7):  # donc il y aura 13 cartes et 13 symboles
        self.order = order

    def generate(self, cards_file="cartes.txt", verbose=False):
        if verbose:
            print("***Generation des cartes***")

        n = self.order

        tab1 = []
        # ajouter n tableaux vides qui seront de taille n pour avoir un tableau nxn 
        # car ordre n 
        for i in range(n):  # n rangées
            rangee = []
            for j in range(n):  # n colonnes
                rangee.append([])
            tab1.append(rangee)

        tab2 = []  # tableau de taille (n+1)x1 (l'horizon)
        # ajouter n+1 tableaux vides 
        for i in range(n + 1):
            tab2.append([])

        # liste de symboles agit comme une pile, n^2+n+1 symboles possibles 
        symboles = []
        nbCartesSymboles = (n ** 2) + n + 1
        for i in range(nbCartesSymboles):
            symboles.append(i)

        # do the first n symbols 
        for i in range(n):
            s = symboles.pop(0)  # remove from list
            for j in tab1[i]:  # rangée du tab 1
                j.append(s)
            tab2[0].append(s)

        # n prochains symboles
        section = symboles[:n]
        for i in range(n):
            for j in section:
                tab1[i][(section.index(j) + i) % n].append(j)
            tab2[1].append(section[i])

            # pop les n prochains elems
        for i in range(n):
            symboles.pop(0)

        # n prochains symboles
        section2 = symboles[:n]
        index = 0
        for i in range(n):
            for j in section2:
                tab1[i][(section2.index(j) + index) % n].append(j)
            tab2[2].append(section2[i])
            index += 2

        for i in range(n):
            symboles.pop(0)

        index = 3
        while (len(symboles) > 1):
            # remplir les colonnes du tab1 en bonds de n
            # & ajouter au tab2
            for i in range(n):
                s = symboles.pop(0)
                for j in range(n):
                    tab1[j][i].append(s)
                tab2[index].append(s)
            index += 1

        # dernier elem de symboles -> remplir l'horizon
        dernierSymbole = symboles.pop(0)
        for i in tab2:
            i.append(dernierSymbole)



        for c in tab1:
            for i in range(len(c)):
                print(c[i])

        for c in tab2 :
            print(c)


        # melange aléatoire des symboles sur les cartes, (random int between x & y to choose the index)
        # pour ne pas avoir des répétitions de symboles sur les mêmes endroits des cartes
        for c in tab1:
            for i in range(len(c)):
                random.shuffle(c[i])

        for c in tab2:
            random.shuffle(c)

        # ecriture des cartes dans le fichier cards_file
        solString = ""
        file = open(cards_file, "w")
        for c in tab1:
            for i in c:
                ligne = ""
                for j in i:
                    ligne += str(j) + " "
                solString += ligne + "\n"

        for c in tab2:
            ligne = ""
            for i in c:
                ligne += str(i) + " "
            solString += ligne + "\n"

        file = open(cards_file, "w")
        file.write(solString)
        file.close()


generator_instance = Generator(order=7)
print(generator_instance.generate(cards_file="cartes.txt", verbose=True))