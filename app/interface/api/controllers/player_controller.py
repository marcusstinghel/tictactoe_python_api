from flask import request, jsonify
from app.application.use_cases import PlayerCreator
from app.infra.db.repositories import PlayerRepository


class PlayerController:

    @staticmethod
    def create_player():
        data = request.json
        player_repository = PlayerRepository()
        player_creator = PlayerCreator(player_repository=player_repository)
        created_player = player_creator.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            nickname=data['nickname'],
        )
        return jsonify(created_player.__dict__), 201
