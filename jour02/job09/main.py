a = 15
b = 15
c = 15

def triangle():
    if (a+b) > c and (a+c) > b and (b+c) > a:
        print("triangle")
    else:
        print("invalide")

triangle()

def quel_triangle():
    if a == b and b == c:
        print("équilatéral")
    elif a == b or b == c or c == a:
        print("isocèle")
    elif (a*a+b*b==c*c) or (b*b+c*c==a*a) or (a*a+c*c==b*b):
        print("rectangle")
    elif (a*a+b*b==c*c) or (b*b+c*c==a*a) or (a*a+c*c==b*b) and a == b or b == c or c == a:
        print("rectangle isocèle")
    else:
        print("quelconque")

quel_triangle()

