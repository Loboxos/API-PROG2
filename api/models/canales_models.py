from ..database import DatabaseConnection
import mysql.connector


class Canales:
    
    def __init__(self, id_canal, nombre, id_servidor):
        self.id_canal = id_canal
        self.nombre = nombre
        self.id_servidor = id_servidor
        
    @classmethod
    def mostrar_canales(cls, id_servidor):
        query = '''
        SELECT c.*
        FROM canales c
        JOIN servidores s ON c.servidor_id = s.servidor_id
        JOIN usuarios u ON s.usuario_id = u.usuario_id
        WHERE u.usuario_id = %s AND s.servidor_id = %s
        '''
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, id_servidor)
        canales = cursor.fetchall()
        cursor.close()
    
        if not canales:
            return "No hay canales asociados a este servidor para este usuario."
        
        return canales
    
    @classmethod
    def crear_canal(cls, nombre, id_servidor):
        query = '''
        INSERT INTO canales (nombre, id_servidor)
        VALUES (%s, %s)
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

