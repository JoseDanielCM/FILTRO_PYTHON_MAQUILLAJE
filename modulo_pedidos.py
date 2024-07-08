from datos import *
import datetime

RUTA_CATALOGO="catalogo.csv"
RUTA_PEDIDOS="JSON\pedidos.json"


###################### SOLO SON PARA USARSE EN PEDIDOS PRODUCTOS #####################
def pedir_opcion():
    try:
        opcion=int(input("Ingresa una opcion:\n>> "))
        return opcion
    except:print("*Debes ingresar un numero entero en 'pedir opcion' ")

def mostrar_categoria(lista_catalogo):
    categorias_disponibles=[]
    for i in lista_catalogo:
        categorias_disponibles.append(i["categoria"])
    categorias_disponibles=set(categorias_disponibles)
    categorias_disponibles=list(categorias_disponibles)
    print("Categorias disponibles: ")
    for i in categorias_disponibles:
        print(i)
    categoria=input("Ingresa cual en cual de las categorias, deseas comprar?: ")
    if categoria in categorias_disponibles: return categoria
    else:
        print("*Se debìa escoger una de las categorias presentadas")
        return None

def mostrar_productos(categoria,lista_catalogo):
    productos_disponibles=[]
    for i in lista_catalogo:
            if categoria==i["categoria"]: productos_disponibles.append(i["producto"])
    productos_disponibles=set(productos_disponibles)
    productos_disponibles=list(productos_disponibles)
    print("Los siguientes son los productos que tenemos disponibles: ")

    ############# MOSTRAR PRODUCTOS ###################3
    for i in productos_disponibles:
        print(i)
    producto_escogido=input("Ingresa cual en cual de las categorias, deseas comprar?:\n>> ")
    producto_escogido=producto_escogido.lower()
    if producto_escogido in productos_disponibles: return producto_escogido
    else:
        print("*Se debìa escoger uno de los productos presentados")
        return None

def mostrar_nombres_precios(producto,lista_catalogo):
    nombres_disponibles=[]
    print("Los siguientes son los nombres de productos que tenemos disponibles: ")
    for i in lista_catalogo:
            if producto==i["producto"]:
                nombres_disponibles.append(i["nombre"])
                print("nombre = "+i["nombre"]+" -> precio = "+i["precio"])
                print ("-------------------------------------------------------")
    ############# MOSTRAR PRODUCTOS ###################3

    nombre_escogido=input("Ingresa cual el nombre del producto que desea el cliente: ")
    nombre_escogido=nombre_escogido.lower()
    if nombre_escogido in nombres_disponibles: return nombre_escogido
    else:
        print("*Se debìa escoger uno de los nombres de producto presentados")
        return None

########################## TXT FECHAS ####################################

def fecha_pago_pedido():
    fecha_actual=datetime.datetime.now()
    fecha_actual=datetime.datetime.strftime(fecha_actual,"%d/%m/%Y - %H:%M:%S")
    return fecha_actual

def pagos_txt(usuario,total):
    fecha_actual=fecha_pago_pedido()
    with open("pagos_hechos.txt","a") as file:
        file.write("\n \n"+fecha_actual+"  -  "+usuario+"  -  "+str(total))

########################## REGISTRO PEDIDOS ####################################

def pedidos_productos(lista_catalogo,datos_pedidos):
    nombre_cliente=input("Ingrese el nombre del cliente que desea hacer un pedido: ")
    total=0
    try:
        if datos_pedidos[nombre_cliente]["pagado"]==False:
            print("* Ya se tenia un pedido anterior pero no està pagado, no se podrà hacer un nuevo pedido hasta que este se pague, si quiere cancelarlo ir al modulo cancelar \n")
            return None
        else:
            print("Ya se tenia un pedido anterior con este cliente, dado que está pago, el nuevo se sobreescribirá")
            try:
                datos_pedidos.pop(nombre_cliente)
            except:
                print("No hay pedido alguno a nombre de este cliente")
    except: None
    while True:
        ############### SE LE PIDE EL PRODUCTO ######################
        if lista_catalogo!=None:
            categoria=mostrar_categoria(lista_catalogo)
            if categoria!=None:
                producto=mostrar_productos(categoria,lista_catalogo)   
                if producto!=None:
                    nombre_producto=mostrar_nombres_precios(producto,lista_catalogo)
                else:
                    break
            else:
                break 
        else:
            break
        try:
            cantidad=int(input("Ingresa la cantidad de producto que desea: "))
        except:
            print("*Debias ingresar en cantidad un numero entero")
            break
        for i in lista_catalogo:
            if nombre_producto==i["nombre"]:
                precio=int(i["precio"])
        subtotal=cantidad*precio
        print("El total de esto serìa",subtotal)
        try:
            datos_pedidos[nombre_cliente][categoria].append({"producto":producto,
                                                                "nombre producto":nombre_producto,
                                                                "cantidad":cantidad,
                                                                "subtotal":subtotal
                                                                })
        except:
            try:           
                datos_pedidos[nombre_cliente][categoria]=[]
                datos_pedidos[nombre_cliente][categoria].append({"producto":producto,
                                                                    "nombre producto":nombre_producto,
                                                                    "cantidad":cantidad,
                                                                    "subtotal":subtotal
                                                                    })
            except:
                datos_pedidos[nombre_cliente]={}            
                datos_pedidos[nombre_cliente][categoria]=[]
                datos_pedidos[nombre_cliente][categoria].append({"producto":producto,
                                                                    "nombre producto":nombre_producto,
                                                                    "cantidad":cantidad,
                                                                    "subtotal":subtotal
                                                                    })
        salir=input("Desea salir y ver la orden completa del pedido (si) o realizar otro pedido (ingrese cualquier letra)")
        if salir=="si":
            for rcategorias in datos_pedidos[nombre_cliente]:
                print("*En ",rcategorias)
                for pedidos in datos_pedidos[nombre_cliente][rcategorias]:
                    print("*****************************************")
                    print("producto = ",pedidos["producto"])
                    print("nombre = ",pedidos["nombre producto"])
                    print("cantidad = ",pedidos["cantidad"])
                    print("subtotal = ",pedidos["subtotal"])
                    print("*****************************************")
            aceptado=False
            while aceptado==False:
                confirmar=input("si desea confirmar el pedido escriba (si) o (no)")
                if confirmar=="si":
                    identificador=input("Ingrese un identificador para el pedido puede ser lo que el cliente guste, un nombre, etc: ")
                    datos_pedidos[nombre_cliente]["identificador"]=identificador
                    datos_pedidos[nombre_cliente]["pagado"]=False
                    json_guardar_datos(datos_pedidos,RUTA_PEDIDOS)

                    aceptado=True
                elif confirmar=="no":
                    print("Entendido")
                    aceptado=True
                else:
                    print("Debes ingresar si o no")
            break
    json_guardar_datos(datos_pedidos,RUTA_PEDIDOS)

def pagar_pedido(datos_pedidos):
    fecha_actual=fecha_pago_pedido()
    nombre_cliente=input("Ingrese el nombre del cliente que desea pagar un pedido: ")
    total=0

    try:
        if datos_pedidos[nombre_cliente]["pagado"]==True:
            print("\n* El pedido ya està pagado no se puede modificar \n")
            return None
    except:
        None

    try:
        print("El pedido que tienes es: \n")
        for rcategorias in datos_pedidos[nombre_cliente]:
            if rcategorias=="pagado" or rcategorias=="identificador" or rcategorias=="fecha_pago":
                None
            else:
                print("*En ",rcategorias)
                for pedidos in datos_pedidos[nombre_cliente][rcategorias]:
                    print("producto = ",pedidos["producto"])
                    print("nombre = ",pedidos["nombre producto"])
                    print("cantidad = ",pedidos["cantidad"])
                    print("subtotal = ",pedidos["subtotal"])
                    print("*****************************************")
                    total+=pedidos["subtotal"]
    except:
        print("*El usuario no se encuentra en los usuarios con pedido \n")
        return None
    print("el total a pagar es",total)
    escoger=input("El cliente desea pagar el pedido? (si) (no): ")
    escoger=escoger.lower()
    if escoger=="si":
        None
    elif escoger=="no":
        print("No se cobrarà aun el pedido")
        return None
    else:
        print("Se debìa escoger (si) o (no)")
        return None
    try:
        recibido=int(input("Ingresa cuanto dinero te diò el cliente: "))
    except:
        print("El valor recibido debe ser un numero")
        return None
    if recibido<total:
        print("*El cliente diò menos dinero del valor del pedido, no se puede efectuar el pago \n")
        return None
    print("*COMPRA EXITOSA")
    print("*Devuelvele al cliente ",recibido-total,"\n")
    datos_pedidos[nombre_cliente]["pagado"]=True
    datos_pedidos[nombre_cliente]["fecha_pago"]=fecha_actual
    datos_pedidos[nombre_cliente]["total"]=total
    pagos_txt(nombre_cliente,total)
    json_guardar_datos(datos_pedidos,RUTA_PEDIDOS)

def cancelar_pedido(datos_pedido):
    nombre_cliente=input("Ingrese el nombre del cliente que desea cancelar un pedido: ")
    try:
        if datos_pedido[nombre_cliente]["pagado"]==False:
            datos_pedido.pop(nombre_cliente)
            print("*Pedido eliminado correctamente")
        else:
            print("\n *El pedido ya està pago, no se puede cancelar \n")
    except:
        print("No hay pedido alguno a nombre de este cliente")
    json_guardar_datos(datos_pedido,RUTA_PEDIDOS)

def modificar_pedido(datos_pedidos):
    nombre_cliente=input("Ingrese el nombre del cliente que desea modificar un pedido: ")
    try:
        if datos_pedidos[nombre_cliente]["pagado"]==True:
            print("* El pedido ya està pagado no se puede modificar \n")
            return None
    except:
        None
    print("El pedido es el siguiente: \n")
    ########################### MOSTRAR LOS PRODUCTOS DEL PEDIDO #################
    try:
        for rcategorias in datos_pedidos[nombre_cliente]:
            if rcategorias=="pagado" or rcategorias=="identificador":
                None
            else:
                print("*En ",rcategorias)
                for pedidos in datos_pedidos[nombre_cliente][rcategorias]:
                    print("producto = ",pedidos["producto"])
                    print("nombre = ",pedidos["nombre producto"])
                    print("cantidad = ",pedidos["cantidad"])
                    print("subtotal = ",pedidos["subtotal"])
                    print("*****************************************")
    except:
        print("*El usuario no se encuentra en los usuarios con pedido \n")
        return None
    
    opcion=input("Que desea modificar el cliente? ('eliminar' un producto del pedido especifico)('modificar' la cantidad de un producto en el pedido): ")

    if opcion=="eliminar":
        producto_a_eliminar=input("De los productos mostrados cual desea eliminar? (ingrese el nombre): ")
        try:
            for rcategorias in datos_pedidos[nombre_cliente]:
                if rcategorias=="pagado" or rcategorias=="identificador":
                    None
                else:
                    for pedidos in range(len(datos_pedidos[nombre_cliente][rcategorias])):
                        if datos_pedidos[nombre_cliente][rcategorias][pedidos]["nombre producto"]==producto_a_eliminar:
                            datos_pedidos[nombre_cliente][rcategorias].pop(pedidos)
                            print("*Producto eliminado correctamente")
                            if len(datos_pedidos[nombre_cliente][rcategorias])==0:
                                datos_pedidos[nombre_cliente].pop(rcategorias)
                            json_guardar_datos(datos_pedidos,RUTA_PEDIDOS)
                            return None
            print("*No se encontrò tal producto \n")
            return None
        except:
            print("*El usuario no se encuentra en los usuarios con pedido \n")
            return None
        
    elif opcion=="modificar":
        producto_a_modificar=input("De los productos mostrados cual desea modificar la cantidad comprada? (ingrese el nombre)")
        try:
            for rcategorias in datos_pedidos[nombre_cliente]:
                if rcategorias=="pagado" or rcategorias=="identificador"  :
                    None
                else:
                    for pedidos in datos_pedidos[nombre_cliente][rcategorias]:
                        if pedidos["nombre producto"]==producto_a_modificar:
                            print("Se tiene: nombre = ",pedidos["nombre producto"],"cantidad =",pedidos["cantidad"])
                            try:
                                cantidad=int(input("A cuanto desea modificar la cantidad de compra del producto: "))
                            except:
                                print("Se debe ingresar cantidad entera")
                                return None
                            precio=pedidos["subtotal"]//pedidos["cantidad"]
                            pedidos["cantidad"]=cantidad
                            pedidos["subtotal"]=precio*cantidad
                            print("*Modificacion completada exitosamente")
                            json_guardar_datos(datos_pedidos,RUTA_PEDIDOS)
                            return None
            print("*No se encontrò tal producto \n")
            return None
        except:
            print("*El usuario no se encuentra en los usuarios con pedido \n")
            return None
    else:
        print("*Se debìa escoger (modificar) o (eliminar)")
        return None

