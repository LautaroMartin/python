print("Ejercicio complementario 8")
print("----------------------------")

#entrada
vela = float( input("Ingrese la velodcidad del primer cuerpo: "))
velb = float( input("Ingrese la velocidad del segundo cuerpo: "))
dis = float( input("Ahora ingrese la distancia entre ambos cuerpos: "))

#proceso
t = dis/(vela+velb)

#salida
print("La colision ocurrira en ",t)