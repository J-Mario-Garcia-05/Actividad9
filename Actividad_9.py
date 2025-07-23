def contar_destinos(destinos):
    if destinos == "":
        return 0

clientes = {}
opcion = "0"
while opcion != "4":
    print("\n\t==MENÚ==")
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
                    visitas = int(input("¿Cuantos destinos desea registrar? (máximo 5): "))
                    for j in range(visitas):
                        clave = input("Código del destino:")
                        destino = input(f"Destino {j + 1}: ")
                        clientes[codigo]["destino"][clave] =  {
                            "destino": destino,
                        }
            case "2":
                if clientes:
                    print("Clientes registrados:")
                    for codigo, cliente in clientes.items():
                        print(f"\nCódigo de cliente: {codigo}")
                        print(f"Nombre: {cliente['nombre']}")
                        print("Destinos:", end=" ")
                        for clave, destino in clientes[codigo]["destino"].items():
                            print(f"{destino['destino']}", end=" ")
                else:
                    print("No hay clientes registrados")
            case "3":
                if clientes:
                    contador = 0
                    visitas = 0
                    mayor_visitante = ""
                    for codigo, cliente in clientes.items():
                        contador = contar_destinos(cliente["destino"])
                        if contador > visitas:
                            visitas = contador
                            mayor_visitante = cliente["nombre"]
                    print("Total de destinos registrados: ", mayor_visitante)
                else:
                    print("No hay clientes registrados")
            case "4":
                print("Saliendo...")
            case __:
                print("Opción no disponible")
    except Exception as e:
        print("Ha ocurrido un error: " + str(e))