from flask import Flask
import os
from config import Config
from .models.db import Database  # 상대 경로 사용

db = Database()

def create_app():
    app = Flask(__name__)
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
    static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
    
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

    from .routes.main_routes import main_bp, cal_bp, his_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(cal_bp)
    app.register_blueprint(his_bp)
    return app