from ..models.canales_models import Canales
from flask import request,jsonify

class CanalesController:

    @classmethod 
    def obtener_canales(self, id_servidor):
        canales = Canales.mostrar_canales(id_servidor)
        if canales:
            response = []
            
            for canal in canales:
                data = {
                    "id_canal":canal["id_canal"],
                    "nombre": canal["nombre"],
                    "id_servidor": canal["id_servidor"],
                    "descripcion": canal["descripcion"]
                }
                response.append(data)
            return jsonify(response), 200
        else:
            return jsonify({"error": "No se encontraron canales"}), 404
    
    @classmethod  
    def crear_canal(self):
        data = request.json
        canal = Canales(
            id_canal = None,
            nombre = data["nombre"],
            id_servidor = data["id_servidor"],
            descripcion = data["descripcion"]
        )
        Canales.crear_canal(canal)
        return jsonify({}), 201