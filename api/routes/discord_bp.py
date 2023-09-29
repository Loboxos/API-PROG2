from flask import Blueprint
from ..controllers.canales_controller import CanalesController
from ..controllers.chat_controller import ChatController
from ..controllers.servidores_controller import ServidoresController
from ..controllers.usuario_controller import UsuarioController

discord_bp = Blueprint('discord', __name__)

discord_bp.route('/login', methods=['POST'])(UsuarioController.login)
discord_bp.route('/logout', methods=['GET'])(UsuarioController.logout)
discord_bp.route('/perfil', methods=['GET'])(UsuarioController.show_profile)


discord_bp.route('/canales/<int:id_servidor>', methods=['GET'])(CanalesController.obtener_canales)
discord_bp.route('/canales/crear', methods=['POST'])(CanalesController.crear_canal)
discord_bp.route('/chat/<int:id_canal>', methods=['GET'])(ChatController.obtener_mensaje)
discord_bp.route('/servidores/<int:id_usuario>', methods=['GET'])(ServidoresController.obtener_servidores)
discord_bp.route('/servidores/crear', methods=['POST'])(ServidoresController.crear_servidor)
discord_bp.route('/usuarios/<int:id_usuario>', methods=['GET'])(UsuarioController.obtener_usuario)
discord_bp.route('/usuarios/crear', methods=['POST'])(UsuarioController.crear_usuario)
discord_bp.route('/usuarios/actualizar', methods=['PUT'])(UsuarioController.actualizar_usuario)
