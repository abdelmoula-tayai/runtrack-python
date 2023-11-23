def supprimer_doublons(liste):
    sans_doublons = []
    for element in liste:
        if element not in sans_doublons:
            sans_doublons.append(element)
    return sans_doublons

ma_liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

ma_liste_sans_doublons = supprimer_doublons(ma_liste)

print(ma_liste_sans_doublons)

