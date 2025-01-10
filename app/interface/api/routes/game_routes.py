from flask import Blueprint
from app.interface.api.controllers import GameController

game_bp = Blueprint('game', __name__)


@game_bp.route('start', methods=['POST'])
def start_game():
    return GameController.start_game()


@game_bp.route('move', methods=['POST'])
def move_game():
    return GameController.make_move()
