print("Ejercicio 53.rc11")

i=0
c=0
numentradas=10

print("Ingrese ", numentradas, "Numeros: ")
while i<=numentradas:
	n=int(input("Ingrese numero: ")):
	if n%2==0:
		c=c+1

	i=i+1

print ("En", numentradas, "números enteros hay", c, "números pares")
