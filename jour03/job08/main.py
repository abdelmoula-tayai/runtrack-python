def aliments (type, saison):
    if type == "fruits" and saison == "hiver":
        print ("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "été":
        print ("Poire, fraise, cassis")
    elif type == "légumes" and saison == "hiver":
        print ("carotte, topinambour, endive")
    elif type == "légumes" and saison == "été":
        print ("artichaut, aubergine,navet")
    else:
        print ("veullez entrez un type (fruits ou légumes) et/ou une saison valide (hiver ou été)")

aliments ("fruits", "hiver")

aliments ("fruits", "été")

aliments ("légumes", "hiver")

aliments ("légumes", "été")

aliments ("légumes", "automne")

aliments ("kebab", "hiver")
