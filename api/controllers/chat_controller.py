from ..models.chat_models import Chat
from flask import request,jsonify

class ChatController:
    def obtener_mensaje(self, id_canal):
        Chat = Chat.obtener_mensaje(id_canal)
        if Chat:
            response ={
                "id_chat": Chat.id_chat,
                "fecha_mensaje": Chat.fecha_mensaje,
                "mensaje": Chat.mensaje,
                "menciones": Chat.menciones
            }
            return jsonify(response),200
        else:
            return jsonify({"error": "No se encontraron mensajes"}),404