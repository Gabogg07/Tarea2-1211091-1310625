'''
Created on Feb 1, 2017

@author: gabriel
@author: ale
'''
class Registro:
    def __init__(self, monto, fecha, idEstablecimiento):
        self.monto = monto
        self.fecha = fecha
        self.idEstablecimiento = idEstablecimiento
        
class BilleteraElectronica(object):
    def __init__(self, nombre = None,apellido = None, ci = None,pin = None,id = None):
        self.Nombre=nombre
        self.Apellido=apellido
        self.Cedula=ci
        self.PIN=pin
        self.id=id
        self.regRecarga = []
        self.regConsumo = []
        self.saldoTotal = 0
        
    