
print("Hei")

print("[0] AND [1] ->".format(True, True, True and True))

n = 0
n_sum = 0

while n < 10 and n_sum < 46:
    n_sum = n_sum + n
    n = n + 1

print(n, n_sum)

# buelengde

from math import radians, asin, sin, cos, sqrt

coordinates = [
    ["Tromso", 69.6489, 18.95508],
    ["Trondheim", 63.43049, 10.39506],
    ["Oslo", 59.91273, 10.74609]
]

R = 6372.8 # Radius of earth in km

for first_city in coordinates:
    for second_city in coordinates:

        # if first_city != second_city:
        if first_city == second_city:
            continue

        dlat = radians(first_city[1] - second_city[1])
        dlon = radians(first_city[2] - second_city[2])
        lat1 = radians(first_city[1])
        lat2 = radians(second_city[1])

        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        d = R * 2 * asin(sqrt(a))

        print("Dist from ", first_city[0], "to", second_city[0], "is", d, "km")
    print()