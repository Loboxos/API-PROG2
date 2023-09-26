from ..database import DatabaseConnection
import mysql.connector


class Canales:
    
    def __init__(self, id_canal, nombre, id_servidor, descripcion):
        self.id_canal = id_canal
        self.nombre = nombre
        self.id_servidor = id_servidor
        self.descripcion = descripcion
        
    @classmethod
    def mostrar_canales(cls, id_servidor):
        query = '''
        SELECT
        id_canal,
        nombre,
        id_servidor,
        descripcion
        FROM canales c
        JOIN servidores s ON c.servidor_id = s.servidor_id
        JOIN usuarios u ON s.usuario_id = u.usuario_id
        WHERE u.usuario_id = %s AND s.servidor_id = %s
        '''
        params = (id_servidor,)
        results = DatabaseConnection.fetch_one(query, params)
        if results is not None:
            return Canales(
                id_canal=results[0],
                nombre=results[1],
                id_servidor=results[2],
                descripcion=results[3]
            )
        else:
            return "NO EXISTE EL CANAL"
    
    @classmethod
    def crear_canal(cls, nombre, id_servidor,descripcion):
        query = '''
        INSERT INTO canales (nombre, id_servidor, descripcion)
        VALUES (%s, %s ,%s)
        '''
        values = (nombre, id_servidor)

        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            return True
        except mysql.connector.IntegrityError as e:
            cursor.close()
            return "Error al crear el canal. Asegúrate de que el servidor exista."

