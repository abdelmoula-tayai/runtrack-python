L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

valeurs_intervalle = [nombre for nombre in L if 25 <= nombre <= 90]


produit_intervalle = 1
for nombre in valeurs_intervalle:
    produit_intervalle *= nombre

print(produit_intervalle)
