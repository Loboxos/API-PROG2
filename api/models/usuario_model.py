from ..database import DatabaseConnection
import mysql.connector


class Usuario:
    def __init__(self, id_usuario,email, nombre, apellido, fecha_nacimiento, contraseña, apodo, avatar):
        self.id_usuario = id_usuario
        self.email = email
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.contraseña = contraseña
        self.apodo = apodo
        self.avatar = avatar
        
        
    @classmethod    
    def crear_usuario(cls, usuario):
        
        query ='''
        INSERT INTO usuario (email,nombre, apellido, fecha_nacimiento, contraseña, apodo)
        VALUES(%s,%s, %s, %s, %s, %s)
        '''
        values = (usuario.email,usuario.nombre, usuario.apellido, usuario.fecha_nacimiento, usuario.contraseña, usuario.apodo)
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
        
    @classmethod
    def mostrar_usuario(cls, id_usuario):
        query = '''
        SELECT 
        id_usuario,
        email,
        nombre,
        apellido,
        fecha_nacimiento,
        contraseña,
        apodo,
        avatar
        FROM usuario
        WHERE
        id_usuario = %s
        '''
        params = (id_usuario,)
        result = DatabaseConnection.fetch_one(query, params)
        if result is None:
            return Usuario(
                id_usuario=[0],
                email=[1],
                nombre=[2],
                apellido=[3],
                fecha_de_nacimiento=[4],
                contraseña=[5],
                apodo=[6],
                avatar=[7]
            )
        else:
            return None