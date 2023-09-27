from ..database import DatabaseConnection

class Servidores:
    
    def __init__(self, id_servidor ,nombre, descripcion, region, miembros, creador, fecha_creacion, id_usuario,logo=None):
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
    def obtener_servidores(cls, id_usuario):
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
        JOIN usuarios u ON s.id_usuario = u.id_usuario
        WHERE u.id_usuario = %s
        '''
        
        params = (id_usuario,)
        results = DatabaseConnection.fetch_all(query, params)

        servidores = []

        for result in results:
            servidores.append({
                    "id_servidor":result[0],
                    "logo":result[1],
                    "nombre":result[2],
                    "descripcion":result[3],
                    "region":result[4],
                    "miembros":result[5],
                    "creador":result[6],
                    "fecha_creacion":result[7],
                    "id_usuario":result[8]
                })
        if servidores:
            return servidores
        else:
            return "NO HAY SERVIDORES PARA ESTE USUARIO"
        
        # for row in results:
        #     servidor = Servidores(
        #         id_servidor=row[0],
        #         logo=row[1],
        #         nombre=row[2],
        #         descripcion=row[3],
        #         regi=row[4],
        #         miembros=row[5],
        #         creador=row[6],
        #         fecha_creacion=row[7],
        #         id_usuario=row[8]
        #     )
        #     servidores.append(servidor)
        # if servidores:
        #     return servidores
        # else:
        #     return "NO HAY SERVIDORES PARA ESTE USUARIO"
            
    @classmethod 
    def crear_servidor(cls, servidor):
        query = '''
        INSERT INTO servidores (nombre, descripcion, region, miembros, creador, fecha_creacion , id_usuario)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        '''
        
        values = (servidor.nombre, servidor.descripcion, servidor.region, servidor.miembros, servidor.creador, servidor.fecha_creacion ,servidor.id_usuario)
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        return True
        
        