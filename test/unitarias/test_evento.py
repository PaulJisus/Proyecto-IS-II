import unittest

from ...backend.models.evento import EventoModel
class TestEvento(unittest.TestCase):
    def setUp(self):
        self.evento = EventoModel(2,2,2,"Ejemplo","Este es un ejemplo","link")

    def test_set_nombre(self):
        self.evento.set_nombre("Nuevo nombre")
        self.assertEqual(self.evento.get_nombre(), "Nuevo nombre")

    def test_set_detalles(self):
        self.evento.set_detalles("Nuevos detalles")
        self.assertEqual(self.evento.get_detalles(), "Nuevos detalles")
    
    def test_set_link(self):
        self.evento.set_link("Nuevo link")
        self.assertEqual(self.evento.get_link(), "Nuevo link")


if __name__ == '__main__':
    unittest.main()