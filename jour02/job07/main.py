chaine = "abcdefghijklmnopqrstuvwxyz" * 10
index = 1
print(chaine[0])
for i in range(1, len(chaine), 2):
    ligne = ""
    for j in range(0, i + 2):
        if index < len(chaine):
            ligne += chaine[index]
            print(chaine[index], end="")
            index += 1
    if ligne:
        print(ligne)