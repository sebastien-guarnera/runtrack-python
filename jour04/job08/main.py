L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
long = len(L)
somme = 0

for i in range(long):
    if i % 2 == 0:
        somme = somme + L[i]

print(somme)