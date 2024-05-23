import random

# Lecture du fichier mot.txt
with open('mot.txt', 'r', encoding='utf-8') as fichier:
    mots = fichier.read().splitlines()

# Initialisation du dictionnaire des occurrences
dictionnaire_occurrences = {}

# Parcourir chaque mot dans la liste de mots
for mot in mots:
    # Parcourir chaque lettre du mot, sauf la dernière
    for i in range(len(mot) - 1):
        lettre_actuelle = mot[i]
        lettre_suivante = mot[i + 1]

        # Initialiser le sous-dictionnaire si nécessaire et incrémenter le compteur
        dictionnaire_occurrences.setdefault(lettre_actuelle, {}).setdefault(lettre_suivante, 0)
        dictionnaire_occurrences[lettre_actuelle][lettre_suivante] += 1


# Construction de la table des probabilités
table_probabilites = {}
for lettre_actuelle, lettres_suivantes in dictionnaire_occurrences.items():
    total_occurrences = sum(lettres_suivantes.values())
    table_probabilites[lettre_actuelle] = {lettre_suivante: compte / total_occurrences 
                                           for lettre_suivante, compte in lettres_suivantes.items()}