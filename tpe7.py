import math
print("Ejercicio complementario 7")
print("----------------------------")

#entrada
pi = 3.1416
b = float( input("Ingrese el primer lado del triangulo: "))
c = float( input("Ingrese el segundo lado del triangulo: "))
alfa = float( input("\n Ingrese el angulo del triangulo en grados sexadesimales: "))

#formula
a= float((b**2+c**2-22*b*c*math.cos(alfa*pi/180))**0.5)

#salida
print("El lado es: \n", a)