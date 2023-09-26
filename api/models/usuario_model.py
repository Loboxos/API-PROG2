from ..database import DatabaseConnection
import mysql.connector


class Usuario:
    def __init__(self, id_usuario,email, nombre, apellido, fecha_nacimiento, contraseña, apodo, avatar=None):
        self.id_usuario = id_usuario
        self.email = email
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.contraseña = contraseña
        self.apodo = apodo
        self.avatar = avatar
        
    def __str__(self):
        return f"{self.nombre},{self.apellido},{self.email}"
   
    @classmethod    
    def crear_usuario(cls, usuario):
        
        query ='''
        INSERT INTO usuarios (email,nombre, apellido, fecha_nacimiento, contraseña, apodo)
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
        FROM usuarios
        WHERE
        id_usuario = %s
        '''
        params = (id_usuario,)
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return Usuario(
                id_usuario=result[0],
                email=result[1],
                nombre=result[2],
                apellido=result[3],
                fecha_nacimiento=result[4],
                contraseña=result[5],
                apodo=result[6],
                avatar=result[7]
            )
        else:
            return None