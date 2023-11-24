def distance_to_toilettes(marches, hauteur):
    distance_jour = (marches * hauteur * 2) / 100  # En mètres
    distance_semaine = distance_jour * 7
    return distance_semaine

# Exemple d'utilisation avec 50 marches de 20 cm
marches = 50
hauteur = 20
distance_totale = distance_to_toilettes(marches, hauteur)

# Affichage du résultat
print(f"Pour {marches} marches de {hauteur} cm, le gardien parcourt {distance_totale:.2f} m par semaine.")
