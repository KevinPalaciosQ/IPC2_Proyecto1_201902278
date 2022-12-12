# Lista Simple de Jugador
from NodoJugador import NodoJugador
from Jugador import Jugador
class ListaSimple:
    def __init__(self):
        self.cabeza=None
        self.tamanio=None
        self.final=0

    def InsertarJugador(self,nombre,edad,movimientos,tamaño,figura):
        NuevoJugador = Jugador(nombre,edad,movimientos,tamaño,figura)
        Nuevo = NodoJugador(NuevoJugador)
        if self.tamanio == 0:
            self.cabeza = Nuevo
            self.final = Nuevo
        else:
            self.final.siguiente=Nuevo
            self.final=Nuevo
        self.tamanio+=1
    
    def MostrarJugador(self,nombre):
        temporal=self.cabeza
        while temporal != None:
            if (temporal.jugador.nombre==nombre):
                print("****JUGADORES****")
                print("Su nombre es: "+temporal.jugador.nombre)
                print("Su edad es: "+temporal.jugador.edad)
                print("Su cantidad de Movimientos es: "+temporal.jugador.movimientos)
                print("Su tamaño es : "+temporal.jugador.tamaño)
                print("Su figura es : "+temporal.jugador.figura)


