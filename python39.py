print("Ejercicio 38.r3")


#entrada

uno=2
fin=1000

cont=0

#proceso


for i in range (uno, fin):
    primo=True
    j=2


while (i>j) and (primo==True):
    if i%j==0:
        primo=False
        break
    else:
        j=j+1

if primo==True:
    print(i, " Es primo")
    Cont=cont+1

#salida

print("Entre los numeros ",uno, " y ", fin, " hay ", Cont, " n° primos")