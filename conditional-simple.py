print("1 rutina: Programa de evaluacion")

nota_alumno = input("Introduce la nota del añumno: ")

def evaluacion(nota):

	_valoracion="aprobado"

	if nota<5:

		_valoracion="suspenso"
	
	return _valoracion
	
print(evaluacion(int(nota_alumno)))

"""--------------------------------------------------------------"""

print("2 rutina: Verificación de acceso")

edad_usuario=int(input("Introduce tu edad: "))

if edad_usuario<18:

    print("No puedes pasar")

elif edad_usuario>100:

    print("Edad incorrecta")

else:
    
    print("Puedes pasar")

print("La rutina ha finalizado")

"""------------------------------------------------------------"""

print("3 rutina: Verificar nota alumno")

nota_alumno=int(input("Introduce tu nota, por favor: "))

if nota_alumno<5:

    print("Insuficiente")

elif nota_alumno<6: 

    print("Suficiente")

elif nota_alumno<7: 

    print("Bien")

elif nota_alumno<9:

    print("Notable")

else:

    print("Sobresaliente")

"""-----------------------------------------------------------"""

print("4 rutina: Analisis simple de una variable")

edad=7

if 0<edad<100:

    print("Edad es correcta")

else:

    print("Edad incorrecta")
