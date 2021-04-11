# Exemple de matrius
import random


class Matriu:
    fila = 0
    columna = 0
    elements = None

    def __init__(self, x, y):
        self.fila = x
        self.columna = y
        self.elements = []
        for i in range(self.fila):
            self.elements.append([])
            for j in range(self.columna):
                self.elements[i].append(random.randrange(10))

    def toString(self):
        for i in range(self.fila):
            for j in range(self.columna):
                print("| {0}".format(self.getCasella(i, j)), sep=",", end=" ")
            print("|\n")

    def getCasella(self, x, y):
        return self.elements[x][y]

    def numeroFila(self):
        return self.fila

    def numeroColumna(self):
        return self.columna

    def esQuadrada(self):
        return self.fila == self.columna

    def setFila(self, fila):
        self.fila = fila

    def setColumna(self, columna):
        self.columna = columna

    def sumarMatrius(self, Matriu):
        if (self.columna == Matriu.numeroColumna()) and (self.fila == Matriu.numeroFila()):
            for i in range(self.fila):
                for j in range(self.columna):
                    self.elements[i][j] += Matriu.elements[i][j]
        else:
            print(
                "No es pot dur a terme la suma de les dues matrius, el nombre de files i columnes no coincideix")

    def restarMatrius(self, Matriu):
        if (self.columna == Matriu.numeroColumna()) and (self.fila == Matriu.numeroFila()):
            for i in range(self.fila):
                for j in range(self.columna):
                    self.elements[i][j] -= Matriu.elements[i][j]
        else:
            print("No es pot dur a terme la resta de les dues matrius, el nombre de files i columnes no coincideix")

    def trasposada(self):
        MatriuAux = []
        for i in range(self.columna):
            MatriuAux.append([])
            for j in range(self.fila):
                MatriuAux[i].append(self.elements[j][i])
        self.elements = MatriuAux
        # Per poder fer el toString, canvima files per columnes i a l'inversa
        self.fila, self.columna = self.columna, self.fila

    def matriuPerEscalar(self, escalar):
        for i in range(self.fila):
            for j in range(self.columna):
                self.elements[i][j] *= escalar

    def matriuIdentitat(self):
        if self.fila == self.columna:
            for i in range(self.fila):
                for j in range(self.columna):
                    if(i == j):
                        self.elements[i][j] = 1
                    else:
                        self.elements[i][j] = 0
        else:
            print("No podem treure la matriu identitat, la matriu no és cuadrada")

'''
    def multiplicar(self, Matriu):
        MatriuAux = []
        for i in range(self.fila):
            MatriuAux.append([])
            for j in range(self.columna):
                for k in range(Matriu.numeroColumna()):
                    MatriuAux[i].append() += self.elements[i][j] * Matriu.getCasella(i, k)
'''
def __del__(self):
    print("Eliminam instànices ja no utilitzades \n ")

