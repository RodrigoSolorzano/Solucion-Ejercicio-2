from datetime import datetime

"""
Ejercicio 02

finanzas personales (ingresos y egresos)

hacer un programa python para consola que le permita al usuario:

1. iniciar un proyecto de finanzas personales con cuenta a 0.00
2. dar opcion para registrar un ingreso o un egreso
3. si es un ingreso sumarlo a la cuenta
4. si es un egreso restarlo a la cuenta
5. verficar que si es un egreso y la cuenta esta a 0.0 debe aparecer
    el monto en negativo.
6. poder generar un reporte de todos los ingresos
7. poder generar un reporte de todos lo egresos
8. poder generar un reporte de todas las transacciones (ingresos y egreso)
9. poder generar un reporte solo de el total de la cuenta

restricciones del ejercicio:
el proyecto finanzas debe ser una clase, un ingreso debe ser una clase
y un egreso debe ser una clase tambien.

"""


class Finanzas:
    def __init__(self):
        self.Cuenta = 0.0
        self.TotalList = []

    def getTotalCuenta(self, ingreso, egreso):
        self.Cuenta = ingreso + egreso
        return self.Cuenta


class Ingresos:
    def __init__(self):

        self.Ingresos = 0.0
        self.ingresosList = []

    def registrarIngreso(self, MontoI):
        Finanzas()
        self.Date = str(datetime.today())
        ingresosDict = {
            "monto:": MontoI,
            "Tipo de transacción:": "Ingreso",
            "fecha de Ingreso:": self.Date,
        }
        self.Ingresos = self.Ingresos + MontoI
        self.ingresosList.append(ingresosDict)

    def getListaIngresos(self):
        return self.ingresosList

    def getTotalIngresos(self):
        return self.Ingresos


class Egresos:
    def __init__(self):
        Finanzas()
        self.egresosList = []
        self.Egresos = 0.0

    def registrarEgreso(self, MontoE):
        self.Date = str(datetime.today())
        egresosDict = {
            "monto:": (-MontoE),
            "Tipo de transacción:": "Egreso",
            "fecha de Egreso": self.Date,
        }
        self.Egresos = self.Egresos - MontoE
        self.egresosList.append(egresosDict)

    def getListaEgresos(self):
        return self.egresosList

    def getTotalEgresos(self):
        return self.Egresos
