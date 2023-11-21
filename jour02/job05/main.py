for entier in range (1, 101):
    if entier % 3 == 0:
     print("Fizz")
    elif entier % 5 == 0:
     print("Buzz")
    elif entier % 3 == 0 and entier % 5 == 0:
     print("FizzBuzz")
    else:
     print(entier)