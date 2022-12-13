import tkinter as tk
from tkinter import filedialog
from colorama import init, Fore, Back, Style
import xml.etree.ElementTree as ET
from ListaJugador import *
from PilaRegalos import *
#OBTENER LA RUTA DEL ARCHIVO
ListaDeJugadores=ListaSimple()
Regalos=PilaRegalo()
def LeerXml(Ruta):
    global ListaSimple
    nombre = ""
    edad = ""
    movimientos = ""
    tamaño = ""
    figura = ""
    if Ruta !="":
        Archivo=ET.parse(Ruta)
        root=Archivo.getroot()
        print("\nTodos los atributos del Jugador: ")
        for elemento in root:#Elemento-Jugador
                    for elemento2 in elemento:
                        if elemento2.tag=="datospersonales":
                            for elemento3 in elemento2:
                                if elemento3.tag=="nombre":
                                    nombre=elemento3.text
                                    print("nombre: "+elemento3.text )
                                elif elemento3.tag=="edad":
                                    edad=elemento3.text
                                    print("edad: "+elemento3.text )
                        elif elemento2.tag=="movimientos":
                            movimientos=elemento2.text
                            print("movimientos: "+elemento2.text )
                        elif elemento2.tag=="tamaño":
                            tamaño=elemento2.text
                            print("tamaño: "+elemento2.text )
                        elif elemento2.tag=="figura":
                            figura=elemento2.text
                            print("figura: "+elemento2.text )
                    ListaDeJugadores.InsertarJugador(nombre,edad,movimientos,tamaño,figura)
                    for elemento2 in elemento:
                        if elemento2.tag=="puzzle":   
                            print("----------------------------Puzzle----------------------------")
                            for elemento3 in elemento2:
                                if elemento3.tag=="celda":
                                    print("fila :"+elemento3.attrib.get("f"))
                                    print("columna :"+elemento3.attrib.get("c"))
                            print("----------------------------Solucion----------------------------")
                    for elemento2 in elemento:
                        if elemento2.tag=="solucion":   
                            for elemento3 in elemento2:
                                if elemento3.tag=="celda":
                                    print("fila :"+elemento3.attrib.get("f"))
                                    print("columna :"+elemento3.attrib.get("c"))
def LeerXmlRegalo(Ruta2):
    global PilaRegalo
    #Regalos.IngresarRegalo("Guatemala","dinero")
    lugar=""
    regalo=""
    if Ruta2 !="":
        Archivo=ET.parse(Ruta2)
        raiz=Archivo.getroot()
        print("\nTodos los atributos de Regalo: ")
        for element in raiz:#Element-Regalo
            for element2 in element:
                if element2.tag=="lugar":
                    lugar=element2.text
                    print("lugar: "+element2.text )
                elif element2.tag=="regalo":
                    regalo=element2.text
                    print("regalo: "+element2.text )
            #Regalos.IngresarRegalo(lugar,regalo)
        

def ruta():
    root = tk.Tk()
    root.withdraw()
    ruta =  filedialog.askopenfilename(title="Cargar Archivo", filetypes = (("Text files", "*.xml*"), ("all files", "*.*")))
    return ruta
def RutaR():
    root = tk.Tk()
    root.withdraw()
    RutaPremio =  filedialog.askopenfilename(title="Cargar Archivo", filetypes = (("Text files", "*.xml*"), ("all files", "*.*")))
    return RutaPremio
def Menu():
    opcion=0
    Ruta=""
    Ruta2=""
    while opcion !=3:
        print(Fore.LIGHTGREEN_EX+"=========================================================================")
        print(Fore.CYAN+"========================"+Fore.LIGHTWHITE_EX+"FESTTIVAL NAVIDEÑO"+Fore.CYAN+"===============================")
        print(Fore.CYAN+"====="+Fore.LIGHTYELLOW_EX+"Laboratorio Introducción a la Programación y Computación 2"+Fore.CYAN+"==========")
        print(Fore.CYAN+"====="+Fore.LIGHTBLUE_EX+"                            MENU                                "+Fore.CYAN+"====")
        print(Fore.CYAN+"=="+Fore.RED+"1."+Fore.BLACK+" CARGAR ARCHIVO XML JUGADORES                                   "+Fore.CYAN+"====")
        print(Fore.CYAN+"=="+Fore.RED+"2."+Fore.BLACK+" PROCESAR ARCHIVO JUGADORES                                               "+Fore.CYAN+"====")
        print(Fore.CYAN+"=="+Fore.RED+"3."+Fore.BLACK+" BUSCAR JUGADOR                                            "+Fore.CYAN+"     ====")
        print(Fore.CYAN+"=="+Fore.RED+"4."+Fore.BLACK+" TOP 10 JUGADORES                                                    "+Fore.CYAN+"====")
        print(Fore.CYAN+"=="+Fore.RED+"5."+Fore.BLACK+" CARGAR ARCHIVO XML PREMIOS                                                      "+Fore.CYAN+"====")
        print(Fore.CYAN+"=="+Fore.RED+"6."+Fore.BLACK+" PROCESAR ARCHIVO XML PREMIOS                                                          "+Fore.CYAN+"====")
        print(Fore.CYAN+"=="+Fore.RED+"7."+Fore.BLACK+" MOSTRAR PILA PREMIOS                                                       "+Fore.CYAN+"====")
        print(Fore.CYAN+"=="+Fore.RED+"8."+Fore.BLACK+" SALIR                                                      "+Fore.CYAN+"====")        
        print(Fore.LIGHTGREEN_EX+"=========================================================================")
        try:    
            opcion = int(input(Fore.LIGHTCYAN_EX+"== Elija una opción:==\n>"))
            if opcion == 1:
                try:
                    Ruta = ruta()
                    if Ruta !="":
                        print("== Ruta: ", str(Ruta))
                        print("== EL ARCHIVO SE CARGO CON EXITO                  ==")
                    else:
                        print("== NO SE CARGÓ NINGUN ARCHIVO                     ==")
                except:
                    print("")
            elif opcion==2:
                LeerXml(Ruta)
            elif opcion ==3 :
                NombreJugador = str(input(Fore.LIGHTBLACK_EX+"==Ingrese el Nombre del Jugador:==\n>"))
                Jugadorcito=ListaDeJugadores.RetornarJugador(NombreJugador)
                if Jugadorcito !=None:
                    ListaDeJugadores.MostrarJugador(NombreJugador)
                else:
                    print(Fore.RED+"No se encontró Jugador")
            elif opcion == 4:
                try:
                    Ruta2 = RutaR()
                    if Ruta2 !="":
                        print("== Ruta: ", str(Ruta2))
                        print("== EL ARCHIVO SE CARGO CON EXITO                  ==")
                    else:
                        print("== NO SE CARGÓ NINGUN ARCHIVO                     ==")
                except:
                    print("")
            elif opcion==5:
                LeerXmlRegalo(Ruta2)
            elif opcion == 6:
                print(Fore.BLUE+"Vuelva Pronto :)")
                break
            else:
                print(Fore.RED+"Por favor ingrese una opción Válida")
        except:
            print(Fore.RED+"Opción Invalida")
Menu()
