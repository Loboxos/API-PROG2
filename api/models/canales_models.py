from ..database import DatabaseConnection

class Canales:
    
    def __init__(self, id_canal, nombre, id_servidor):
        self.id_canal = id_canal
        self.nombre = nombre
        self.id_servidor = id_servidor
        