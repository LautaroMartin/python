print("Ejercicio complementario vectores 1")



V1=3*[0]
V2=[0]*3

for i in range(3):
	V1[i]=int(input("v1({}): ".format(i+1)))


for i in range (3):
	V2[i]=int(input("v2({}): ".format(i+1)))


sum=0

for i in range (3):
	p= v1[i]*v2[i]
	sum=sum+p

print("El producto escalar es: ", sum)
x = V1[1]* V2[2] - V1[2]* V2[1]
y = -( V1[0]* V2[2] - V1[2]* V2[0] )
z = V1[0]* V2[1] - V1[1]* V2[0]
print("El producto vectorial es: {}i {}j {}k".format(x, y, z))