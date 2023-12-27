class Nombre:
    def __init__(self, nombres_, apellido_):
        self.nombres = nombres_
        self.apellido = apellido_

    def full(self):
        return "{} {}".format(self.nombres, self.apellido)

class UsuarioModel:
    def __init__(self, id_, nombre_, apellido_, correo_):
        self.id = id_
        self.nombre_completo = Nombre(nombre_, apellido_)
        self.correo = correo_
    
    def get_id(self):
        return self.id

    def set_nombre(self, nombre_, apellido_):
        self.nombre_completo = Nombre(nombre_,apellido_)
    def get_nombre(self):
        return self.nombre_completo.full()
    
    def set_correo(self, correo_):
        self.correo = correo_
    def get_correo(self):
        return self.correo
