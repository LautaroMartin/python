print("Ejercicio vectores 2")

suma=0
media=0.0
c=0
temp=[]

n=int(input("Ingrese la cantidad e temperaturas: "))

for i in range(n):
	temperatura=float(input("Ingrese temperatura {0}:".format(i+1)))
	temp.append(temperatura)
	suma=suma+temp[i]
media=suma/n


for tempelement in temp:
	if tempelement>=media:
		c=c+1
		print(tempelement)


print("La media es de ", media)
print("Total de temperaturas >= a la medias es ", c)
