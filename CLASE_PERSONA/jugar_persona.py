from persona import  Persona

print("")
print("Proves mab la classe Persona implementada a partir del llibre 'Aprende a programar con PYTHON")

def menu():
    print("")
    print("-------------------------------------------------")
    print("1.Inicialitzar dades del objecte.")
    print("2.Imprimir dades associades al objecte.")
    print("3.Canviar valor d'un atribut.")
    print("4.Obtenir el valor d'un atribut.")
    print("0.Sortir")
    print("-------------------------------------------------")
    print("")

def menu2():
    print("")
    print("-------------------------------------------------")
    print("1.Atribut EDAD")
    print("2.Atribut NOM")
    print("3.Atribut DNI")
    print("-------------------------------------------------")
    print("")

sortir = True
miquel = Persona()
while(sortir):
    menu()
    opcio =int(input("Intorduiex la opció: "))
    print("")
    if opcio == 0:
        print("Sortim del programa.\n")
        sortir = False
    elif opcio == 1:
        print("Opció inicialitzar dades del objecte.\n")
        miquel.inicialitzar_Dades()
    elif opcio == 2:
        print("Opció imprimir dades associades al objecte.\n")
        miquel.imprimir_Dades()
    elif opcio == 3:
        print("Canviar valor d'un atribut.")
        menu2()
        opcio2 =int(input("Intorduiex la opció: "))
        print("")
        if opcio2 == 1:
            print("Canviam valor atribut EDAD.\n")
            valor = input("Nou valor: ")
            miquel.set_edad(valor)
        elif opcio2 == 2:
            print("Canviam valor atribut NOM.\n")
            valor = input("Nou valor: ")
            miquel.set_nom(valor)
        elif opcio2 == 3 :
            print("Canviam valor atribut DNI.\n")
            valor = input("Nou valor: ")
            miquel.set_DNI(valor)
        else:
            print("Opció no vàlida.")
    elif opcio == 4: 
        print("Canviar valor d'un atribut.")
        menu2()
        opcio2 =int(input("Intorduiex la opció: "))
        print("")
        if opcio2 == 1:
            print("Obtenim valor atribut EDAD.")
            print(miquel.get_edad())
        elif opcio2 == 2:
            print("Obtenim valor atribut NOM.")
            print( miquel.get_nom())
        elif opcio2 == 3 :
            print("Obtenim valor atribut DNI.")
            print(miquel.get_DNI())
        else:
            print("Opció no vàlida.")
    else: 
        print("Opció no vàlida.")









