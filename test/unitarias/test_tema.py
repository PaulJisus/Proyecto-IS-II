import unittest
from ...backend.models.tema import Tema

class TestTema(unittest.TestCase):
    def setUp(self):
        self.tema = Tema(2,"Grafos")

    def test_set_nombre(self):
        self.tema.set_nombre("Nuevo tema")
        self.assertEqual(self.tema.get_nombre(), "Nuevo tema")

if __name__ == '__main__':
    unittest.main()