s = "abcdefghijklmnopqrstuvwxyz" * 10
n = 1
i = 0

while i < len(s):
    for j in range(n):
        if i >= len(s):
            break
        print(s[i], end=" ")
        i += 1
    print()
    n += 1



