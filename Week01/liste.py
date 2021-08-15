
l = [6, 7, 8, 9, 10, 12]

print(l) # hele lista
print("index 0 er forste element:", l[0]) # index 0
print("index 1:", l[1]) # index 1
print(l[3:]) # fra index 3 og ut
print(l[:2]) # fra start til (ikke med) 2
print(l[2:4])

l.append(190) # legger til 190 bakerst
l.remove(8) # fjerne forste forekomst av 8

print(l)

# l.remove(3) # error: not in list

for i in range(0,3):
    l.append(8)

print(l)

print("lista er", len(l), "lang")

while 8 in l:
    l.remove(8)

print(l)

print("na er lista", len(l), "lang")

while len(l) > 1:
    l.pop()

print(l)

print("tilslutt er lista", len(l), "lang")

C_liste = []
F_liste = []

for C in range(-20, 21, 5): # steps by 5
    F = 9/5*C + 32
    C_liste.append(C)
    F_liste.append(F)

print(C_liste, F_liste)

for i in range(0, len(C_liste)):
    print("C = ", C_liste[i], "F = ", F_liste[i])