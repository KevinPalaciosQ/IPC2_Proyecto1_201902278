from Player import Player
class ListaDoble():
    def __init__(self):
        self.inicio = None
        self.final = None
        self.size = 0
    def insertar(self, jugador, punteo): #insertar
        nuevo = Player(jugador, punteo)
        self.size += 1
        if self.inicio is None:
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
            nuevo.anterior = tmp
            self.final = nuevo
    def mostrarPuntos(self):
        tmp = self.inicio
        while tmp is not None:
            print("Jugador: ", tmp.jugador, "       Punteo: ", tmp.punteo)
            tmp = tmp.siguiente
    def BubbleSort(self):
        if self.size > 1:
            while True:
                actual = self.inicio
                i = None  # anterior
                j = self.inicio.siguiente  # siguiente
                cambio = False
                while j != None:
                    if actual.punteo< j.punteo:
                        cambio = True
                        if i != None:
                            tmp = j.siguiente
                            i.siguiente = j
                            j.siguiente = actual
                            actual.siguiente = tmp
                        else:
                            tmp2 = j.siguiente
                            self.inicio = j
                            j.siguiente = actual
                            actual.siguiente = tmp2
                        i = j
                        j = actual.siguiente
                    else:
                        i = actual
                        actual = j
                        j = j.siguiente
                if not cambio:
                    break