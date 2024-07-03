import os, csv 
from funciones import *


os.system("cls")
while True:
    try:
        print ("""Bienvenido a Gaxplosive
           1.Registrar pedido
           2.Listar todos los pedidos
           3.Buscar pedido por rut
           4.imprimir hoja de ruta
           5.salir del programa""")
        opc=input("selecciones una opcion: ")
    except:
        print("Ingrese opcion correcta")
    if opc=="1":
      repartos()
      
    elif opc=="2":
       pedido()
       
    elif opc=="3":
      b_rut=input("Ingrese rut: ")
      b_rut.index(ruts)
    elif opc=="4":
      rutas()
    else:
        print("Gracias vuelva pronto")