from ..models.usuario_model import Usuario
from flask import request, jsonify

class UsuarioController:
    
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