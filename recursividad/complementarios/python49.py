print("Ejercicio 49.rp7")

n=int(input("Ingrese un numero "))
con=0

for i in range (2,n):
    if n%i==0:
        con=con+1

if con==0:
    print("Es numero primo")
else:
    print("No es numero primo")
