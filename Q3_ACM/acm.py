#Océane HAYS, Matricule
#Alessandra MANCAS, 20249098

import math
import sys
INFINITY = math.inf

#TODO: Kruskal en python a partir du pseudocode 

#Fonctions pour lire/écrire dans les fichier. Vous pouvez les modifier, 
#faire du parsing, rajouter une valeur de retour, mais n'utilisez pas
#d'autres librairies.
def read_problems(input_file):
    # lecture du fichier/file reading
    file = open(input_file,"r")
    lines = [line.strip() for line in file.readlines()]
    graphes = []
    nbProblemes = int(lines[0])
    index = 1
    while index < (len(lines)):
        nbSommets = int(lines[index])
        unGraphe = [] #le graphe est un tableau de sommets
        # Lire les coordonnées pour chaque sommet
        for ligne in range(1, nbSommets + 1):
            coordonnees = lines[index + ligne].split(" ")
            unGraphe.append(coordonnees)
        graphes.append(unGraphe) #rajouter a la liste de tous les graphes des problemes
        index += nbSommets + 1
    file.close()
    return graphes

# Faire une fonction pour calculer la distance euclidienne entre les sommets 
def distance(sommet1, sommet2):
    # Les sommets sont un tableau de taille 2 tq le sommet x aie les composantes [x1, x2]
    return math.sqrt((float(sommet2[0]) - float(sommet1[0]))**2 + (float(sommet2[1]) - float(sommet1[1]))**2)


def write(fileName, content):
    #écrire la sortie dans un fichier/write output in file
    file = open(fileName, "w")
    file.write(content)
    file.close()

def traiterGraphe(sommets):
    nbSommets = len(sommets);
    matAdj = []
    # calculer la longueur de chaque arête dans le graphe
    for i in range(nbSommets):
        unSommet = []
        for j in range(nbSommets):
            if i == j:
                unSommet.append(0)
            else:
                dist = distance(sommets[i], sommets[j])
                unSommet.append(dist) # ajouter a la matrice d'adjacence 
        matAdj.append(unSommet)
    for ligne in matAdj:
        print(ligne)
    return matAdj

# algo de prim adapté pour retourner le poids des arêtes seulement 
# source: https://www.programiz.com/dsa/prim-algorithm#:~:text=Prim's%20Algorithm%20pseudocode,connecting%20the%20least%20weight%20edge
def prim(matAdj):
    arbre = []
    selectionnee = []
    numSommets = len(matAdj) 
    for i in range(numSommets):
        selectionnee.append(0)
    num_arete = 0
    selectionnee[0] = True #on commence par sélectionner la 1ere arête
    while num_arete < (numSommets - 1):
        min = INFINITY
        u_p = 0
        u = 0
        for i in range(numSommets):
            if selectionnee[i]: #si le sommet est sélectionné en ce moment
                for j in range(numSommets):
                    if( (not selectionnee[j]) and matAdj[i][j]):
                        if min > matAdj[i][j]:
                            min = matAdj[i][j]
                            u_p = i
                            u = j
        arbre.append(matAdj[u][u_p])
        selectionnee[u] = True
        num_arete += 1
    poidsTotal = 0
    for i in arbre: 
        poidsTotal += i
    return poidsTotal

#Fonction main/Main function
def main(args):
    input_file = "/Users/alessandramancas/Desktop/Devoir1_2125/input0.txt"
    input_file = args[0]
    output_file = args[1]
    
    #tableau des différents problèmes 
    problemes = read_problems(input_file)
    for p in problemes:
        graphe = p # un graphe
        matAdj = traiterGraphe(graphe) # retourne une matrice d'adjacence contenant les poids des arêtes
        poidsTotal = prim(matAdj) # prim retourne le poids total 
        write(output_file, poidsTotal)


#NE PAS TOUCHER
#DO NOT TOUCH
if __name__ == '__main__':
    main(sys.argv[1:])
