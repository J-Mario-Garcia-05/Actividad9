def contar_destinos(destinos):
    if not destinos:
        return 0
    else:
        return 1 + contar_destinos(destinos[1:])

clientes = {}
opcion = "0"
while opcion != "4":
    print("\t==MENÚ==")
    print("1.Registrar clientes y destinos visitados")
    print("2.Mostrar clientes y destinos visitados")
    print("3.Mostrar total de destinos registrados")
    print("4.Salir")
    opcion = input("\nSeleccione una opción: ")
    try:
        match opcion:
            case "1":
                cantidad = int(input("¿Cuántos clientes desea registrar? (máximo 15): "))
                if cantidad < 1 or cantidad > 15:
                    print("Cantidad ingresada fuera de rango.")
                    continue
                for i in range(cantidad):
                    print(f"Ingrese los datos del cliente {i}:")
                    codigo = input("Código de cliente: ")
                    nombre = input("Nombre: ")
                    clientes[codigo] = {
                        "nombre": nombre,
                        "destino":{}
                    }
                    visitas = int(input("¿Cuantos destinos desea registrar? (máximo 5)"))
                    for i in range(visitas):
                        clave = input("Clave del destino:")
                        destino = input(f"Destino {i}: ")
                        clientes[codigo]["destino"][clave] =  {
                            "destino": destino,
                        }
            case "2":
                if clientes:
                    print("Clientes registrados:")
                    for codigo, cliente in clientes.items():
                        print(f"\nCódigo de cliente: {codigo}")
                        print(f"Nombre: {cliente['nombre']}")
                        for clave, destino in clientes[codigo]["destino"].items():
                            print(f"Destinos: {destino}", end="")
                else:
                    print("No hay clientes registrados")
    except Exception as e:
        print("Ha ocurrido un error: " + str(e))