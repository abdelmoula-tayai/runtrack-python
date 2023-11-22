def calcule (num1, operator, num2):
    if operator == "x":
     print (num1 * num2)
    elif operator == "/":
     print (num1 / num2)
    elif operator == "+":
     print (num1 + num2)
    elif operator == "%":
     print (num1 % num2)
    elif operator == "-":
     print (num1 - num2)

calcule (2, "x", 5)

calcule (2, "+", 5)

calcule (5, "-", 2)

calcule (5, "/", 2)

calcule (2, "%", 5)