from ..database import DatabaseConnection
import mysql.connector


class Usuario:
    def __init__(self, email, contraseña= None, id_usuario=None, nombre=None, apellido=None, fecha_nacimiento=None, apodo=None, avatar=None,):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.apodo = apodo
        self.email = email
        self.contraseña = contraseña
        self.avatar= avatar
        
    def __str__(self):
        return f"{self.nombre},{self.apellido},{self.email}"
    
    
    @classmethod
    def is_registered(cls, usuario):
        query = """SELECT id_usuario FROM usuarios 
        WHERE email = %s and contraseña = %s"""
        params = (usuario.email, usuario.contraseña)
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return True
        return False
    
    
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
    def actualizar_usuario(cls, data):
        print(data)
        query ='''
        UPDATE usuarios
        SET avatar = %s
        WHERE id_usuario = %s ;
        '''
        values = (data['avatar'], data['userId'])
        connection = DatabaseConnection.get_connection()
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        return True            


    @classmethod
    def mostrar_usuario(cls, email):
        query = '''
        SELECT 
        id_usuario,
        fecha_nacimiento,
        email,
        nombre,
        apellido,
        apodo,
        avatar
        FROM usuarios
        WHERE
        email = %s
        '''
        params = (email,)
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return Usuario(
                id_usuario=result[0],
                fecha_nacimiento=result[1],
                email=result[2],
                nombre=result[3],
                apellido=result[4],
                apodo=result[5],
                avatar=result[6]
            )
        else:
            return None
   
    """ def mostrar_usuario(cls, id_usuario):
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
            return None """