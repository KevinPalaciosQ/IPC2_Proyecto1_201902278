# Lista Simple de Jugador
from NodoJugador import NodoJugador
from Jugador import Jugador
import os
from colorama import Fore
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
                print(Fore.LIGHTBLACK_EX+"=============================="+Fore.YELLOW+" ඞ JUGADOR ඞ "+Fore.LIGHTBLACK_EX+"==============================")
                print("==Su nombre es: "+temporal.jugador.nombre)
                print("==Su edad es: "+temporal.jugador.edad)
                print("==Su cantidad de Movimientos es: "+temporal.jugador.movimientos)
                print("==Su tamaño es : "+temporal.jugador.tamaño)
                print("==Su figura es : "+temporal.jugador.figura)
                print(Fore.LIGHTBLACK_EX+"=========================================================================")
            temporal = temporal.siguiente
    def RetornarJugador(self,nombre):
        temporal=self.cabeza
        while temporal!=None:
            if (temporal.jugador.nombre==nombre):
                return temporal.jugador.edad
            temporal=temporal.siguiente
        return None
    def ReporteLista(self):
        text=""
        text+="rankdir=LR; \n "
        text+="node[shape=box, style=filled, color=skyblue, fontname=\"Century Gothic\"]; \n "
        text+="graph [fontname=\"Century Gothic\"]; \n "
        text+="labelloc=\"t\"; label=\"Jugadores\"; \n"
        contador=0
        temporal=self.cabeza
        #text+=str(contador)+"[label=\"Nombre: "+temporal.jugador.nombre+"\"];\n"
        while temporal!=None:
            text+=str(contador)+"[label=\"Nombre: "+temporal.jugador.nombre+"\\nEdad: "+temporal.jugador.edad+"\\nMovimientos: "+temporal.jugador.movimientos+"\\nTamaño: "+temporal.jugador.tamaño+"\\nFigura: "+temporal.jugador.figura+"\"];\n"
            if temporal.siguiente!=None:
                aux=contador+1
                text+=str(contador)+"->"+str(aux)+"[dir=back];\n"
            temporal=temporal.siguiente
            contador+=1
        text+="}"
        return text
    def CrearReporteLista(self):
        try:
            os.mkdir("Jugadores")
        except:
            pass
        contenido="digraph G{\n\n"
        r= open("Jugadores/reporte.dot","w",encoding="utf8")
        contenido+=str(self.ReporteLista())
        r.write(contenido)
        r.close()
        os.system("dot -Tpng Jugadores/reporte.dot -o Jugadores/reporte.png")
        os.system("dot -Tpdf Jugadores/reporte.dot -o Jugadores/reporte.pdf")
        os.startfile("Jugadores/reporte.png")

        print("done")
    def ReporteListaActualizado(self):
        text=""
        text+="rankdir=LR; \n "
        text+="node[shape=box, style=filled, color=skyblue, fontname=\"Century Gothic\"]; \n "
        text+="graph [fontname=\"Century Gothic\"]; \n "
        text+="labelloc=\"t\"; label=\"Jugadores Actualizados\"; \n"
        contador=0
        temporal=self.cabeza
        #text+=str(contador)+"[label=\"Nombre: "+temporal.jugador.nombre+"\"];\n"
        while temporal!=None:
            text+=str(contador)+"[label=\"Nombre: "+temporal.jugador.nombre+"\\nEdad: "+temporal.jugador.edad+"\\nMovimientos: "+temporal.jugador.movimientos+"\\nTamaño: "+temporal.jugador.tamaño+"\\nFigura: "+temporal.jugador.figura+"\"];\n"
            if temporal.siguiente!=None:
                aux=contador+1
                text+=str(contador)+"->"+str(aux)+"[dir=back];\n"
            temporal=temporal.siguiente
            contador+=1
        text+="}"
        return text
    def CrearReporteListaActualizado(self):
        try:
            os.mkdir("Jugadores")
        except:
            pass
        contenido="digraph G{\n\n"
        r= open("Jugadores/reporteactualizado.dot","w",encoding="utf8")
        contenido+=str(self.ReporteListaActualizado())
        r.write(contenido)
        r.close()
        os.system("dot -Tpng Jugadores/reporteactualizado.dot -o Jugadores/reporteactualizado.png")
        os.system("dot -Tpdf Jugadores/reporteactualizado.dot -o Jugadores/reporteactualizado.pdf")
        os.startfile("Jugadores/reporteactualizado.png")

        print("done")
    def Top10Jugadores():
        print("Top 10 Jugadores")
        pass