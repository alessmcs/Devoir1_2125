#Nom, Matricule
#Nom, Matricule

# cette classe sert a créer les cartes visuelles du jeu dans le dossier "results"
# this class is used to create the game visual cards in the "results" folder

from PIL import Image
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

        ordre = 0
        if os.path.isfile(cards_file):
            with open(cards_file, 'r') as file:
                ligne = file.readlines()
                ordre = len(ligne)

        #img = Image.new("RGB", (, height), background_color)

        # Lecture des images à partir du dossier "images" : "1.png2, "2.png", "3.png", ... "<N>.png"
        dossier_images = "Q4 Dobble copy 2/images"
        images = []
        for filename in os.listdir(dossier_images):
            if filename.endswith(".png"): 
                images.append(os.path.join(dossier_images, filename))

        # essayer de faire une carte avec une image 
        img = Image.new("RGB", (500, 500), (255, 255, 255))

        # Specify the region to paste onto
        paste_region = (10, 10, 10 + 300, 10 + 300)  # Adjust these values as needed (left, upper, right, lower)

        # Paste the first image onto the specified region
        img.paste(Image.open(images[0]).resize((300, 300)), paste_region)

        # Save or display the resulting image
        img.show()


        #for carte in range(len(ligne)) :
        #une_carte = Image.new("RBG", (500,500),(255, 255, 255))
            # placement des images sur les cartes visuelles, rotations appréciées
             #for image in images:
       # image = Image.open(dossier_images)
        #image.resize(self.pic_size)
        #une_carte.paste(image, (0,0))
        #image.show()

        # Ajout de la bordure sur les cartes visuelles
        # sauvegarde des cartes dans le dossier "results" : "card1.jpg", "card2.jpg", "card3.jpg", ... "card<N>.jpg"
            
        # reading images from the "images" folder: "1.png2, "2.png", "3.png", ..., "<N>.png"
        # placement of images on visual cards, rotations appreciated
        # added border on visual cards
        # save cards in the “results” folder : "card1.jpg", "card2.jpg", "card3.jpg", ... "card<N>.jpg"

# Create an instance of the Creator class
card_creator = Creator(pic_size=300, border_size=10, padding=10)

# Call the make_cards method
card_creator.make_cards(cards_file="cartes.txt", verbose=True)