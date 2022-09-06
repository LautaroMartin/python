print("--------------------------------")
print("Ejercicio 31")
print("--------------------------------")


costo=float(input("Ingrese el costo del articulo "))
print("Ingrese la marca del producto ")
marca=input()


if (costo>=2000) & (marca=="NOSY"):
	pa=costo*0.90
	pt=pa*0.95
	print("El monto a pagar es de un total de ", pt, " pesos")
	
elif(costo>=200) & (marca!="NOSY"):
	pt=costo*0.90
	print("El monto a pagar es de un total de ", pt, " pesos")

elif (costo<2000) & (marca=="NOSY"):
	pa=costo*0.95
	pt=pa+pa*0.20
	print("El monto a pagar es de un total de ", pt, " pesos")
	
elif(costo<2000) & (marca!="NOSY"):
	pa=costo*1.20
	print("El monto a pagar es de un total de ", pt, " pesos")