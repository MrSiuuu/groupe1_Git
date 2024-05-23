# Fonction pour générer un mot basé sur la table de probabilités
def generer_mot(table_probabilites, longueur_max=10):
    mot = random.choice(list(table_probabilites.keys()))
    while len(mot) < longueur_max:
        lettre_actuelle = mot[-1]
        if lettre_actuelle in table_probabilites:
            lettre_suivante = random.choices(
                list(table_probabilites[lettre_actuelle].keys()),
                list(table_probabilites[lettre_actuelle].values())
            )[0]
            mot += lettre_suivante
        else:
            break
    return mot
