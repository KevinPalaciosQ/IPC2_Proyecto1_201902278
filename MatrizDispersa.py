from Nodo_Cabecera import Nodo_Cabecera
from Lista_Cabecera import ListaCabecera
import os
import webbrowser

class Nodo_Celda():
    def __init__(self,x,y,caracter):
        self.caracter = caracter
        self.coordenadaX = x #fila
        self.coordenadaY = y #columna
        self.arriba = None
        self.abajo = None
        self.derecha = None
        self.izquierda = None

    def setArriba(self, arriba):
        self.arriba = arriba

    def getArrita(self):
        return self.arriba

    def setAbajo(self, abajo):
        self.abajo = abajo

    def getAbajo(self):
        return self.abajo

    def setDerecha(self,derecha):
        self.derecha = derecha

    def getDerecha(self):
        return self.derecha 

    def setIzuierda(self, izquierda):
        self.izquierda = izquierda

    def getIzquierda(self):
        return self.izquierda

class MatrizDispersa():
    def __init__(self):
        self.capa = 0
        self.filas= ListaCabecera("f")
        self.columnas =ListaCabecera("c")