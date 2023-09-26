from ..database import DatabaseConnection

class Chat:
    
    def __init__(self, id_chat, fecha_mensaje, mensaje, menciones, id_canal):
        self.id_chat = id_chat
        self.fecha_mensaje = fecha_mensaje
        self.mensaje = mensaje
        self.menciones = menciones
        self.id_canal = id_canal
        
        
    @classmethod
    def obtener_mensaje(cls, id_canal):
        query = '''
        SELECT
        chat.id_chat,
        chat.fecha_mensaje,
        chat.mensaje,
        chat.menciones
        FROM chat
        JOIN canal ON chat.id_canal = canal.id_canal
        WHERE
        canal.id_canal = %s
        '''
        
        params = (id_canal,)
        result = DatabaseConnection.fetch_one(query, params)
        
        if result is not None:
            return Chat(
               id_chat = result[0],
               fecha_mensaje = result[1],
               mensaje = result[2],
               menciones = result[3]
            )
        else:
         return "NO HAY MENSAJES EN ESTE CANAL"
     
     