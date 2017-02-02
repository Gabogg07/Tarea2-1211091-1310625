'''
Created on Feb 1, 2017

@author: Gabriel Gutierrez 13-10625
@author: Alessandra Marrero 12-11091
'''
import unittest
import datetime
import math
from Billetera import *


class Test(unittest.TestCase):

    def setUp(self):
        self.persona=BilleteraElectronica("Gabriel","Gutierrez",24723958,192,987654321)
        
    def testBilletera(self):
        assert(self.persona.nombreValido()), "Atributo nombre invalido."
        assert(self.persona.apellidoValido()), "Atributo apellido invalido."
        self.assertEqual(self.persona.Nombre, "Gabriel", "Error en el nombre")
        self.assertEqual(self.persona.Apellido, "Gutierrez", "Error en el apellido")
        self.assertEqual(self.persona.Cedula,24723958,"Error en la cedula")
        self.assertEqual(self.persona.PIN, 192, "Error en el pin")
        self.assertEqual(self.persona.id, 987654321, "Error en el identificador")
    
    def testSaldo(self):
        self.assertEqual(self.persona.saldo(),0, "Error al ver el saldo disponible")
        
    def testRecargar(self):
        recargar=Registro(10000,datetime.date.today(),150)
        self.persona.recargar(recargar)
        self.assertEqual(self.persona.regRecarga[-1], recargar,"Error en la recarga")
        
    def testConsumir(self):
        recargar=Registro(10000,datetime.date.today(),150)
        self.persona.recargar(recargar)
        consumo = Registro(20, datetime.date.today(), 200)
        self.persona.consumir(consumo, 192)
        self.assertEqual(self.persona.regConsumo[-1], consumo, "Error en el consumo")
    
    def testFrontera1Recargar(self):
        recargar=Registro(0,datetime.date.today(),150)
        self.persona.recargar(recargar)
        self.assertEqual(self.persona.regRecarga[-1], recargar,"Error en la recarga")
    
    def testFrontera2Recargar(self):
        num= float("inf")
        recargar=Registro(num,datetime.date.today(),150)
        self.persona.recargar(recargar)
        self.assertEqual(self.persona.regRecarga[-1], recargar,"Error en la recarga")
    
    #Caso Interior
    def testEsquina1Recargar(self):
        recargar=Registro(0.1,datetime.date.today(),150)
        self.persona.recargar(recargar)
        self.assertEqual(self.persona.regRecarga[-1], recargar,"Error en la recarga")
    
    #Caso Interior
    def testEsquina2Recargar(self):
        num= float("inf")
        recargar=Registro(num-0.1,datetime.date.today(),150)
        self.persona.recargar(recargar)
        self.assertEqual(self.persona.regRecarga[-1], recargar,"Error en la recarga")
    
    #Se hace una recarga negativa
    def testMaliciaRecarga(self):
        recargar=Registro(-1 ,datetime.date.today(),150)
        try:
            self.persona.recargar(recargar)
        except:
            pass
        
    def testFrontera1Consumir(self):
        recargar=Registro(10000,datetime.date.today(),150)
        self.persona.recargar(recargar)
        consumo = Registro(10000, datetime.date.today(), 200)
        self.persona.consumir(consumo, 192)
        self.assertEqual(self.persona.regConsumo[-1], consumo, "Error en el consumo")
    
    def testFrontera2Consumir(self):
        num= float("inf")
        recargar=Registro(num,datetime.date.today(),150)
        self.persona.recargar(recargar)
        consumo = Registro(num, datetime.date.today(), 200)
        self.persona.consumir(consumo, 192)
        self.assertEqual(self.persona.regConsumo[-1], consumo, "Error en el consumo")
    
    #Caso Interior
    def testEsquina1Consumir(self):
        recargar=Registro(10001,datetime.date.today(),150)
        self.persona.recargar(recargar)
        consumo = Registro(10000, datetime.date.today(), 200)
        self.persona.consumir(consumo, 192)
        self.assertEqual(self.persona.regConsumo[-1], consumo, "Error en el consumo")
    
    #Caso Interior
    def testEsquina2Consumir(self):
        num= float("inf")
        recargar=Registro(num,datetime.date.today(),150)
        self.persona.recargar(recargar)
        consumo = Registro(num-1, datetime.date.today(), 200)
        self.persona.consumir(consumo, 192)
        self.assertEqual(self.persona.regConsumo[-1], consumo, "Error en el consumo")
     
    #Se hace un consumo mayor al saldo disponible
    def testMaliciaConsumir(self):
        recargar=Registro(10,datetime.date.today(),150)
        self.persona.recargar(recargar)
        consumo = Registro(10000, datetime.date.today(), 200)
        try:
            self.persona.consumir(consumo, 102)
        except:
            pass
        
    #Se hace un consumo negativo
    def testMalicia1Consumir(self):
        recargar=Registro(10,datetime.date.today(),150)
        self.persona.recargar(recargar)
        consumo = Registro(-10000, datetime.date.today(), 200)
        try:
            self.persona.consumir(consumo, 102)
        except:
            pass
        
        
    def testApellidoValido(self):
        assert(self.persona.apellidoValido()), "Atributo apellido invalido."
        
    def testNombreValido(self):
        assert(self.persona.nombreValido()), "Atributo nombre invalido."
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()