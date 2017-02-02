'''
Created on Feb 1, 2017

@author: Gabriel Gutierrez 13-10625
@author: Alessandra Marrero 12-11091
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
        self.Nombre = nombre
        self.Apellido = apellido
        self.Cedula = ci
        self.PIN = pin
        self.id = id
        self.regRecarga = []
        self.regConsumo = []
        self.saldoTotal = 0
        
    def nombreValido(self):
        if self.Nombre.isalpha() and self.Nombre is not None:
            return True
        else: 
            return False
     
    def apellidoValido(self):
        if self.Apellido.isalpha() and self.Apellido is not None:
            return True
        else: 
            return False
        
    def saldo(self):
        return self.saldoTotal
    
    def recargar(self, registro):
        if (registro.monto < 0):
            print("El monto debe de ser positivo")
            assert(registro.monto>=0)
        self.regRecarga.append(registro)
        self.saldoTotal+= registro.monto

    def consumir(self, consumo, pin):
        if (pin != self.PIN):
            print( "El PIN no es valido")
            assert(pin==self.PIN)
        elif (self.saldoTotal < consumo.monto):
            return "Su saldo no es suficiente"
        elif (consumo.monto < 0):
            return "El monto del consumo no puede ser negativo"
        else:
            self.regConsumo.append(consumo)
            self.saldoTotal -= consumo.monto        