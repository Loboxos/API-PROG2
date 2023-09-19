from ..database import DatabaseConnection

class Usuario:
    def __init__(self, id_usuario, nombre, apellido, fecha_de_nacimiento, contraseña, apodo, avatar):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.contraseña = contraseña
        self.apodo = apodo
        self.avatar = avatar
        