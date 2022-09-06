print("Ejercicio matrices 1")

a=[]
b=[]
c=[]


print("Ingrese la dimension de la matriz, hasta un maximo de 100")
s=int(input("Numero de filas "))
r=int(input("Numero de columnas "))


for i in range(s):
	a[i].append([])
	b[i].append([])
	c[i].append([])
	for j in range(r):
		a[i].append(int(input("A{}{}:".format(i+1,j+1))))
		b[i].append(int(input("B{}{}:".format(i+1,j+1))))
		c[i].append( a[i][j]+b[i][j])

print(a)
print(b)
print(c)
