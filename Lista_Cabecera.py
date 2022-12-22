from Nodo_Cabecera import Nodo_Cabecera
class Lista_Cabecera:
    def __init__(self,tipo):
        self.tipo = tipo
        self.ultimo = None
        self.tipo = tipo #para verificar si son filas o columnas
        self.size = 0
    def insertar_nodoCabecera(self, nuevo : Nodo_Cabecera):
        self.size += 1
        if self.primero == None:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            
            if nuevo.id < self.primero.id:
                nuevo.siguiente = self.primero
                self.primero.anterior = nuevo
                self.primero = nuevo
            
            elif nuevo.id > self.ultimo.id:
                self.ultimo.siguiente = nuevo
                nuevo.anterior = self.ultimo
                self.ultimo = nuevo
            else:
                tmp: Nodo_Cabecera = self.primero 
                while tmp != None:
                    if nuevo.id < tmp.id:
                        nuevo.siguiente = tmp
                        nuevo.anterior = tmp.anterior
                        tmp.anterior.siguiente = nuevo
                        tmp.anterior = nuevo
                        break
                    elif nuevo.id > tmp.id:
                        tmp = tmp.siguiente
                    else:
                        break
    
    def mostrarCabeceras(self):
        tmp = self.primero
        while tmp != None:
            print("Coordenada", self.tipo, tmp.id)
            tmp = tmp.siguiente
            

    def getCabecera(self, id) -> Nodo_Cabecera: 
        tmp = self.primero
        while tmp != None:
            if id == tmp.id:
                return tmp
            tmp = tmp.siguiente
        return None