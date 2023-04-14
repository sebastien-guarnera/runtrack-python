L = "La peur est le chemin vers le côté obscur " \
    "la peur mène à la colère la colère mène à la haine la haine mène à la souffrance"
n = 3


def mots_longs(L, n):
    mots = L.split()
    mots_filtres = []
    for mot in mots:
        if len(mot) > n:
            mots_filtres.append(mot)
    return mots_filtres


mots = mots_longs(L, n)
print(mots)
