#se importa el paquete random para la generacion del array aleatorio.
import random
#Definimos la funcion menu que nos mostrara el menu en pantalla
def menu():	

    print ("\n Menu:")
    print ("\t 1 - Calculo de IMC")
    print ("\t 2 - Suma de dígitos")
    print ("\t 3 - Moviendo ceros")
    print ("\t 4 - Salir")

    #fin

#funcion de Indice de Masa Corporal
def IMC():
    #peticion de datos
    estatura = float(input('\n Introduce la estatura en metros: \n '))
    peso = float(input('\n Introduce el peso en kilos: \n '))
        
        #conversion a metros en caso de que el usuario no leyera el aviso
    if estatura > 100:
        estatura = estatura/100
        
    # calculo del IMC
    elevado = pow(estatura, 2)
    #debug
    #print ("\n", elevado,"\n")
    resultado = peso / elevado

    print ("Tu imc es:", resultado)

    #control de flujo para mostrar el texto a devolver
    if resultado <= 18.5:
        print ("Infrapeso")
    elif resultado <= 25.0:        
        print ("Normal")
    elif resultado <= 30:        
        print ("Sobrepeso")
    elif resultado > 30:        
        print ("Obeso")
    else:
        print ("datos correctos pls")
    #fin

#Suma de dígitos
def numeros():
    num = int(input('\n Introduce el numero final: \n '))
    #Nos aseguramos de que el cero se omite para empezar el bycle en 1
    num = num+1

    #generamos las listas
    listado = []
    lista = []

    #bucle FOR que se repetira tantas veces como numero se le ha indicado para poblar la lista
    for miaw in range(1, num):
        lista.append(miaw)
    listado.append(lista)
        
    #se muestran los datos mediante el habitual print
    print (lista)
    #se usa la funcion de python que nos suma todos los elementos de la lista sin necesidad de desglosarlos
    resultado_numeros = sum(lista)
    print ("\n Suma de los numeros es", resultado_numeros, "\n")

def ceros():
    #peticion al usuario
    numceros = int(input('\n Introduce un numero que sera la longitud del array: \n '))
    numceros = numceros+1
    #creamos el array con numeros aleatorios
    listadoceros = []
    listaceros = []
    
    #for para crear un array de numeros aleatorios
    for x in range(1, numceros):
        #generacion de los numeros aleatorios de 0 a 9
        listaceros.append((random.randint(0, 9)))
    listadoceros.append(listaceros)

    print ("\n Listado aleatorio original: \n", listaceros)
    movidos = sorted(listaceros, key=bool, reverse=True)

    print ("\n Numeros desplazados: \n",movidos,)

#Se genera un bucle infinito hasta que se termine el proceso con break o lo termine el usuario
while True:
    #Se genera el menu llamando a su funcion
	menu()    
    #Se espera la interaccion del usuario
	opcion = input("\n Selecciona la opcion deseada en tu teclado: \n ")
    #Se procede a declarar las opciones y las llamadas a sus funciones segun proceda
	if opcion == "1":
		IMC()
	elif opcion == "2":
		numeros()
	elif opcion == "3":
		ceros()
	elif opcion == "4":        
		print ("\n Bye!")
		break
	else:
		input("Por favor, pulsa una opcion valida \n")