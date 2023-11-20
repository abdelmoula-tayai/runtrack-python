montant_initial = 10000
taux_rendement = 5
gain = (taux_rendement/100)*montant_initial
print("gain annuel = {}€" .format(gain))
montant_initial += 5000
taux_rendement += 2
gain = (taux_rendement/100)*montant_initial
print("gain annuel = {}€" .format(gain))

montant_initial = montant_initial - (montant_initial * 30/100)
taux_rendement = taux_rendement - (taux_rendement * 1/100)
gain = (taux_rendement/100)*montant_initial
print("gain annuel = {}€" .format(gain))