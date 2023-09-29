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
                c.id_canal,
                c.nombre AS canal_nombre,
                c.id_servidor,
                c.descripcion,
                s.nombre AS servidor_nombre
            FROM canales c
            JOIN servidores s ON c.id_servidor = s.id_servidor
            JOIN usuarios u ON s.id_usuario = u.id_usuario
            WHERE u.id_usuario = %s AND s.id_servidor = %s
        '''
        params = (id_servidor,id_servidor)
        results = DatabaseConnection.fetch_all(query, params)
        
        canales = []
        for result in results:
            canales.append({
                "id_canal":result[0],
                "nombre":result[1],
                "id_servidor":result[2],
                "descripcion":result[3]
                
            }) 
        if canales:
            return canales
        else:
            return "NO EXISTEN CANALES EN EL SERVIDOR"
    
    @classmethod
    def crear_canal(cls, canal):
        query = '''
        INSERT INTO canales (nombre, id_servidor, descripcion)
        VALUES (%s, %s ,%s)
        '''
        values = (canal.nombre, canal.id_servidor, canal.descripcion)

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

