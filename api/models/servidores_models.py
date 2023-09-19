from ..database import DatabaseConnection

class Servidores:
    
    def __init__(self, id_servidor, logo, nombre, descripcion, region, miembros, creador, fecha_creacion, id_usuario):
        self.id_servidor = id_servidor
        self.logo = logo
        self.nombre = nombre
        self.descripcion = descripcion
        self.region = region
        self.miembros = miembros
        self.creador = creador
        self.fecha_creacion = fecha_creacion
        self.id_usuario = id_usuario