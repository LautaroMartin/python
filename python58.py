print("Ejercicio vectores 3")

VEC=[]

n=int(input("Ingrese numero de elementos del vector"))


if i<=n & n<=200:

	for i in range (1,n+1):
	elemento=int(input("Ingrese entero {0}: ". format(i) ))
	VEC.append(elemento)
	i=0

	for elemento in VEC:
		if elemento not in lista_nueva:
			lista_nueva.append(elemento)


	lista_nueva.sort()

print(lista_nueva)