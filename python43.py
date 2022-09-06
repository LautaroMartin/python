print("Ejercicio 43.rc1")


#entrada
c=0


#proceso


for i in range(1,10+1):
    num=int(input("Ingrese Numero"))
    if num%2==0:
        c=c+1


print("Hay ", c , " pares")