print("------------------------")
print("Ejercicio 33.c5")
print("------------------------")

#entrada
vel1=float(input("Ingrese la velocidad del primer auto"))
vel2=float(input("Ingrese la velocidad del segundo auto"))
t=float(input("Ingrese el tiempo"))
d=float(input("Ingrese la distancia que los separa"))


#proceso
if vel1>0 & vel2>0:
    t=d/(vel1+vel2) 
    print("El tiempo de encuentro es de: ", t)
else:
    print("Ingrese de vuelta los numero en caso de una operaccion erronea")
    
