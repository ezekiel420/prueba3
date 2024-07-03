import csv
pedidos=[]
gas_5=12500
gas_15=25500
ruts=[]
lista_rutas=["colina","santiago","puente alto"]
def repartos():
    rut=int(input("Ingrese su rut: "))
    ruts.append(rut)
    nombre=input("Ingrese su nombre: ")
    pedidos.append(nombre)
    direccion=input("Ingrese direccion: ")
    pedidos.append(direccion)
    comuna=input("Ingrese comuna: ")
    pedidos.append(comuna)
    while True:
        print(f"""Ingrese que gas llevara
              1.5 kilos  ${gas_5}
              2.15 kilos ${gas_15}   
              3.mesclado o mas de 1""")
        opc2=int(input("ingrese opcion: "))
        if opc2=="1":
            print("compra realizada")
            pedidos.append(opc2)
        elif opc2=="2":
            print("compra realizada")
            total=gas_15
            pedidos.append(opc2)
        elif opc2=="3":
            cantidad=input("Ingrese cilindro: ")
            if cantidad=="5":
                total=cantidad + gas_5
                pedidos.append(opc2)
            elif cantidad=="15":
                total= cantidad + gas_15
                pedidos.append(opc2)
        else:
            print("opcion incorrecta")

        print(f"su pedido: {rut}, {nombre}, {direccion}, {comuna}, {total}")

def pedido():
    print("datos de los pedidos")
    print(pedidos)
     
def rutas():
    print("las rutas son",lista_rutas)
    with open ("lista_rutas.csv",newline="") as arc:
        arc=csv.reader(lista_rutas)