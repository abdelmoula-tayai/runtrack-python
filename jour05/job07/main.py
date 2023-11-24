def arrondir_notes(notes):
    notes_arrondies = []
    for note in notes:
        if note < 40:
            notes_arrondies.append(note)
        else:
            multiple_de_5_superieur = ((note + 4) // 5) * 5
            if multiple_de_5_superieur - note < 3:
                notes_arrondies.append(multiple_de_5_superieur) 
            else:
                notes_arrondies.append(note) 

    return notes_arrondies


notes_etudiants = [83, 76, 42, 68, 91, 57]
notes_arrondies = arrondir_notes(notes_etudiants)
print(notes_arrondies)
