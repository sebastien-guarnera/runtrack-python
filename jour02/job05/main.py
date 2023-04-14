num1 = 56
operator = "*"
num2 = 65

def calcule():
    if operator == "+":
        print(num1+num2)
    elif operator == "-":
        print(num1-num2)
    elif operator == "/":
        print(num1/num2)
    elif operator == "*":
        print(num1*num2)
    elif operator == "%":
        print(num1%num2)
    else:
        print("null")

calcule()


