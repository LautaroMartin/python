print("Ejercicio complementario vectores 5")



valor=[]

m=int(input("Ingrese el numero de elementos del array"))

print("Ingrese los el del array")
for i in range (m):
	elemento=int(input("Ingrese elemento: "))
	valor.append(elemento)
	
	
bus=int(input("Ingrese el valor a buscar: "))

print("La posicion del valor sera: ")
for i in range(m):
	if valor[i]==bus:
		r=i
		print("La posicion del elemento es ", r+1)
		break
		
