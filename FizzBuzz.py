print(25*"-", "Bienvenidos a FizzBuzz", 25*"-")

num1 = input("Ingrese un numero del 1 al 100")
num1 = int(num1)
print("El numero escogido es:", num1)
for num2 in range(1, num1 + 1):
    if num1 > 100:
        print(num1, "no esta entre 1 y 100")
        break
    elif num2 % 3 == 0:
        print("fizz")
    elif num2 % 5 == 0:
        print("buzz")
    elif num2 % 3 and num2 % 5 == 0:
        print("fizzbuzz")
    else:
        print(num2)
print(".")
print(".")
print(".")
print(".")
print(".")
print("EXIT")