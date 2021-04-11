#Primer exemple de la POO en Python

class Persona:
    #Atribut de classe
    vida  = 5
    #Atribut d'instànica
    #Constructor
    def __init__(self):
        self.nom = ""
        self.edad = "0"
        self.DNI = ""

    def inicialitzar_Dades(self):
        self.edad = input("Introdueix la edat: ")
        self.DNI = input("Introdeuix el DNI: ")
        self.nom = input("Introdeuix el nom: ")

    #Mètodes d'instància    
    def imprimir_Dades(self):
        print("L'edat de la persona és: " + self.edad + " anys")
        print("El seu DNI és: " + self.DNI)
        print("El seu nom és: " + self.nom)

    def set_edad(self, edad):
        self.edad = edad

    def get_edad(self):
        return self.edad

    def set_nom(self, nom):
        self.nom = nom

    def get_nom(self):
        return self.nom

    def set_DNI(self, DNI):
        self.DNI = DNI

    def get_DNI(self):
        return self.DNI

    #Mètodes de clase
    @classmethod
    def correr(cls):
        print("Método de clase")

    #Mètodes estàtics
    @staticmethod
    def brincar():
        vida = 10

    #Lliberam els recursos de memoria que ja no són utilitzats per la instància.
    def __del__(self):
        print("Eliminam instànices ja no utilitzades \n ")


