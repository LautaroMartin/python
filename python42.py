print("Ejercicio 42.r6")


#entrada


a1=1
a2=0
an=a1+(2*a2)
cont=0

#proceso


while   an<300:
    a2=a1
    a1=an
    an=a1+(2*a2)
    cont=cont+1


#salida


print("El rango es ", cont, " y el resultado es ", an)
