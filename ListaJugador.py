# Lista Simple de Jugador
from NodoJugador import NodoJugador
from Jugador import Jugador
class ListaSimple:
    def __init__(self):
        self.cabeza=None
        self.tamanio=0

    def InsertarJugador(self,nombre,edad,movimientos,tamaño,figura):
        NuevoJugador = Jugador(nombre,edad,movimientos,tamaño,figura)
        Nuevo = NodoJugador(NuevoJugador)
        if self.cabeza==None:#CABEZA NULLA, CABEZA NUEVO
            self.cabeza = Nuevo
        else:
            temporal=self.cabeza#para ver cual es el siguiente
            while temporal!= None:
                if temporal.siguiente==None:
                    break
                temporal=temporal.siguiente
            temporal.siguiente=Nuevo
        self.tamanio+=1
    def SacarJugador(self):
        if self.tamanio!=0:
            self.cabeza=self.cabeza.siguiente
            self.tamanio-=1
        else:
            print("La cola ya esta vacia :)")
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
            temporal = temporal.siguiente
    def RetornarJugador(self,nombre):
        temporal=self.cabeza
        while temporal!=None:
            if (temporal.jugador.nombre==nombre):
                return temporal.jugador.edad
            temporal=temporal.siguiente
        return None




