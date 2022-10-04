import string


print("Prueba 10/04/22")

vec=[]
vec.append("caballo")
vec.append("gallina")
vec.append("sariguella")



opc=int(input("Ingrese 1 para añadir elementos, 2 para eliminar, 3 para buscar los elementos del vector y 4 para ordenar el vector "))
if(opc==1):
    print("Eligio Añadir")

    for i in range(3,6):
        lugar=input("Ingrese el animal{}: " .format(i+1))
        vec.append(lugar)

elif (opc==2):
    print("Eligio eliminar")

    print("Ingrese 0 para terminar, o borre el vector completo (6 elementos)")
    opc2=1
    while (opc2>=1):
        print("Elemento a borrar ")
        delete=(input())
        vec.remove(delete)
        opc2=int(input("¿Continuar?(0=no o 1+=si)"))

elif (opc==3):
    print("Eligio busqueda")
    nombre=input("Ingrese el animal buscado ")
    for j in range (3):
        if vec[j]== nombre:
            if (j==0):
                 print("El animal que busca tiene como vecino a su derecha")
                 print(vec[j+1])
            elif (j==3-1):
                print("El animal que busca tiene como vecino a su izquierda")
                print(vec[j-1]) 
            else:
                print("El animal que busca tiene como vecino a su derecha")
                print(vec[j+1]) 
                print("El animal que busca tiene como vecino a su izquierda")
                print(vec[j-1]) 
elif (opc==4):
    print("Eligio ordenar")
    vec.sort()
    for b in range (3):
        print(vec[b])






