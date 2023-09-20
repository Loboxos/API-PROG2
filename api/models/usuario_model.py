from ..database import DatabaseConnection
import mysql.connector


class Usuario:
    def __init__(self, id_usuario, nombre, apellido, fecha_de_nacimiento, contraseña, apodo, avatar):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.contraseña = contraseña
        self.apodo = apodo
        self.avatar = avatar
        
        
    @classmethod    
    def crear_usuario(cls, usuario):
        
        query ='''
        INSERT INTO usuario (nombre, apellido, fecha_de_nacimiento, contraseña, apodo)
        VALUES(%s, %s, %s, %s, %s)
        '''
        values = (usuario.nombre, usuario.apellido, usuario.fecha_de_nacimiento, usuario.contraseña, usuario.apodo)
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            return True
        except mysql.connector.IntegrityError as e:     
            cursor.close()
            return "El usuario ya existe en la base de datos"