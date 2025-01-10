from flask import request, jsonify
import json
import ast

from app.application.use_cases import GameStarter
from app.infra.db.repositories import GameRepository, PlayerRepository
from app.application.use_cases import GameMoveMaker
from app.domain.services import GameService, PlayerService


class GameController:

    @staticmethod
    def start_game():
        data = request.json
        game_repository = GameRepository()
        game = GameStarter(game_repository=game_repository)
        new_game = game.start(
            player_id=data['player_id'],
        )
        return jsonify(new_game.__dict__), 201

    @staticmethod
    def make_move():
        data = request.json
        game_repository = GameRepository()
        player_repository = PlayerRepository()
        game = game_repository.get_in_progress_game(
            player_id=data['player_id'],
        )
        player = player_repository.get_player(
            id=data['player_id'],
        )
        game_service = GameService(game=game)
        player_service = PlayerService(player=player)
        game_move_maker = GameMoveMaker(game_repository=game_repository, game_service=game_service,
                                        player_repository=player_repository, player_service=player_service)
        response = game_move_maker.make_move(
            game=game,
            movement=ast.literal_eval(json.dumps(data['movement']))
        )
        return jsonify(response), 200
