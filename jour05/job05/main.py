def chiffrement_cesar(message, decalage):
    resultat = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                resultat += chr((ord(char) - ord('A' if char.isupper() else 'a') + decalage) % 26 + ord('A' if char.isupper() else 'a'))
            else:
                resultat += chr((ord(char) - ord('A' if char.isupper() else 'a') + decalage) % 26 + ord('A' if char.isupper() else 'a'))
        else:
            resultat += char
    return resultat

message = "Hello, World!"
decalage = 3
message_chiffre = chiffrement_cesar(message, decalage)
print(message_chiffre)
