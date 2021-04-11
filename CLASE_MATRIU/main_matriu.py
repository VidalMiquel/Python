from matriu import Matriu


def menu():
    print("----------------------------------------------------")
    print("0.Sortir del programa.")
    print("1.Sumar matrius.")
    print("2.Restar matrius.")
    print("3.Trasposada.")
    print("4.Imprimir infromació associada a la matriu.")

    print("---------------------------------------------------- \n")


print("")
print("--------------------Problema de matrius-----------------------\n")

sortir = True
B = Matriu(2, 2)

print("Inicialitam la matriu.\n")
x = int(input("Numero de files: "))
y = int(input("Numero de columnes: "))
joc = Matriu(x, y)
print("\n")
joc.toString()
print("\n")

while sortir:
    menu()
    opcio = int(input("Introdueix la opció a realitzar: "))
    print("")
    if opcio == 0:
        print("Sortim del programa, ADEU!\n")
        sortir = False
    elif opcio == 1:
        print("Sumam les matrius A i B\n")
        print("Matriu A \n")
        joc.toString()
        print("Matriu B \n")
        B.toString()
        joc.sumarMatrius(B)
        print("Resultat: \n")
        joc.toString()
    elif opcio == 2:
        print("Restam les matrius A i B\n")
        print("Matriu A \n")
        joc.toString()
        print("Matriu B \n")
        B.toString()
        joc.restarMatrius(B)
        print("Resultat: \n")
        joc.toString()
    elif opcio == 3:
        print("Calculam la trasposada de la matriu\n")
        print("Matriu A \n")
        joc.toString()
        joc.trasposada()
        print("")
        print("Matriu resultant: \n")
        joc.toString()
    elif opcio == 4:
        print("Multiplicam les matrius A i B\n")
        print("Matriu A \n")
        joc.toString()
        print("Matriu B \n")
        B.toString()
        joc.multiplicar(B)
        print("Resultat: \n")
        joc.toString()
    else:
        print("Opció introduïda incorrecte\n")




