print("Ejercicio matrices 2")

A = []

N = int( input("Ingrese dimensiones del arreglo "))



if 1 <= N and N <= 100:

	for i in range(N):
		A.append( [] ) 
		for j in range(N):
			elemento = input( "A{}{}: ".format(i, j) )
			A[i].append( int(elemento))
	BAND = True
	i = 0
	while i < N and BAND == True:
		j = 0
		while j < i-1 and BAND == True:
			if A[i][j] == A[j][i]:
				j = j + 1
			else:
				BAND = False
		i = i + 1
	if BAND:
		print("SI ES SIMÉTRICA")
	else:
		print("NO ES SIMÉTRICA")
else:
	print("La dimensión de la matriz no es correcta.")
