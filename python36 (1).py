print("Ejercicio 36.c8")


#entrada

op = int(input ("Ingrese que quiere hacer (1 o 2)"))

if op==1:
    print("Eligio area de triangulo")
    i=float(input ("Ingrese el lado de triangulo"))
    a= ((3**0.5)/4)*i**2

    print("El area del triangulo es ", a)
    elif op==2:
        pi=3.1416
        print("Eligio area del circulo")
        r=float(input ("Ingrese el radio del circulo"))
        c=pi*r**2
    else:
        print("Error")
        