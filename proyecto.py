asientos = [
" 1"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9","10","11","12","13","14","15",
"16","17","18","19","20","21","22","23","24","25","26","27",
"28","29","30","31","32","33","34","35","36","37","38","39","40","41","42"]
pasajeros =  {}


def asientos_avion():

    return print( "|"+ asientos[0]+" " +" "  + asientos[1] +" " +" "  + asientos[2]  +" "  +" " + asientos[3]+" " +" "  + asientos[4] +" " +" " + asientos[5] +"|"+"\n"
            +"|"+ asientos[6]+" " +" "  + asientos[7] +" " +" "  + asientos[8]  +" "  +" " + asientos[9]+" " +" "  + asientos[10] +" " +" " + asientos[11] +"|" +"\n"
            +"|"+ asientos[12]+" " +" "  + asientos[13] +" " +" "  + asientos[14]  +" "  +" " + asientos[15]+" " +" "  + asientos[16] +" " +" " + asientos[17] +"|" +"\n"
            +"|"+ asientos[18]+" " +" "  + asientos[19] +" " +" "  + asientos[20]  +" "  +" " + asientos[21]+" " +" "  + asientos[22] +" " +" " + asientos[23] +"|" +"\n"
            +"|"+ asientos[24]+" " +" "  + asientos[25] +" " +" "  + asientos[26]  +" "  +" " + asientos[27]+" " +" "  + asientos[28] +" " +" " + asientos[29] +"|" +"\n"
            +"|-----------"+ " ----------|" +"\n"
            +"|-----------"+ " ----------|" +"\n"
            +"|"+ asientos[30]+" " +" "  + asientos[31] +" " +" "  + asientos[32]  +" "  +" " + asientos[33]+" " +" "  + asientos[34] +" " +" " + asientos[35] +"|" +"\n"
            +"|"+ asientos[36]+" " +" "  + asientos[37] +" " +" "  + asientos[38]  +" "  +" " + asientos[39]+" " +" "  + asientos[40] +" " +" " + asientos[41] +"|")

entrada = 0

while entrada != "5":
    print(
        "[1] Ver asientos disponibles" + "\n" +
        "[2] Comprar asiento " + "\n" +
        "[3] Anular vuelo" + "\n" +
        "[4] Modificar datos de pasajero" + "\n" +
        "[5] Salir")
    
    entrada = input("Seleccione una Opcion: ")

    if entrada == "1":
        asientos_avion()
    if entrada == "2":
            asientos_avion()
            print("Porfavor Registre los Siguientes Datos A continuacion ... ")
            nombrePasajero = input("ingrese su Nombre: ")
            rutPasajero = int(input("ingrese su Rut: "))
            while rutPasajero < 5000000 or rutPasajero > 99999999:
              print('Ingrese un rut valido.')
              rutPasajero = int(input("ingrese su Rut: "))
            telefonoPasajero = int(input("ingrese su Telefono: "))
            while telefonoPasajero < 100000000 or telefonoPasajero > 999999999:
              print('Ingrese numero valido.')
              telefonoPasajero = int(input("ingrese su Telefono: "))
            bancoPasajero = input("ingrese al banco que Pertenece: ")
            
            print("Seleccione el asiento que desea Comprar: ")
            compra = input()
            index = int(compra)-1
            if int(compra) >42:
                print("El asiento ingresado esta fuera del Rango")
            else:    
                if asientos[index] == " x":
                    print("Este Asiento ya fue Comprado")
                else:
                    if int(compra) <=30:
                        asiento = int(compra) - 1
                        if bancoPasajero != "bancoduoc":
                            print("Asiento del tipo Normal... tiene un valor de $78.900")
                        else:
                            print("Asiento del tipo Normal... Usuario de bancoDuoc tiene un valor de $78.900 - el 15% =  $67.065")

                        ocupado = " x"
                        asientos.pop(asiento)
                        asientos.insert(asiento,ocupado)
                        pasajeros[asiento] = rutPasajero, nombrePasajero,telefonoPasajero,bancoPasajero
                        print(pasajeros)
                    if int(compra) >30 and int(compra) <=42:
                        asiento = int(compra) - 1
                        if bancoPasajero != "bancoduoc":
                            print("Asiento del tipo VIP... tiene un valor de $240.000")
                        else:
                            print("Asiento del tipo VIP... Usuario de bancoDuoc tiene un valor de $240.000 - el 15% =  $204.000")
                        ocupado = " x"
                        asientos.pop(asiento)
                        asientos.insert(asiento,ocupado)
                        pasajeros[asiento] = rutPasajero, nombrePasajero,telefonoPasajero,bancoPasajero
    if entrada == "3":
        asientos_avion()
        anular = input("Seleccione el pasaje que desea Anular: ")
        asiento = int(anular) - 1
        asientos.pop(asiento)
        asientos.insert(asiento,anular)
        pasajeros.pop(asiento)

    if entrada == "4":
        asientos_avion()
        print( "Pasajeros Registrados por Asiento: " + str(pasajeros))
        asiento_pasajero = input("Ingrese el Asiento del Pasajero: ")
        rut_pasajero = input("Ingrese el Rut del Pasajero: ")
        asiento = int(asiento_pasajero) - 1
        print(
                "[1] Modificar Nombre Pasajero" + "\n" +
                "[2] Modificar Numero Telefonico" + "\n")
        entrada = input("Seleccione una Opcion: ")     
