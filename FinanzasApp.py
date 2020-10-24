from tusFinanzas import Finanzas, Ingresos, Egresos


# 1. iniciar un proyecto de finanzas personales con cuenta a 0.00
# 2. dar opcion para registrar un ingreso o un egreso
# 3. si es un ingreso sumarlo a la cuenta
# 4. si es un egreso restarlo a la cuenta
# 5. verficar que si es un egreso y la cuenta esta a 0.0 debe aparecer
#     el monto en negativo.
# 6. poder generar un reporte de todos los ingresos
# 7. poder generar un reporte de todos lo egresos
# 8. poder generar un reporte de todas las transacciones (ingresos y egreso)
# 9. poder generar un reporte solo de el total de la cuenta

print("Inicio FinanzasApp: \n")
objFinanza = Finanzas()
objIngreso = Ingresos()
objEgreso = Egresos()


def registrarIngreso():
    print("\n**registrar un ingreso**\n")
    Monto = float(input("Ingreso: "))
    objIngreso.registrarIngreso(Monto)


def registrarEgreso():
    print("\n**registrar un Egreso**\n")
    MontoE = float(input("Egreso: "))
    objEgreso.registrarEgreso(MontoE)


def generarReporteIngresos():

    print("\n**Reporte Ingresos**\n")
    ingresos = objIngreso.getListaIngresos()
    if len(ingresos) > 0:
        for ingreso in ingresos:
            print(ingreso)
        I = objIngreso.getTotalIngresos()
        print("\n Total de ingresos: $ " + str(I))
    else:
        print("\n**no hay Ingresos por el momento**\n")


def generarReporteEgresos():
    print("\n**Reporte Egresos**\n")
    egresos = objEgreso.getListaEgresos()
    if len(egresos) > 0:
        for egreso in egresos:
            print(egreso)
        E = objEgreso.getTotalEgresos()
        print("\n Total de Egresos: $ " + str(E))
    else:
        print("\n**no hay Egresos por el momento**\n")


def ObtenerSaldo():
    print("\n")
    Ingresos = objIngreso.getTotalIngresos()
    Egresos = objEgreso.getTotalEgresos()
    total = objFinanza.getTotalCuenta(Ingresos, Egresos)
    print("El total de la cuenta es " + str(total))


def ObtenerTransacciones():
    print("\n")
    Ingresos = objIngreso.getListaIngresos()
    Egresos = objEgreso.getListaEgresos()
    if len(Ingresos) > 0 or len(Egresos) > 0:
        resultado = Ingresos + Egresos
        print("El total de transacciones son: \n ")
        for transaccion in resultado:
            print(transaccion)
    else:
        print("\n**no hay ingresos ni egresos por el momento**\n")


while True:
    print("\n Menu: \n")
    print("(0) salir")
    print("(1) registrar un ingreso")
    print("(2) registrar un egreso")
    print("(3) reporte de los ingresos")
    print("(4) reporte de los egresos")
    print("(5) Obtener saldo total de la cuenta")
    print("(6) Obtener todas las transacciones\n")
    option = int(input("opcion: "))
    if option == 0:
        print("termino FinanzasApp\n")
        break
    elif option == 1:
        registrarIngreso()
    elif option == 2:
        registrarEgreso()
    elif option == 3:
        generarReporteIngresos()
    elif option == 4:
        generarReporteEgresos()
    elif option == 5:
        ObtenerSaldo()
    elif option == 6:
        ObtenerTransacciones()