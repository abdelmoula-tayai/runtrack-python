def my_long_word(longueur_min, phrase):
    mots = []
    mot_actuel = ""
    for caractere in phrase:
        if caractere.isalpha():
            mot_actuel += caractere
        elif mot_actuel:
            nb_caracteres = 0
            for _ in mot_actuel:
                nb_caracteres += 1
            if nb_caracteres > longueur_min:
                mots.append(mot_actuel)
            mot_actuel = ""
    if mot_actuel:
        nb_caracteres = 0
        for _ in mot_actuel:
            nb_caracteres += 1
        if nb_caracteres > longueur_min:
            mots.append(mot_actuel)
    return " ".join(mots)

resultat = my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")
print("Output :", resultat)


resultat = my_long_word(4, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")
print("Output :", resultat)



