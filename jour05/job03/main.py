def draw_carpet(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                print(" ", end="")
            else:
                print("#", end="")
        print()


draw_carpet(10)
