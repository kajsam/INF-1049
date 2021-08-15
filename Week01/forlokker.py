# for og while-lokke

s = 0
for i in range(2,12): # starter pa 2 (0 default), opp til, ikke inkludert, 12
    s = s + i**2
    print("Sum sa langt:", s)
    print("La til", i**2)

print("Ferdig!")

x = 2
s = 0
i = 0

while i < 10:
    s = s + x**2
    print("Sum sa langt:", s)
    print("La til", x**2)
    x = x + 1
    i = i + 1

print("Ferdig!")