from ..models.chat_models import Chat
from flask import request,jsonify

class ChatController:
    @classmethod
    def obtener_mensaje(self, id_canal):
        chats = Chat.obtener_mensaje(id_canal)
        if chats:
            response = []
            for chat in chats:
                data = {
                    "fecha_mensaje": str(chat["fecha_mensaje"]),
                    "mensaje": chat["mensaje"],
                    "menciones": chat["menciones"],
                }
                response.append(data)
                
            return jsonify(response),200
        else:
            return jsonify({"error": "No se encontraron mensajes"}),404