class Nodo_Puntaje():
    def __init__(self,jugador,puntaje):
        self.jugador=jugador
        self.puntaje=puntaje
        self.siguiente=None
        self.anterior=None