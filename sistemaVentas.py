import misfunciones as mf

while True:
    mf.limpiarPantalla()
    mf.titulo("BookStore")
    mf.printRojo("""
    1) Registrar libro
    2) Listar libro
    3) Imprimir certidicado 
    0) Salir
    """)
    opcion = int(input("Seleccione -->"))
    if opcion == 0:
        mf.printVerde("Adios")
        break
    elif opcion ==1:
        mf.titulo("REGISTRAR LIBRO")
        codigo = int(input("Ingrese codigo del libro -->"))
        titulo = input("Ingrese titulo del libro -->").capitalize()
        autor = input("Ingrese autor del libro -->").capitalize()
        precio = int(input("Ingrese precio del libro -->"))
        mf.guardarLibro(codigo,titulo,autor,precio)
    elif opcion ==2:
        mf.titulo("LISTAR LIBRO")
        codigo = int(input("Ingrese codigo del libro -->"))
        mf.listarLibro(codigo)
    elif opcion ==3:
        while True:
            mf.printRojo("""
            1) Imprimir criticas
            2) Detalle de ventas
            0) Salir
            """)
            opcion2 = int(input("Seleccione -->"))
            if opcion2 == 0:
                break
            elif opcion2 ==1:
                mf.titulo("IMPRIMIR CRITICAS")
                codigo = int(input("Ingrese codigo del libro -->"))
                mf.criticasLibro(codigo)
                break
            elif opcion2 ==2:
                mf.titulo("DETALLE DE VENTAS")
                codigo = int(input("Ingrese codigo del libro -->"))
                mf.detalleVentas(codigo)
                break
            else:
                mf.printERROR("Opcion no valida")
    else:
        mf.printERROR("Opcion invalida!")
