import class Persona
# FUNCIONS

print("-----------------FUNCIONS AMB PARÀMTRES------------------------------")
def saludar(nom):
    return "Bon dia " + nom + "!" 
    #print("El país de procedència és: " + pais)
    #print("El seu DNI és: " + str(DNI))

nom = "Miquel Vidal"
#pais = "Espanya"
#DNI = 23456789
print(saludar(nom))

def sumar(primer_numero, segundo_numero):
    return primer_numero + segundo_numero

a = 3
b = 4
c = sumar(a,b)
print("El resultado de sumar " + str(a)+ " + " + str(b) + " es: " + str(c))
print(c)



print("-----------------FUNCIONS AMB PARÀMTRES AMB VALORS PER DEFECTE------------------------------")

#LA FUNCIÓ ESTÀ LLESTA PER FER FEINA TANT AMB PARÀMETRE COM SENSE PARÀMETRE, UTILITZANT EL PARÀMETRE
#PER DEFECTE (ESPECIFICAT AL IMPLEMENTAR LA FUNCIÓ) O EL QUE LI ESPECIFICAM PERA PARÀMETRE

def menjar_ous (correcte = True):
    if correcte:
        print("En Toni lo gosa")
    else:
        print("En Toni no lo gosa")

correcte = False

menjar_ous()
menjar_ous(correcte)

print("-----------------FUNCIONS AMB PARÀMTRES AMB NOM------------------------------")

def adeu (x, nombre):
    print("Adeu " + nombre)

adeu (1, "Miquel")
adeu (x = 1, nombre = "Pere")
adeu (nombre = "Joan", x = 1)


print("-----------------FUNCIONS DIFERENT QUANTITAT DE PARÀMETRES------------------------------")

#UN ASTERISC --> TUPLA
#DOS ASTERISCS --> DISSCIONARI

#AIXÒ ES COM SI PASSASIM PER PARÀMETRE UNA TUPLA = (1,2,3,4,5)
def sumatori (*nombre):
    c = 0
    for n in nombre:
        c += n
    return c

print(sumatori(1,2,3,4,5))

jose = Persoan()