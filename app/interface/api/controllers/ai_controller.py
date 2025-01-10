from flask import request, jsonify

from app.infra.ai.use_cases import AIMovement, AILearning
from app.infra.db.repositories import GameRepository
from app.application.use_cases import MLMoveMaker, MLTrainer

class AIController:

    @staticmethod
    def make_move():
        player_id = request.args.get('player-id')
        game_repository = GameRepository()
        ai_movement = AIMovement()
        ml_move_maker = MLMoveMaker(game_repository=game_repository, ml_movement=ai_movement)
        movement = ml_move_maker.make_move(
            player_id=int(player_id),
        )
        return jsonify(movement), 200

    @staticmethod
    def train():
        data = request.json
        ai_learning = AILearning()
        game_repository = GameRepository()
        ml_trainer = MLTrainer(ml_learning=ai_learning, game_repository=game_repository)
        ml_trainer.train(
            games_amount=data['amount'],
            pth_file_path='tic_tac_toe_model.pth'
        )
        return jsonify('successfully trained AI'), 200
