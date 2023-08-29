print("1 rutina: analisis de salarios logicos")

salario_presidente = int(input("Introduce salario presidente: "))

print("Salario presidente: " + str(salario_presidente))

salario_director = int(input("Introduce salario director: "))

print("Salario director: " + str(salario_director))

salario_jefe_area = int(input("Introduce salario Jefe Área: "))

print("Salario jefe de area: " + str(salario_jefe_area))

salario_administrativo = int(input("Introduce salario administrativo: "))

print("Salario administrativo: " + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    
    print("TODO FUNCIONA CORRECTAMENTE")

else:

    print("NO FUNCIONA CORRECTAMENTE")

"""----------------------------------------------------------------------------"""

print("2 rutina: Programa de becas")

distancia_escuela = int(input("Introduce la distancia a la escuela en km: "))

print(distancia_escuela)

numero_hermanos=int(input("Introduce el numero de hermanos en el centro"))

print(numero_hermanos)

salario_familiar = int(input("Introduce el salario anual bruto"))

print(salario_familiar)

if (distancia_escuela>40 and numero_hermanos>2) or salario_familiar<=20000: 

    print("Tienes derecho a beca")

else:

    print("No tienes derecho a beca")
 