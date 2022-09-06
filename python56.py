print ("Ejercicio 56, vectores 1")

i = 1
F = [] 

numElementos = int( input("Ingrese Número de elementos a Ingresar: "))

while i <= numElementos:
	elemento = int( input("Ingrese Elemento: "))
	F.append(elemento)
	i = i + 1

print("salida: ")

print(F)