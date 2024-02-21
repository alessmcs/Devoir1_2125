#Nom, Matricule
#MANCAS Alessandra, 20249098

# cette classe sert a créer les cartes visuelles du jeu dans le dossier "results"
# this class is used to create the game visual cards in the "results" folder

from PIL import Image, ImageDraw
import os
import math
import random

# info :
# https://pillow.readthedocs.io/en/stable/reference/Image.html

class Creator():
    def __init__(self, pic_size=300, border_size=10, padding = 10):
        self.pic_size = pic_size
        self.border_size = border_size
        self.padding = padding

    def make_cards(self, cards_file = "cartes.txt", verbose = False):
        if verbose :
            print("***Creation des cartes visuelles***")

        table = []
        lignes = 0
        if os.path.isfile(cards_file):
            with open(cards_file, 'r') as file:
               lignes = file.readlines()
            for ligne in lignes:
                uneCarte = ligne.strip().split(" ")
                table.append(uneCarte)

        # lecture des images à partir du dossier "images" : "1.png2, "2.png", "3.png", ... "<N>.png"
        dossier_images = "Q4 Dobble copy 2/images"
        images = []
        for filename in os.listdir(dossier_images):
            if filename.endswith(".png"): 
                images.append(os.path.join(dossier_images, filename))

        img = Image.new("RGB", (960, 960), (255, 255, 255))

        # nous avons implémenté la création de cartes pour l'ordre 7 seulement (8 images par carte)
        imageCounter = 0
        for carte in table:
            index = 1
            nbImages = len(carte)
            for i in range(3):
                for j in range(3):
                    if index < nbImages: 
                        paste_region = (15 + j * 315, 15 + i * 315, 15 + 300 + j * 315, 15 + 300 + i * 315)
                        ind = int(carte[index])
                        img.paste(Image.open(images[ind -1]).resize((300, 300)), paste_region)
                        index += 1
            
            img2 = Image.new("RGB", (990, 990), (128, 128, 128)) # ajouter une bordure 
            paste_region2 = (15, 15, 15 + 960, 15 + 960)
            img2.paste(img, paste_region2)
            # enregistrer cartes dans le dossier "results"
            img2.save("Q4 Dobble copy 2/results/card" + str(imageCounter) +".png")
            imageCounter +=1


# Create an instance of the Creator class
card_creator = Creator(pic_size=300, border_size=10, padding=10)

# Call the make_cards method
card_creator.make_cards(cards_file="/Users/alessandramancas/Desktop/Devoir1_2125/Q4 Dobble copy 2/cartes_test6.txt", verbose=True)