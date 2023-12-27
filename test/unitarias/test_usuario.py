import unittest
from ...backend.models.usuario import UsuarioModel


class TestUsuario(unittest.TestCase):
    def setUp(self):
        self.usuario = UsuarioModel(2,"Nombre","Apellido","Correo")

    def test_set_nombre(self):
        self.usuario.set_nombre("Nuevo nombre","Nuevo apellido")
        self.assertEqual(self.usuario.get_nombre(), "Nuevo nombre Nuevo apellido")

    def test_set_correo(self):
        self.usuario.set_correo("Nuevo correo")
        self.assertEqual(self.usuario.get_correo(), "Nuevo correo")
    

if __name__ == '__main__':
    unittest.main()