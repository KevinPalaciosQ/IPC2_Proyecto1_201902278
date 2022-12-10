import tkinter as tk
from tkinter import filedialog
from colorama import init, Fore, Back, Style
import xml.etree.ElementTree as ET
#OBTENER LA RUTA DEL ARCHIVO
def ruta():
    root = tk.Tk()
    root.withdraw()
    ruta =  filedialog.askopenfilename(title='Cargar Archivo', filetypes = (("Text files", "*.xml*"), ("all files", "*.*")))
    return ruta
def Lector():
    tree=ET.parse('jugadores.xml')
    root=tree.getroot()
    print('\nTodos los atributos del Jugador: ')
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
                        movimientos=elemento2.text
                        print("tamaño: "+elemento2.text )
                    elif elemento2.tag=="figura":
                        movimientos=elemento2.text
                        print("figura: "+elemento2.text )
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
def Menu():
    opcion=0
    Ruta=""
    while opcion !=3:
        print(Fore.LIGHTGREEN_EX+"=========================================================================")
        print(Fore.CYAN+"========================"+Fore.LIGHTWHITE_EX+"FESTTIVAL NAVIDEÑO"+Fore.CYAN+"===============================")
        print(Fore.CYAN+"====="+Fore.LIGHTYELLOW_EX+"Laboratorio Introducción a la Programación y Computación 2"+Fore.CYAN+"==========")
        print(Fore.CYAN+"====="+Fore.LIGHTBLUE_EX+"                            MENU                                "+Fore.CYAN+"====")
        print(Fore.CYAN+"=="+Fore.RED+"1."+Fore.BLACK+" CARGAR ARCHIVO XML                                              "+Fore.CYAN+"====")
        print(Fore.CYAN+"=="+Fore.RED+"2."+Fore.BLACK+" PROCESAR ARCHIVO                                                "+Fore.CYAN+"====")
        print(Fore.CYAN+"=="+Fore.RED+"3."+Fore.BLACK+" BUSCAR PARTICIPANTE                                            "+Fore.CYAN+"     ====")
        print(Fore.CYAN+"=="+Fore.RED+"4."+Fore.BLACK+" GENERAR REPORTE                                                        "+Fore.CYAN+"====")
        print(Fore.CYAN+"=="+Fore.RED+"5."+Fore.BLACK+" SALIR                                                           "+Fore.CYAN+"====")
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
                #LeerXmlEquisde(Ruta)
                print("hola")
            elif opcion ==3 :
                NombrePaciente = str(input(Fore.LIGHTBLACK_EX+"==Ingrese el Nombre del Paciente:==\n>"))
                print("hola3")
                #pacientito = ListaDePacientes.RetornarPaciente(NombrePaciente)
            elif opcion == 4:
                print("== SE GENERO CON EXITO SU REPORTE EN GRAPHIZ==")
            elif opcion == 5:
                print(Fore.BLUE+"Vuelva Pronto :)")
                break
            else:
                print(Fore.RED+"Por favor ingrese una opción Válida")
        except:
            print(Fore.RED+"Opción Invalida")
Menu()
#Lector()