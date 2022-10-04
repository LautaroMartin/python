print("Ejercico r2")



#entrada
num=int(input("Ingrese un numero positivo para iniciar el programa"))


#proceso
while num>0:
    suma=0
    for i in range (1,num+1):
        if num%i==0:
            Suma=suma+1
    print("La suma de los divisores es: ", Suma, "\n")
    print("Ingresa otro numero, si quieres terminar ingresa uno negativo")
    
