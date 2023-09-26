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
        
        servidores = []
        for row in results:
            servidor = Servidores(
                id_servidor=row[0],
                logo=row[1],
                nombre=row[2],
                descripcion=row[3],
                region=row[4],
                miembros=row[5],
                creador=row[6],
                fecha_creacion=row[7],
            )
        servidores.append(servidor)

        if servidores:
            return servidores
        else:
            return "NO HAY SERVIDORES PARA ESTE USUARIO"
            
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
        
        