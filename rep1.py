print("Ejercicio r1")




#entrada
c=-1
i=0
m=0

while (c<0 or (i<=0) or i>=100 or (m<=0)):
    print ("Introduce el capital, interes y el tiempo correspondientes")
    c=int(input("Capital "))
    i=int(input("Interes "))
    m=int(input("Tiempo en años "))

#proceso
for  i in range(m):
    c=c*(1+i/100)


#salida
print("Tienes ", c, " pesos")
