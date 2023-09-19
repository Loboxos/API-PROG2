from ..database import DatabaseConnection

class Chat:
    
    def __init__(self, id_chat, hora_mensaje, mensaje, menciones, id_canal):
        self.id_chat = id_chat
        self.hora_mensaje = hora_mensaje
        self.mensaje = mensaje
        self.menciones = menciones
        self.id_canal = id_canal