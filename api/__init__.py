from flask import Flask
from flask_cors import CORS
from config import Config
from .database import DatabaseConnection
from .routes.discord_bp import discord_bp




def init_app():
    """Crea y configura la aplicación FLask."""
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    
    CORS(app, supports_credentials=True)
    
    app.config.from_object(Config)
    
    DatabaseConnection.set_config(app.config)
    
    app.register_blueprint(discord_bp)
    


    @app.route('/')
    def hello_world():
        return 'Bienvenidos!'
    
    
    
    return app