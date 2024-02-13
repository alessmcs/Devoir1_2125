#Océane HAYS, Matricule
#Alessandra MANCAS, 20249098

import math
import sys
INFINITY = math.inf

#TODO: interpréter les fichiers input 
    # PARSER CHQ PROBLÈME 
    # coordonnées sont en x & y (par convention)
    # chq ligne est un sommet avec ses coordonnées respectives


#TODO: Kruskal en python a partir du pseudocode 

#Fonctions pour lire/écrire dans les fichier. Vous pouvez les modifier, 
#faire du parsing, rajouter une valeur de retour, mais n'utilisez pas
#d'autres librairies.
def read_problems(input_file):
    # lecture du fichier/file reading
    file = open(input_file,"r")
    lines = file.readlines() #lines est un tableau avec chaque ligne du fichier texte
    graphes = []
    nbProblemes = lines[0]
    index = 1
    while index <= (lines.len() + 1):
        nbSommets = lines[index]
        unGraphe = [] #le graphe est un tableau de sommets
        # Lire les coordonnées pour chaque sommet
        for ligne in range(1, nbSommets):
            coordonnees = lines[index + ligne].split(" ")
            unGraphe.append(coordonnees)
        graphes.append(unGraphe) #rajouter a la liste de tous les graphes des problemes
        index += nbSommets
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
    listeAretes = [] # une arête sera de la forme [s1, s2, long]
    # calculer la longueur de chaque arête dans le graphe
    for i in range(sommets.len()-1):
        for j in range(sommets.len() - 1):
            if i!=j:
                arete = [sommets[i], sommets[j], distance(sommets[i], sommets[j])]
                if arete not in listeAretes: # évite la duplication
                    listeAretes.append(arete)
                    listeAretes.sort() # trier à chaque fois qu'on ajoute 
    return 

def kruskal(listeAretes, listeSommets):
    arbre = []
    while arbre.len() < (listeSommets.len() - 1):
        areteMin = listeAretes.pop()
    return 

#Fonction main/Main function
def main(args):
    input_file = args[0]
    output_file = args[1]
    
    #tableau des différents problèmes 
    problemes = read_problems(input_file)

    for p in problemes:
        graphe = p # un graphe
        traiterGraphe(graphe)
        # calculer la longueur de chaque arête dans le graphe



    #Toutes les arêtes entre chaque paire de sommets sont possibles 
    #Le poids d'une arête est la distance euclidienne entre les 2 coordonnées 
    #On pourrait copier le pseudocode vu en classe & implementer l'algo 
    #Réponse retournée doit être le poids de l'ACM

    #TODO : Continuer ici/Complete here...
    #Vous pouvez découper votre code en d'autres fonctions...
    #You may split your code in other functions...


#NE PAS TOUCHER
#DO NOT TOUCH
if __name__ == '__main__':
    main(sys.argv[1:])
