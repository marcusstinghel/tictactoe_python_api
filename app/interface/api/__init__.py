from flask import Flask
from app.interface.api.routes import player_bp, game_bp, ai_bp


def create_app():
    app = Flask(__name__)
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

    app.register_blueprint(player_bp, url_prefix='/api/')
    app.register_blueprint(game_bp, url_prefix='/api/')
    app.register_blueprint(ai_bp, url_prefix='/api/')

    return app
