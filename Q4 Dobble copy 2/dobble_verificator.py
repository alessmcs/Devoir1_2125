# Nom, Matricule
# Nom, Matricule

# cette classe sert a verifier la validite de l'ensemble des cartes du jeu dans le fichier cartes.txt

# doit retourner 0 si tout est correct, 1 si le jeu n'est pas optimal selon l'ordre et 2 si le jeu n'est pas valide

import os.path
from dobble_generator import Generator


class Verificator:
    def __init__(self, generator):
        self.generator = generator.order

    def verify(self, cards_file="cartes.txt", verbose=False):
        if verbose:
            print("***Verification des cartes***")

        correct = 0  # le jeu est correct
        pas_optimal = 1  # pas optimal selon l'ordre
        pas_valide = 2  # le jeu n'est pas valide

        resultat = False

        if os.path.isfile(cards_file):
            with open(cards_file, 'r') as file:
                ligne = file.readlines()
                nombre_carte = len(ligne)

            # test : le nombre de cartes devrait être optimal
            # càd n^2 + n + 1
            carte_optimal = self.generator ** 2 + self.generator + 1


            # test : le nombre de symboles par carte est le même pour chaque carte
            symbole_par_carte = len(ligne[1].split(' '))-1
            symbole_par_carte_optimal = self.generator + 1


            # test : chaque paire de cartes partagent toujours un et un seul symbole en commun
            for i in range(len(ligne)):
                carte1 = ligne[i].split(' ')
                for j in range(i + 1, len(ligne)):
                    carte2 = ligne[j].split(' ')
                    symboles_communs = set(carte1) & set(carte2)  # fonctionne comme une intersection, crée un ensemble contenant leurs éléments communs
                    if len(symboles_communs) != 1:
                        resultat = False
                        break
                    resultat = True


            # test : le nombre de symboles total devrait être optimal
            nombre_total_symbole_optimale = carte_optimal

            liste_symbole = set()
            for i in range(len(ligne)):
                for symbole in ligne[i].split(' '):
                    liste_symbole.add(symbole)     # ajouteras à la liste seulement s'il n'exista pas déjà

            nombre_tot_symbole = len(liste_symbole)


            if carte_optimal == nombre_carte and \
                    symbole_par_carte_optimal == symbole_par_carte \
                    and nombre_total_symbole_optimale == nombre_tot_symbole:
                resultat = True
            elif carte_optimal > nombre_carte or \
                    symbole_par_carte_optimal == symbole_par_carte \
                    or nombre_total_symbole_optimale == nombre_tot_symbole:
                return pas_optimal
            else:
                resultat = False

            if resultat == True:
                return correct
            else:
                return pas_valide

        else:
            print(f"Le fichier {cards_file} n'existe pas.")
            return pas_valide
        # succès (0) si le jeu est valide et optimal
        # avertissement (1) si le jeu de carte n'est pas optimal
        # erreur (2) si le jeu de carte n'est pas valide


generator_instance = Generator(order=7)
verificator_instance = Verificator(generator_instance)

result = verificator_instance.verify(cards_file="cartes.txt", verbose=True)
print(result)
