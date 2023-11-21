while True:
        N = int(input("veuillez saisir un entier supérieur a zéro (N) :"))
        if N > 0:
            break
        else:
            print("veuillez saisir un entier supérieur a 0")

for i in range (1, N+1):
        print(f"\ntable de multiplication de {i} :\n")
        for j in range (1, 11):
            print(f"{i} X {j} = {i * j}")