from ..models.servidores_models import Servidores
from flask import request,jsonify

class ServidoresController:
    
    @classmethod 
    def obtener_servidores(self,id_usuario):
        servidores = Servidores.obtener_servidores(id_usuario)
        if servidores:
            response = []
            print(servidores)
            for servidor in servidores:
                data= {
                    "id_servidor":servidor["id_servidor"],
                    "nombre": servidor["nombre"],
                    "descripcion": servidor["descripcion"],
                    "region": servidor["region"],
                    "miembros": servidor["miembros"],
                    "creador": servidor["creador"],
                    "fecha_creacion": str(servidor["fecha_creacion"]), 
                    "id_usuario": servidor["id_usuario"],
                    "logo": servidor["logo"],
                }
                response.append(data)
            return jsonify(response), 200
        else:
            return jsonify([],{"message": "No se encontraron datos"}), 404


    @classmethod 
    def crear_servidor(self):
        data = request.json
        servidores = Servidores(
            id_servidor=None,
            nombre=data.get('nombre'),
            descripcion=data.get('descripcion'),
            region=data.get('region'),
            miembros=data.get('miembros'),
            creador=data.get('creador'),
            fecha_creacion=data.get('fecha_creacion'),
            id_usuario=data.get('id_usuario')
        )
        Servidores.crear_servidor(servidores)
        return jsonify({}), 201