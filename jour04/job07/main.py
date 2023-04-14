L = [8, 24, 48, 2, 16]
long = len(L)
multiples = 0


for i in range(long):
    if L[i] % 3 == 0:
        multiples = multiples + 1

print(multiples)




