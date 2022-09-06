print("Ejercicio complementario vectores 9")

animal=[]


tamarray=int(input("Ingresar dimension del array: "))

print("Ingrese los nombres de los animales ")

for x in range(tamarray):
	elemento=input("Ingrese animal{}:".format(x+1))
	animal.append(elemento)
	nombre=input("Ingrese el animal buscado: ")
	print("El animal tiene como vecino a: )
	for x in range(tamarray):
		if animal[x]==nom:
			if x==0:
				print(animal[[x+1])
			elif x==tamarray-1:
				print(animal[x-1])
			else:
				print(animal[[x+1])
				print(animal[x-1])