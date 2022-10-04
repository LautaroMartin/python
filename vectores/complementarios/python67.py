print("Ejercicio complementario vectores 6")

v1=[]


n=int(input("Ingrese la cantidad de elementos del vector: ")

print("Ingrese los valores del vector")

for x in range(n):
	valor=int(input("v{}:".format(x+1)))
	v1.append(valor)
	
print("Los elementos del vector son: ")

for y in range(n):
	for x in range(n-1):
		if v1[x]<v1[x+1]:
			m=v1[x]
			v1[x] = v1[x+1]
			v1[x+1] = m
			
			
print(v1)
