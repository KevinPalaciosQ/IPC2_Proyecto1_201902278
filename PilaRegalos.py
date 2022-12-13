from NodoRegalo import NodoRegalo
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


