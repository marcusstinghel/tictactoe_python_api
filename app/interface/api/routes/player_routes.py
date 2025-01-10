from flask import Blueprint
from app.interface.api.controllers import PlayerController

player_bp = Blueprint('player', __name__)

@player_bp.route('/register', methods=['POST'])
def create_player():
    return PlayerController.create_player()
