print("Ejercicio complementario vectores 8")

vec=[]

tamvec=int(input("Ingrese dimension del vector: "))

pares=tamvec*[0]
impares=tamvec*[0]

print("Ingrese los ",tamvec," valores del vector")
for x in range(tamvec):
	elemento=int(input("Elemento{}:".format(x+1)))
	vec.append(elemento)
	
	vpr=0
	i=0
	
	for x in range(tamvec):
		if vec[x]%2==0:
			pares[vpr]=vec[x]
			vpr=vpr+1
		else:
			impares[i]=vec[x]
			i=i+1
	
print(pares[0:vpr])
print("El vector de pares tiene ",vpr," elementos")

print(impares[0:i])
print("El vector de impares tiene ",i," elementos")

if vpr>i:
	print("El vector de pares es mas grande")
elif vpr<i:
	print("El vector de imparres es mas grande")
else:
		print("Los 2 vectores son iguales en tamaño")
