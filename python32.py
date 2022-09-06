print("--------------------------------")
print("Ejercicio 32")
print("--------------------------------")

print("Ingrese la fecha: ")
año=int(input("Ingrese el año "))
mes=int(input("Ingrese el mes "))
dia=int(input("Ingrese el dia "))

if dia>0 and dia<30 :
	print("El dia es ", dia+1)
	print("\nDel mes de ", mes)
	print("\nDel año de ", año)
elif mes>0 and mes<12 :
	print("1")
	print("\nEl mes es ", mes+1)
	print("\nDel año de ", año)
else:
	print("1")
	print("1")
	print(año+1)