from app.infra.settings import EnvVarsHandler
from app.application.use_cases import GameMoveMaker
from app.infra.db.repositories import GameRepository, PlayerRepository
from app.domain.services import GameService, PlayerService


def test_game_move_maker():
    EnvVarsHandler.read_env_vars('C:/Users/vinio/Projects/tictactoe_api/.env')
    game_repository = GameRepository()
    player_repository = PlayerRepository()
    game = game_repository.get_in_progress_game(player_id=1)
    player = player_repository.get_player(id=1)
    game_service = GameService(game=game)
    player_service = PlayerService(player=player)
    game_move_maker = GameMoveMaker(game_repository=game_repository, game_service=game_service,
                                    player_repository=player_repository, player_service=player_service)
    response = game_move_maker.make_move(game=game, movement={'column': 0, 'row': 0, 'value': 1})

    print(response)
