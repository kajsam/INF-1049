
tromso = open("tromso-sunhours.csv", "r")

# print(tromso) # didn't work

dager_tromso = []

for line in tromso:
    dager_tromso.append(round(float(line)/60, 2)) # need to add float, 2 decimals

for i in range(0, len(dager_tromso)):
    print("Dag", i+1)
    print("Tromso:", dager_tromso[i])
    print()