from ..models.canales_models import Canales
from flask import request,jsonify

class CanalesController:
    def obtener_canales(self, id_servidor):
        Canales = Canales.obtener_canales(id_servidor)
        if Canales:
            response = {
                "id_canal": Canales.id_canal,
                "nombre": Canales.nombre,
                "id_servidor": Canales.id_servidor,
                "descripcion": Canales.descripcion
            }
            return jsonify(response), 200
        else:
            return jsonify({"error": "No se encontraron canales"}), 404
        
    def crear_canal(self):
        data = request.json
        Canales = Canales(
            id_canal = None,
            nombre = data["nombre"],
            id_servidor = data["id_servidor"],
            descripcion = data["descripcion"]
        )
        Canales.crear_canal(Canales)
        return jsonify({}), 201