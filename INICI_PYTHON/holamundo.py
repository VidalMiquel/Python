print("Hola mundo")
print("----------------MATRIUS--------------------------")
matriu = [[1,2,3],[4,5,6]]
for fila in matriu:
    for columna in fila:
        print(columna)
print("El primer element de la mariu és " + str(matriu[0][0]))
print("----------------DICCIONARIS--------------------------")
print("Feim feinamb diccionaris...")
dicc = {"nombre": "jose", "apellido": "lujan", "edad":28}
print(dicc)
print("Actualitzam els valors del diccionari")
dicc["apellido"] = "Vidal"
print(dicc)
print("Imprimint les keys del diccionari...")
print(dicc.keys())
print("Imprimint els valors assignats a les keys...")
print(dicc.values())
print("Eliminam una key del diccionari (NOMBRES)...")
del(dicc["nombre"])
print(dicc)
print("Afegim una key amb un valor nou al diccionari (X)...")
dicc['x'] = 100
print(dicc)
print(dicc.values())

print("----------------OPERADORS LÒGICS--------------------------")
a = 3
b = 2

print("El valor de la varible a és: " + str(a))
print("El valor de la varible b és: " + str(b))
c = a + b
print("a + b: " + str(c))
c = a-b
print("a - b: " + str(c))
c =  a*b
print("a * b: " + str(c))
c = a/b
print("a / b: " + str(c) + " DIVISÓ RESULTAT FLOTANT")
c = a//b
print("a // b: " + str(c) + " DIVISIÓ RESULTAT SENCER")
c = a%b
print("a mod b: " + str(c) + " IMPRIMIM RESIDU")
c = a**b
print("a elevatn b: " + str(c)) 
print("El valor de la varible a és: " + str(a))
print("El valor de la varible b és: " + str(b))
print("Intercanviant els valor de a i b")
a,b = b,a
print("El valor de la varible a és: " + str(a))
print("El valor de la varible b és: " + str(b))

encertat = True
not_encertat = False
print("TRUE AND FALSE")
print(encertat and not_encertat)
print("TRUE OR FALSE")
print(encertat or not_encertat)
print("NOT TRUE")
print(not encertat)
print("NOT FALSE")
print(not not_encertat)

print("--------------------CONDICIONALS---------------------")

if (a<b):
    print("El valor de a: " + str(a) + " és major que el de b: " + str(b))
else:
    print("El valor de a: " + str(a) + " és menor que el de b: " + str(b))


if (a == b):
    print("El valor de a: " + str(a) + " és igual a b " + str(b))
else:
    print("El valor de a: " + str(a) + " és diferent a b " + str(b))

if (a != b):
    print("El valor de a: " + str(a) + " és diferent a b " + str(b))


if (a == 0):
     print("A es igual a 0")
elif (a>0):
    print("A es major que 0")
else:
    print("A es menor que 0")

print("--------------------ITERADORS: FORS---------------------")
# podem fer us de BREAK (lo vist a java).
# continue: pel valor que esteim tractant, no aplicam les instruccions de l'iterador, passam al següent valor
# pass: per indicar que no tenim el codi pensat i sera substituïda per aquest
print("Iteram sobre una cadena")
nom = "supercalifragilistico"
print(nom)
for caracter in nom:
    print(caracter)

llista = [1,2,3, 'm' , 'manel']
print(llista)
print("Iterma sobre una llista")
for x in llista:
    print(x)

print("--------------------ITERADORS: WHILE---------------------")

x = 0;
while(x<10):
    print("El valor de x és " + str(x))
    x +=1

while (x<4):
    pass