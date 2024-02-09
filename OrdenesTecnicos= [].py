
Ordenes= []
continuar = True
Tecnicos=[]

while continuar:
    print("------------ menu ------------")
    print("1. ingresar datos")
    print("2. leer ordenes datos de ordenes")
    print("3. leer datos de tecnicos")
    opcion=int(input("escoja uno: "))
    print("------------  ------------")
    print("------------  ------------")
    if opcion == 1:
        print("que desea ingresar")
        print("1. ingresar ordenes normales")
        print("2. ingresar ordenes con garantia")
        print("3. ingresar nombres de tecnicos")
        seleccion=int(input("seleccione una opcion: "))
        print("------------  ------------")
        print("------------  ------------")
        if seleccion ==1:
            OrdenNormal={}
            print("escriba los datos que se piden para incluirlos dentro de la orden: ")
            datos={}
            nombre=input("escriba el nombre del cliente: ")
            fecha=input("en que fecha ingreso el vehiculo: ")
            fechaRepa=input("fecha de inicio de reparacion: ")
            finalRepa=input("fecha en que finalizo: ")
            precio=input("precio que costo la reparacion: ")
            tecnicoatendiendo=input("tecnico que atendio: ")
            tecnico={}
            datos["datos"]=nombre,fecha,fechaRepa,finalRepa,precio,tecnicoatendiendo
            tecnico["tecnicos"]=tecnicoatendiendo
            OrdenNormal["ordenes normales"]=datos
            Ordenes.append(OrdenNormal)
            Tecnicos.append(tecnico)
            
        elif seleccion==2:
            OrdenGarantia={}
            print("escriba los datos que se piden para incluirlos dentro de la orden: ")
            datos={}
            nombre=input("escriba el nombre del cliente: ")
            fecha=input("en que fecha ingreso el vehiculo: ")
            fechaRepa=input("fecha de inicio de reparacion: ")
            finalRepa=input("fecha en que finalizo: ")
            Refer=input("numero de referencia de la garantia: ")
            tecnicoatendiendo=input("tecnico que atendio: ")
            tecnico={}
            tecnico["tecnicos"]=tecnicoatendiendo
            datos["datos"]=nombre,fecha,fechaRepa,finalRepa,Refer,tecnicoatendiendo
            OrdenGarantia["orden con garantia"]=datos
            Ordenes.append(OrdenGarantia)
            Tecnicos.append(tecnico)
        elif seleccion==3:
            Tecnico={}
            nombre=input("escriba el nombre del tecnico: ")
            Tecnico["Tecnicos"]=nombre
            Ordenes.append(Tecnico)
    elif opcion==2:
        print("leyendo datos")
        print("leyendo datos")
        for i in range(len(Ordenes)):
            print(Ordenes[i])
            print("")
        
        for i in range(len(Tecnicos)):
            print(Tecnicos[i], end=" ")

        """for i in range(len(OrdenesTecnicos)):
            for j in range(len(OrdenesTecnicos)):
                print(OrdenesTecnicos[j][i])
                este imprime primero el nombre de las sublistas de ahi los diccionarios no se como mejorarlo
                """
