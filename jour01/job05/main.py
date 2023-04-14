def Alphabet():
  return list(map(chr, range(97, 123)))

print (Alphabet())

for ReverseAlphabet in reversed(Alphabet()):
  print(ReverseAlphabet)