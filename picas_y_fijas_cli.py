from colorama import init, Fore, Style #libreria para utilizar colores en los print y hacer más facil la lectura
import random, msvcrt
init() #inicialización de colorama

def juego(intento,dificultad):
        nombre=input(Fore.RED + "Robot:" + Style.RESET_ALL +" Cual es tu nombre ? ... ")
        print(Fore.RED + "Robot:" + Style.RESET_ALL + " Estas son las reglas del juego Picas y Fijas... ")
        print("1. He seleccionado un número de 4 cifras.")
        print("2. Los 4 números son diferentes, es decir, el numero 1231, no es una opción luego que el número 1 se repite.")
        print("3. Tiene " + str(dificultad) +" intentos para adivinar el número que seleccione.")
        print("4. Con cada turno dare pistas basado en que tan cerca has estado de adivinar el numero, por ejemplo,")
        print("si mi número seleccionado es el '1234', y en tu intento tu dices el número '9253', te dire que tienes: ")
        print("1 FIJA (que corresponde a que el número '2' esta en el lugar correcto) y 1 PICA (que corresponde a que el 3 está, pero no en esa posición)")
        print("Algo que no te dire es cúal de los números has acertado, por tanto para el ejemplo anterior te dire: 'Tienes 1 FIJA y 1 PICA' ")
        print(Fore.RED + "-Robot:" + Style.RESET_ALL + " Empecemos "+ nombre +", dime cúal crees que es mi número? ")

        fijas = 0
        picas = 0
        num_robot = [] # lista donde se guardara el numero seleccionado aleatoriamente
        while len(num_robot) < 4:
            numero = random.randint(0, 9) #condiciona que sean numeros del 0 al 9
            if numero not in num_robot: #condiciona que no se repita ningun numero
                num_robot.append(numero)
                
        registro_intentos = [] #lista de los intentos realizados por el jugador
        for i in range(dificultad):
            if i == dificultad - 1:
                 print(Fore.RED + "--- PIENSALO BIEN ESTE ES EL ULTIMO INTENTO!!! --- " + Style.RESET_ALL)
            intento=input(Fore.YELLOW +">"+ nombre +": " + Style.RESET_ALL)
            while not intento.isdigit() or len(intento) != 4 or len(set(intento)) != 4:
                print(Fore.RED + "El número ingresado no es válido. Debe ser un número de 4 dígitos sin números repetidos." + Style.RESET_ALL)
                intento=input(Fore.YELLOW +">"+ nombre +": " + Style.RESET_ALL)

            registro_intentos.append(intento)  #guarda el intento en la lista de intentos
            
            lista_intento = list(intento) #convierte el intento en una lista con el fin de comparar con lista del numero del robot
            lista_intento = [int(elemento) for elemento in lista_intento] #convierte de str a int los elementos de la lista
            
            if num_robot == lista_intento: #comparación de las listas
                print(Fore.RED + "-Robot: " + Style.RESET_ALL + " GANASTE !!! ")
                print("Presiona una tecla para volver al menu... ")
                msvcrt.getch()
                menu()
            else:
                 for numero in lista_intento: #ciclo para control del numero de intentos
                    if numero in num_robot: #comparación de cada numero para determinar fijas y picas
                        posicion1 = lista_intento.index(numero)
                        posicion2 = num_robot.index(numero)
                        if posicion1 == posicion2:
                             fijas = fijas + 1                          
                        else:
                             picas = picas + 1
            print(Fore.RED + "-Robot:" + Style.RESET_ALL + " Fijas: " + str(fijas) + " Picas: " + str(picas) + " --- Intento #"+ str(i+1))
            if i+1 == dificultad:
                print(Fore.RED + "-Robot: " + Style.RESET_ALL + " Perdiste, intentalo de nuevo !!! ")
                print(Fore.RED + "-Robot: " + Style.RESET_ALL + " Mi número era: " + str(num_robot))
                print("Presiona una tecla para volver al menu... ")
                msvcrt.getch()
                menu()

            fijas = 0
            picas = 0
def menu():
    print (Fore.GREEN + "########################## ")
    print ("### Menu Picas y Fijas ###")
    print ("### 1. Jugar           ###")
    print ("### 2. Dificultad      ###")
    print ("### 3. Salir           ###")
    print ("##########################")

    opcion=input(Fore.RED + "-Robot:" + Style.RESET_ALL + " Que opción desea? ... ")

    if opcion.isdigit and opcion >= "1" and opcion <= "3":
        if opcion == "1":
            juego(0000,10)

        if opcion == "2":
                print (Fore.GREEN + "###################################")
                print ("### Dificultad:                 ###")
                print ("### 1. Facil (20 intentos)      ###")
                print ("### 2. Intermedio (10 intentos) ###")
                print ("### 3. Dificil (5 intentos)     ###")
                print ("###################################")               
                dif=input(Fore.RED + "-Robot:" + Style.RESET_ALL + " Que dificultad desea? ... ")

                while not dif.isdigit() or dif > "3" or dif <= "0":
                        print(Fore.RED + "Opción invalida, seleccione una opción del 1 al 3" + Style.RESET_ALL)
                        dif=input(Fore.RED + "-Robot:" + Style.RESET_ALL + " Que dificultad desea? ... ")

                if dif == "1":
                        print (Fore.GREEN + "Intentos permitidos = 20")
                        juego(0000,20)
                if dif == "2":
                        print (Fore.GREEN + "Intentos permitidos = 10")
                        juego(0000,10)
                if dif == "3":
                        print (Fore.GREEN + "Intentos permitidos = 5")
                        juego(0000,5)
        if opcion == "3":
                print (Fore.GREEN + "Adios! ")
    else:
            print (Fore.RED + "!!! Opción incorrecta !!!")
            menu()
menu()