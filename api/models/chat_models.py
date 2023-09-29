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
        JOIN canales ON chat.id_canal = canales.id_canal
        WHERE
            canales.id_canal = %s
        ORDER BY chat.fecha_mensaje ASC;

        '''
        
        params = (id_canal,)
        results = DatabaseConnection.fetch_all(query, params)
        
        print(results)
        chats = []
        
        if results is not None:

            for result in results:
                chats.append({
                    "id_chat":result[0],
                    "fecha_mensaje":result[1],
                    "mensaje":result[2],
                    "menciones":result[3]
                })
            print(chats)
            return chats
        else:
            return "NO HAY MENSAJES EN ESTE CANAL"
     
     