print("--------------------------------------")
print("Ejercicio 36.c8")
print("--------------------------------------")

#entrada
pi=3.1416
print("1 es para el triangulo y 2 es para el circulo ")
opc=int(input("Ingrese opc: "))

#proceso
if opc==1:
    print("Area del triangulo ")
    print("Ingrese el area del triangulo ")
    l=float(input())
    a=((3**0.5)/4)*l**2
    print("El area del triangulo es ", a)

elif opc==2:
    print("Area del circulo ")
    print("Ingrese el radio del circulo ")
    r=float(input())
    c=pi*r**2
    print("El area del circulo es de ", c)
        