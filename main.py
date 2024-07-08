from modulo_pedidos import *
from modulo_consultas import *
def menu ():
    print("Bienvenido")
    while True:
        print("1. Registrar pedido")
        print("2. Realizar pago")
        print("3. Cancelar un pedido ")
        print("4. Modificar un pedido ")
        print("5. Modulo de Consultas")
        print("6. Salir")
        opcion=pedir_opcion()
        datos_pedidos=json_traer_datos(RUTA_PEDIDOS)
        lista_catalogo=csv_traer_datos(RUTA_CATALOGO)
        if opcion==1: pedidos_productos(lista_catalogo,datos_pedidos)
        elif opcion==2:pagar_pedido(datos_pedidos)
        elif opcion==3: cancelar_pedido(datos_pedidos)
        elif opcion==4: modificar_pedido(datos_pedidos)
        elif opcion==5: mod_consultas(datos_pedidos)
        elif opcion==6: return print("*Saliste exitosamente")
        else: print ("*Opcion no valida")

menu()