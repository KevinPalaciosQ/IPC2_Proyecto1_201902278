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
        aux=self.cima
        text=""
        text+="rankdir=LR; \n "
        text+="node[shape=egg, style=filled, color=khaki, fontname=\"Century Gothic\"];  graph [fontname = \"Century Gothic\"];"
        text+="labelloc=\"t; \"label = \"Cursos\";\n"
        while aux:
            text+="x"+str(aux.regalo)+"[dir=both label=\"Lugar ="+str(aux.lugar)+"\\nRegalo = "+str(aux.regalo)+ "\"]"
            aux=aux.abajo
            print(text)
            if aux!=self.cima:
                text+="x"+str(aux.regalo)+"[dir=both label=\"Lugar ="+str(aux.lugar)+"\\nRegalo = "+str(aux.regalo)+ "\"]"
            if aux==self.cima:
                text+="x"+str(aux.regalo)+"[dir=both label=\"Lugar ="+str(aux.lugar)+"\\nRegalo = "+str(aux.regalo)+ "\"]"
        return text
            


    def CrearReporteRegalo(self):
        os.mkdir("Regalo")
        contenido="digraph G{\n\n"
        r=open("Regalo/regalo.txt","w")
        contenido+=str(self.report())
        contenido+="\n}"
        r.write(contenido)
        r.close()
        print("done")
        os.system("dot -Tpng Regalo/regalo.txt -o Regalo/regalo..png")
        os.system("dot -Tpdf Regalo/regalo.txt -o Regalo/regalo.pdf")


