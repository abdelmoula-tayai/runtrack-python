L = [1, 2, 3, 4, 5]
print (L)
print(L[1])

def somme (liste):
    somme_voisine = liste[2] + liste[4]
    liste[3] = somme_voisine

somme (L)
print(L)

print (L[-1])