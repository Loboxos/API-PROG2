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
        SELECT
        s.id_servidor,
        s.logo,
        s.nombre,
        s.descripcion,
        s.region,
        s.miembros,
        s.creador,
        s.fecha_creacion,
        u.id_usuario
        FROM servidores s
        JOIN usuario u ON s.usuario_id = u.usuario_id
        WHERE u.usuario_id = %s
        '''
        
        params = (usuario_id,)
        results = DatabaseConnection.fetch_one(query, params)
        
        if results is not None:
            return Servidores(
                id_servidor=results[0],
                logo=results[1],
                nombre=results[2],
                descripcion=results[3],
                region=results[4],
                miembros=results[5],
                creador=results[6],
                fecha_creacion=results[7],
            )
        else:
            return "NO HAY SERVIDORES EN ESTA USUARIO"
        
    @classmethod 
    def crear_servidor(cls, servidor):
        query = '''
        INSERT INTO servidores (nombre, descripcion, region, miembros, creador, fecha_creacion)
        VALUES (%s, %s, %s, %s, %s, %s)
        '''
        
        values = (servidor.nombre, servidor.descripcion, servidor.region, servidor.miembros, servidor.creador, servidor.fecha_creacion)
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        return True
        
        