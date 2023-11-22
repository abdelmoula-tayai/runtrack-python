def pair_impaire (num):
     if isinstance(num) and num >= 0:
        if num % 2 == 0:
            print (num, "est un nombre pair")
        else:
            print(num, "est un nombre impaire")
     else:
         print("veuillez entrez un nombre entier positif")



pair_impaire(2)
pair_impaire(5)
pair_impaire(-2)
