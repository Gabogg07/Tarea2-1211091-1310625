'''
Created on Feb 1, 2017

@author: gabriel
'''
import unittest
from Billetera import Usuario


class TestBilletera(unittest.TestCase):


    def testUsuario(self):
        persona=Usuario("Gabriel","Gutierrez",24723958,192,987654321)
        self.assertEqual(persona.Nombre, "Gabriel", "error en el nombre")
        self.assertEqual(persona.Apellido, "Gutierrez", "error en el apellido")
        self.assertEqual(persona.Cedula,24723958,"error en la cedula")
        self.assertEqual(persona.PIN, 192, "error en el pin")
        self.assertEqual(persona.id, 987654321, "error en el identificador")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()