min = 0
max = 1001

for i in range(min, max):
   if i > 1:
       for n in range(2, i):
           if (i % n) == 0:
               break
       else:
           print(i)