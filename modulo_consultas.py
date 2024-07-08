from datos import *
from modulo_pedidos import pedir_opcion

RUTA_PEDIDOS="JSON\pedidos.json"

def mostrar_todos_pedidos(datos_pedidos):
    for user in datos_pedidos:
        print("\n"+"*"*len(F"Pedido de {user}:"))
        print(F"Pedido de {user}: ")
        print("*"*len(F"Pedido de {user}:"))
        for rcategorias in datos_pedidos[user]:
            if rcategorias=="pagado" or rcategorias=="identificador" or rcategorias=="fecha_pago" or rcategorias=="total":
                print(" *"+rcategorias+" = "+str(datos_pedidos[user][rcategorias]))
            else:
                print(" *En ",rcategorias)
                print("     -----------------------------------------")
                for pedidos in datos_pedidos[user][rcategorias]:
                    print("     producto = ",pedidos["producto"])
                    print("     nombre = ",pedidos["nombre producto"])
                    print("     cantidad = ",pedidos["cantidad"])
                    print("     subtotal = ",pedidos["subtotal"])
                    print("     -----------------------------------------")


def mostrar_pedido_especifico(datos_pedidos):

    valor=input(f"Ingrese el nombre del cliente o el identificador para buscar el pedido:\n>> ")

    for user in datos_pedidos:
        if user==valor or datos_pedidos[user]["identificador"]==valor:

            print(F"\nPedido de {user}: ")
            print("*"*len(F"Pedido de {user}:"))
            for rcategorias in datos_pedidos[user]:
                if rcategorias=="pagado" or rcategorias=="identificador" or rcategorias=="fecha_pago" or rcategorias=="total":
                    print(" *"+rcategorias+" = "+str(datos_pedidos[user][rcategorias]))
                else:
                    print(" *En ",rcategorias)
                    for pedidos in datos_pedidos[user][rcategorias]:
                        print("     -----------------------------------------")
                        print("     producto = ",pedidos["producto"])
                        print("     nombre = ",pedidos["nombre producto"])
                        print("     cantidad = ",pedidos["cantidad"])
                        print("     subtotal = ",pedidos["subtotal"])
                        print("     -----------------------------------------") 
            return None
    print(F"\n*No se encontró un pedido a ese nombre o con ese identificador\n")
    return None

def mod_consultas(datos_pedidos):
    print("\n*-*-*-MODULO DE CONSULTAS-*-*-*")
    while True:
        print("1. Todos los pedidos")
        print("2. Pedido especifico")
        print("3. Salir")
        opcion=pedir_opcion()
        if opcion==1: mostrar_todos_pedidos(datos_pedidos)
        elif opcion==2: mostrar_pedido_especifico(datos_pedidos)
        elif opcion==3: return print("*Volviendo al modulo principal\n")
        else: print("*Opcion no valida")