from flask import Blueprint
from app.interface.api.controllers import AIController

ai_bp = Blueprint('ai', __name__)


@ai_bp.route('/ai-move', methods=['GET'])
def ai_move():
    return AIController.make_move()


@ai_bp.route('/ai-train', methods=['POST'])
def train():
    return AIController.train()
