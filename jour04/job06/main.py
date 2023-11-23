L = [1, 2, 3, 4, 5]
print (L)

def echange (liste):
    liste[0], liste[-1] = liste[-1], liste[0]

echange(L)
print(L)