'''
Created on Feb 1, 2017

@author: gabriel
'''
import unittest
from Billetera import BilleteraElectronica


class TestBilleteraElectronica(unittest.TestCase):


    def testBilletera(self):
        persona=BilleteraElectronica("Gabriel","Gutierrez",24723958,192,987654321)
        self.assertEqual(persona.Nombre, "Gabriel", "Error en el nombre")
        self.assertEqual(persona.Apellido, "Gutierrez", "Error en el apellido")
        self.assertEqual(persona.Cedula,24723958,"Error en la cedula")
        self.assertEqual(persona.PIN, 192, "Error en el pin")
        self.assertEqual(persona.id, 987654321, "Error en el identificador")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()