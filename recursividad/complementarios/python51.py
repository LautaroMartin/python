print("Ejercicio 51.rc9")


limite=int(input("Ingrese la cantidad de numeros a comparar"))
n=int(input("Ingrese el numero"))



men=n
may=n


for i in range (1,lim):
    n=(input("Ingrese numero "))

    if n<men:
        men=n
    else:
        if n>may:
            may=n



print("El numero mayor es: ",men)
print("El numero menor es: ", may)
