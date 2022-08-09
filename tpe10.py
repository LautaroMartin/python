print("Ejercicio complementario 10")
print("--------------------------------")

#entrada
x1 = float( input("Ingrese x1, y1 y z1 "))
y1 = float ( input())
z1 = float ( input())
x2 = float ( input("Ingrese x2, y2 y z2 "))
y2 = float ( input())
z2 = float ( input())

#proceso
dis = float (((z2-z1)**2+(y2-y1)**2+(x2-x1)**2)**0.5)

#salida
print("La distnacia es de:", dis)