def arrondir_et_trier(liste):
    liste_arrondie = [int(nombre + 0.5) for nombre in liste]

    n = 0
    for _ in liste_arrondie:
        n += 1

    for i in range(n):
        for j in range(0, n - i - 1):
            if liste_arrondie[j] > liste_arrondie[j + 1]:
                liste_arrondie[j], liste_arrondie[j + 1] = liste_arrondie[j + 1], liste_arrondie[j]

    return liste_arrondie

ma_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
print("Liste de base :", ma_liste)

liste_arrondie_trie = arrondir_et_trier(ma_liste)


print("Liste arrondie et triée :", liste_arrondie_trie)
