print("------------------------------------------------------");
print("Ejercicio 3: puntaje final");
print("------------------------------------------------------");

#entrada de datos
print("Ingrese el numero de respuestas correctas: ");
rc=int( input());
print("Ingrese el numero de respuestas incorrectas");
ri=int( input());
print("Ingrese el numero de respuestas en blanco");
rb= int( input());

#calculo de datos
pcr=rc*3;
pri=ri*-1;
prb=rb*0;
pf=pcr+pri+prb;

#final

print("El puntaje total es ", pf)