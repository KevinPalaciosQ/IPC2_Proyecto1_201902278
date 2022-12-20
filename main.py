import tkinter as tk
from tkinter import filedialog
from colorama import init, Fore, Back, Style
import xml.etree.ElementTree as ET
from ListaJugador import *
from PilaRegalos import *
#OBTENER LA RUTA DEL ARCHIVO
ListaDeJugadores=ListaSimple()
Regalos=PilaRegalo()
ListaDeTop10=ListaSimple()
def LeerXml(Ruta):
    global ListaSimple
    nombre = ""
    edad = ""
    movimientos = ""
    tamaño = ""
    figura = ""
    punteo=0
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
                            if int(movimientos)<5:
                                punteo+=100
                            elif int(movimientos)>5 and int(movimientos)<10:
                                punteo+=75
                            elif int(movimientos)>10 and int(movimientos)<15:
                                punteo+=50
                            elif int(movimientos)>15 and int(movimientos)<20:
                                punteo+=25
                            elif int(movimientos)>20 and int(movimientos)<25:
                                punteo+=20
                            elif int(movimientos)>=10000:
                                print("Usted alcanzó el Límite de Movimientos")
                            print(str(punteo))
                            print("movimientos: "+elemento2.text )
                        elif elemento2.tag=="tamaño":
                            tamaño=elemento2.text
                            if int(tamaño)>=30:
                                print("Usted alcanzó el máximo del tamaño")
                            print("tamaño: "+elemento2.text )
                        elif elemento2.tag=="figura":
                            figura=elemento2.text
                            if str(figura)=="estrella de Belén":
                                punteo+=500
                            elif str(figura)=="Árbol de Navidad":
                                punteo+=250
                            elif str(figura)=="Regalo":
                                punteo+=100
                            print("figura: "+elemento2.text )
                    ListaDeJugadores.InsertarJugador(nombre,edad,movimientos,tamaño,figura)
                    #insertar jugador y puntaje 
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
            Regalos.IngresarRegalo(lugar,regalo)        

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
        print(Fore.CYAN+"======================"+Fore.YELLOW+"✰ "+Fore.LIGHTWHITE_EX+"FESTIVAL NAVIDEÑO"+Fore.YELLOW+"✰ "+Fore.CYAN+"==============================")
        print(Fore.MAGENTA+"=========================================================================")
        print(Fore.MAGENTA+"======= "+Fore.WHITE+"╚╣╠╝─╚╣╠╝─────────╗╬╔╬╔"+Fore.LIGHTYELLOW_EX+"  Feliz★* 。 • ˚ ˚ ˛ ˚ ˛ •"+Fore.MAGENTA+"         =======")
        print(Fore.MAGENTA+"======= "+Fore.WHITE+"▄╬╬──▄╬╬───╔╗───╔▀▀▀▀▀║"+Fore.LIGHTYELLOW_EX+"•。★Navidad★ 。* 。"+Fore.MAGENTA+"                =======")
        print(Fore.MAGENTA+"======= "+Fore.WHITE+"╚╗╠▄╬╚╗╠▄╬─╚╗─╔▀╝────╔╝"+Fore.LIGHTBLUE_EX+" ° 。 ° ˛˚˛ * _Π______*。*˚"+Fore.MAGENTA+"        =======")
        print(Fore.MAGENTA+"======= "+Fore.WHITE+"─╠╦╦╬─╠╦╦╬══╬═╩╦═╦═╦═╬"+Fore.LIGHTBLUE_EX+"    ˚ ˛ •˛•˚ */______/~  ＼。˚ ˚ "+Fore.MAGENTA+"   =======")
        print(Fore.MAGENTA+"======= "+Fore.WHITE+"─╝╝╝╝─╝╝╝╝─╘╧══╧═╧═╧═╧═╛"+Fore.LIGHTBLUE_EX+" ˚ ˛ •˛• ˚ ｜ 田田 ｜門｜ ˚"+Fore.MAGENTA+"       =======")
        print(Fore.MAGENTA+"=========================================================================")
        print(Fore.CYAN+"====="+Fore.LIGHTYELLOW_EX+"Laboratorio Introducción a la Programación y Computación 2"+Fore.CYAN+"==========")
        print(Fore.LIGHTGREEN_EX+"=========================================================================")
        print(Fore.CYAN+"====="+Fore.LIGHTMAGENTA_EX+" ඞ "+Fore.LIGHTCYAN_EX+" ඞ "+Fore.YELLOW+" ඞ "+Fore.LIGHTRED_EX+"                   MENU                     "+Fore.LIGHTMAGENTA_EX+" ඞ "+Fore.LIGHTCYAN_EX+" ඞ "+Fore.YELLOW+" ඞ  "+Fore.LIGHTRED_EX+Fore.CYAN+"=====")
        print(Fore.CYAN+"=="+Fore.RED+"1."+Fore.BLACK+" CARGAR ARCHIVO XML JUGADORES                                   "+Fore.CYAN+ " ====")
        print(Fore.CYAN+"=="+Fore.RED+"2."+Fore.BLACK+" PROCESAR ARCHIVO JUGADORES                                      "+Fore.CYAN+"====")
        print(Fore.CYAN+"=="+Fore.RED+"3."+Fore.BLACK+" BUSCAR JUGADOR                                            "+Fore.CYAN+"      ====")
        print(Fore.CYAN+"=="+Fore.RED+"4."+Fore.BLACK+" TOP 10 JUGADORES                                                "+Fore.CYAN+"====")
        print(Fore.CYAN+"=="+Fore.RED+"5."+Fore.BLACK+" CARGAR ARCHIVO XML PREMIOS                                      "+Fore.CYAN+"====")
        print(Fore.CYAN+"=="+Fore.RED+"6."+Fore.BLACK+" PROCESAR ARCHIVO XML PREMIOS                                    "+Fore.CYAN+"====")
        print(Fore.CYAN+"=="+Fore.RED+"7."+Fore.BLACK+" MOSTRAR PILA PREMIOS                                            "+Fore.CYAN+"====")
        print(Fore.CYAN+"=="+Fore.RED+"8."+Fore.BLACK+" SALIR                                                           "+Fore.CYAN+"====")        
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
                ListaDeJugadores.CrearReporteLista()
            elif opcion ==3 :
                NombreJugador = str(input(Fore.LIGHTBLACK_EX+"==Ingrese el Nombre del Jugador:==\n>"))
                Jugadorcito=ListaDeJugadores.RetornarJugador(NombreJugador)
                if Jugadorcito !=None:
                    ListaDeJugadores.MostrarJugador(NombreJugador)
                    ListaDeJugadores.SacarJugador()
                    ListaDeJugadores.CrearReporteListaActualizado()
                    #ListaDeJugadores.CrearReporteLista()
                    #print(ListaDeJugadores)
                    Menu()
                else:
                    print(Fore.RED+"No se encontró Jugador")
                    Menu()
            elif opcion == 4:
                global ListaSimple
                print("TOP 10 JUGADORES")
                
            elif opcion == 5:
                try:
                    Ruta2 = RutaR()
                    if Ruta2 !="":
                        print("== Ruta: ", str(Ruta2))
                        print("== EL ARCHIVO SE CARGO CON EXITO                  ==")
                    else:
                        print("== NO SE CARGÓ NINGUN ARCHIVO                     ==")
                except:
                    print("")
            elif opcion==6:
                LeerXmlRegalo(Ruta2)
                Regalos.CrearReporteRegalo()
                Menu()
            elif opcion==7:
                print("Pila de premios Restante")
            elif opcion == 8:
                print(Fore.BLUE+"Vuelva Pronto :)")
                print(Fore.WHITE+"════════════ ('\../') ═════════════")
                print(Fore.WHITE+"════════════  (◕.◕) ═══════════════")
                print(Fore.WHITE+"════════════ (,,)(,,) ═════════════")
                print(Fore.BLUE+".▀█▀.█▄█.█▀█.█▄.█.█▄▀　█▄█.█▀█.█─█")
                print(Fore.BLUE+"─.█.─█▀█.█▀█.█.▀█.█▀▄　─█.─█▄█.█▄█")
                print(Fore.WHITE+"═══════════════════════════════════")
                break
            else:
                print(Fore.RED+"Por favor ingrese una opción Válida")
        except:
            print(Fore.RED+"Opción Invalida")
Menu()

