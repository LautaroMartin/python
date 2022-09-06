print("Ejercicio complementario vectores 7")


v=[]

print("Ingrese los 10 valores del vector: ")
for i in range(10): 
	valor=int(input("valor{}:".format(i+1)))
	v.append(valor)
	
valor11=int(input("Ingrese valor a insertar: "))
v.append(valor11)

for x in range(11):
	for y in range(10):
		if v[y]>v[x]:
			a=v[y]
			v[y]=v[x]
			v[x]=a
			
			
for x in range(11):
	print(v[x])