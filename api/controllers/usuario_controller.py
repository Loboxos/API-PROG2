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
            apellido=data.get('apellidos'),
            fecha_nacimiento=data.get('fecha_nacimiento'),
            contraseña=data.get('contraseña'),
            apodo=data.get('apodo')
        )
        usuario.crear_usuario(usuario)
        return jsonify({}), 201
    
    @classmethod 
    def obtener_usuario(self, id_usuario):
        Usuario = Usuario.obtener_usuario(id_usuario)
        if Usuario:
            response = {
                "email": Usuario.email,
                "nombre": Usuario.nombre,
                "apellidos": Usuario.apellido,
                "fecha_nacimiento": Usuario.fecha_nacimiento,
                "contraseña": Usuario.contraseña,
                "apodo": Usuario.apodo
            }
            
            return jsonify(response), 200
        else:
            return jsonify({}), 404