from NodoRegalo import NodoRegalo
import os
class PilaRegalo():
    def __init__(self) :
        self.cima=None
        self.tamanio=0
    def IngresarRegalo(self,lugar,regalo):#se añadió regalo
        nuevo=NodoRegalo(lugar,regalo)
        nuevo.abajo=self.cima#subiendo regalos
        self.cima=nuevo
        self.tamanio+=1
    def SacarRegalo(self):
        self.cima=self.cima.abajo
        if self.tamanio!=0:
            self.tamanio-=1
        else:
            print("Se acabaron los regalos :c")

    def GraficarRegalos(self):
        text=""
        text+="rankdir=LR; \n "
        text+="node[shape=Mrecord]; \n "
        text+="graph [fontname=\"Century Gothic\"]; \n "
        text+="Pila[style=\"filled\" ,label=\""
        temporal=self.cima
        while temporal!=None:
            if temporal.abajo==None:
                text+=temporal.regalo
                temporal=temporal.abajo
            else:
                text+=temporal.regalo +"|"
                temporal=temporal.abajo
        text+="\"];\n}"
        return text


    def CrearReporteRegalo(self):
        try:
            os.mkdir("Regalos")
        except:
            pass
        contenido="digraph G{\n\n"
        r= open("Regalos/reporte.dot","w",encoding="utf8")
        contenido+=str(self.GraficarRegalos())
        print(contenido)
        r.write(contenido)
        r.close()
        os.system("dot -Tpng Regalos/reporte.dot -o Regalos/reporte.png")
        os.system("dot -Tpdf Regalos/reporte.dot -o Regalos/reporte.pdf")
        os.startfile("Regalos/reporte.png")
        print("done")
    def GraficarRegalos2(self):
        text=""
        text+="rankdir=DU; \n "
        text+="node[shape=box, style=filled, color=gray, fontname=\"Century Gothic\"]; \n "
        text+="graph [fontname=\"Century Gothic\"]; \n "
        text+="labelloc=\"t\"; label=\"Regalos\"; \n"
        actual=self.cima
        while actual!=None:
            if (actual.abajo==None):
                text+=str(actual)+"[label=\"Lugar: "+actual.lugar+"\\Regalo: "+actual.regalo+"\"];\n"
                actual=actual.abajo
        text+="}"
        return text
    def CrearReporteRegalo1(self):
        try:
            os.mkdir("Regalos")
        except:
            pass
        contenido="digraph G{\n\n"
        r= open("Regalos/reporte.dot","w",encoding="utf8")
        contenido+=str(self.GraficarRegalos2())
        r.write(contenido)
        r.close()
        os.system("dot -Tpng Regalos/reporte.dot -o Regalos/reporte.png")
        os.system("dot -Tpdf Regalos/reporte.dot -o Regalos/reporte.pdf")
        os.startfile("Regalos/reporte.png")
        print("done")         



