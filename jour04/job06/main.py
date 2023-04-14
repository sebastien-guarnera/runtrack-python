quelconque = [5, 2, 3, 4, 1]

def liste():
    quelconque[0], quelconque[4] = quelconque[4], quelconque[0]
    print(quelconque)

liste()