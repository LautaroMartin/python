print("Ejercicio r3")




#entrada
inicio=2
final=1000

cont=int(input())


#proceso
for i in range(inicio, final):
    primo=True
    j=2
    while (i>j) & (primo==True):
        if i%j==0:
            primo=False
            break
        else:
            j=j+1
    if primo==True:
        print (i, " es primo")
        cont=cont+1


#salida
print("\nSalida: ")
print("Entre ",inicio, " y ", final, " hay ", cont, "n° primos")
