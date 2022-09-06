print("Ejercicio 48.rc6")



aux=0
aux2=0

n=int(input("Ingrese un numero "))
i=10

while i<=n:
    aux=n%10
    n=n//10
    aux2=aux2*10+aux

aux2=aux2*10+n

print("El numero invertido es ", aux2)

