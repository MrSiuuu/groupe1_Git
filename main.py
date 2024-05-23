import random

# Lecture du fichier mot.txt
with open('mot.txt', 'r', encoding='utf-8') as fichier:
    mots = fichier.read().splitlines()

# Initialisation du dictionnaire des occurrences
dictionnaire_occurrences = {}