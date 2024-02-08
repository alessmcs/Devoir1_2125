#Océane HAYS, Matricule
#Alessandra MANCAS, Matricule

import math
import sys
INFINITY = math.inf

#Fonctions pour lire/écrire dans les fichier. Vous pouvez les modifier, 
#faire du parsing, rajouter une valeur de retour, mais n'utilisez pas
#d'autres librairies.
def read_problems(problems, input_file):
    # lecture du fichier/file reading
    file = open(input_file,"r")
    lines = file.readlines()
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
    #Réponse retournée doit être le poids de l'ACM
    #TODO : Continuer ici/Complete here...
    #Vous pouvez découper votre code en d'autres fonctions...
    #You may split your code in other functions...


#NE PAS TOUCHER
#DO NOT TOUCH
if __name__ == '__main__':
    main(sys.argv[1:])
