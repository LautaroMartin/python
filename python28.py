print("--------------------------------")
print("Ejercicio 28")
print("--------------------------------")



a = int(input("Ingrese a "))
b = int(input("Ingrese b "))
c = int(input("Ingrese c "))



if a>b:
	if a>c:
		if b>c:
			print(a,b,c)
		else:
				print (a,c,b)
	else:
		print(c,a,b)
else:
	if b>c:
		if a>c:
			print(b,a,c)
		else:
			print(b,c,a)
	else:
		print (b,c,a)