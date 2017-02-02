'''
Created on Feb 1, 2017

@author: gabriel
@author: ale
'''
import unittest
from Billetera import *


class Test(unittest.TestCase):

    def setUp(self):
        self.persona=BilleteraElectronica("Gabriel","Gutierrez",24723958,192,987654321)
        
    def testBilletera(self):
        self.assertEqual(self.persona.Nombre, "Gabriel", "Error en el nombre")
        self.assertEqual(self.persona.Apellido, "Gutierrez", "Error en el apellido")
        self.assertEqual(self.persona.Cedula,24723958,"Error en la cedula")
        self.assertEqual(self.persona.PIN, 192, "Error en el pin")
        self.assertEqual(self.persona.id, 987654321, "Error en el identificador")
    
    def testSaldo(self):
        self.assertEqual(self.persona.saldo(), 0, "Error al ver el saldo disponible")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()