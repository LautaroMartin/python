print("Ejercicio 10")

#entrada
pi = 3.1416
radio = float(input("Ingrese el radio "))
altura = float(input("Ingrese la altura del cilindro "))

#proceso
vol = pi*radio**2*altura
area = 2*pi*radio*(radio+altura)

#fin
print("El area del cilindro es de un total", area)
print("El voliumen total del cilindro es de", vol)