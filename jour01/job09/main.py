produit = "bouteille d'eau"
prix = 1
stock = 15
print ("{} {} stock {}" .format(produit, prix, stock))
achat = int(input("combien de bouteille souhaiter vous acheter "))
if achat <= stock:
    stock -= achat
    print("Achat effectué avec succès ! Nouveau stock : {} bouteilles.".format(stock))
else:
    print("Stock insuffisant. Achat non effectué.")

prix = prix*1.1
print ("{} nouveau prix {} stock {}" .format(produit, prix, stock))
