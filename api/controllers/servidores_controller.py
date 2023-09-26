from ..models.servidores_models import Servidores
from flask import request,jsonify

class ServidoresController:
    
    @classmethod 
    def obtener_servidores(self,usuario_id):
        Servidores = Servidores.obtener_servidores(usuario_id)
        if Servidores:
            response ={
                "logo": Servidores.logo,
                "nombre": Servidores.nombre,
                "descripcion": Servidores.descripcion,
                "region": Servidores.region,
                "miembros": Servidores.miembros,
                "creador": Servidores.creador,
                "fecha_creacion": Servidores.fecha_creacion,
                "id_usuario": Servidores.id_usuario
            }
            return jsonify(response), 200
        else:
            return jsonify({"message": "No se encontraron datos"}), 404
        
    @classmethod 
    def crear_servidor(self):
        data = request.json()
        Servidores = Servidores(
            id_servidor=None,
            nombre=data.get('nombre'),
            descripcion=data.get('descripcion'),
            region=data.get('region'),
            miembros=data.get('miembros'),
            creador=data.get('creador'),
            fecha_creacion=data.get('fecha_creacion')
        )
        Servidores.crear_servidor(Servidores)
        return jsonify({}), 201