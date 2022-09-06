print("Ejercicio 38.r2")

#entrada
i=0

print("Ingrese numeros enteros positivos, para terminar ingrese uno negativo")
num=int(input())


#poceso
while  (num>0):
    suma=0
    for i in range (1, num+1):
        if num%1==0:
            suma=suma+i


#salida
print("La suma de los divisores del numero es ", suma)
