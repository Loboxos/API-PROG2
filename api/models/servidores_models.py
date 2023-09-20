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
        
    @classmethod
    def obtener_servidores_de_usuario(cls, usuario_id):
        query = '''
        SELECT s.*
        FROM servidores s
        JOIN usuario u ON s.usuario_id = u.usuario_id
        WHERE u.usuario_id = %s
        '''
        
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, (usuario_id,))
        servidores = cursor.fetchall()
        cursor.close()
        
        if not servidores:
            return "El usuario no pertenece a ningún servidor."
    
        return servidores