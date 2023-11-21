a = float(input("Entrez la longueur du côté a : "))
b = float(input("Entrez la longueur du côté b : "))
c = float(input("Entrez la longueur du côté c : "))

if a + b > c and a + c > b and b + c > a:
    print("Les longueurs saisies forment un triangle.")

   
    if a == b == c:
        print("C'est un triangle équilatéral.")
    elif a == b or a == c or b == c:
        print("C'est un triangle isocèle.")
        
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("C'est aussi un triangle rectangle isocèle.")
    else:
        print("C'est un triangle quelconque.")
else:
    print("Les longueurs saisies ne forment pas un triangle.")
