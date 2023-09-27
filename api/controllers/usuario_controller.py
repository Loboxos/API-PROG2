from ..models.usuario_model import Usuario
from flask import request, jsonify ,session

class UsuarioController:
    
    @classmethod
    def login(cls):
        data = request.json
        usuario = Usuario(
            email = data.get('email'),
            password = data.get('password')
        )
        
        if Usuario.is_registered(usuario):
            session['email'] = data.get('email')
            return {"message": "Sesion iniciada"}, 200
        else:
            return {"message": "Usuario o contraseña incorrectos"}, 401



    @classmethod
    def crear_usuario(cls):
        data = request.json
        usuario = Usuario(
            id_usuario=None,
            email=data.get('email'),
            nombre=data.get('nombre'),
            apellido=data.get('apellido'),
            fecha_nacimiento=data.get('fecha_nacimiento'),
            contraseña=data.get('contraseña'),
            apodo=data.get('apodo')
        )
        print(usuario)
        Usuario.crear_usuario(usuario)
        return jsonify({}), 201
    
    @classmethod 
    def obtener_usuario(self, id_usuario):
        usuario = Usuario.mostrar_usuario(id_usuario)
        if usuario:
            response = {
                "email": usuario.email,
                "nombre": usuario.nombre,
                "apellidos": usuario.apellido,
                "apodo": usuario.apodo,
                "avatar":usuario.avatar
            }
            
            return jsonify(response), 200
        else:
            return jsonify({}), 404

