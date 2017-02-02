'''
Created on Feb 1, 2017

@author: gabriel
@author: ale
'''
import datetime

class Registro:
    def __init__(self, monto, fecha, idEstablecimiento):
        self.monto = monto
        self.fecha = fecha
        self.idEstablecimiento = idEstablecimiento
    
    def devMonto(self):
        return self.monto
        
class BilleteraElectronica:
    def __init__(self, nombre = None,apellido = None, ci = None,pin = None,id = None):
        self.Nombre=nombre
        self.Apellido=apellido
        self.Cedula=ci
        self.PIN=pin
        self.id=id
        self.regRecarga = []
        self.regConsumo = []
        self.saldoTotal = 0
        
    def saldo(self):
        return self.saldoTotal
    
    def recargar(self, monto, fecha, idEstablecimiento):
        registro = Registro(monto, fecha, idEstablecimiento)
        self.regRecarga.append(registro)
        self.saldoTotal+= registro.devMonto()
        print(self.regRecarga[-1].fecha)
