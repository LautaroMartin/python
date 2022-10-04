print("Ejercicio 50.rc8")



n=int(input("Ingrese la cantidad de numeros a evaluar "))
c=0

for i in range(1,n+1):
    num=int(input("Ingrese numero "))
    if num==0:
        c=c+1


print("Hay ", c, " numeros ceros")
