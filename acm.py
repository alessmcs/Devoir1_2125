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


def write(fileName, content):
    #écrire la sortie dans un fichier/write output in file
    file = open(fileName, "w")
    file.write(content)
    file.close()


#Fonction main/Main function
def main(args):
    input_file = args[0]
    output_file = args[1]
    



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
