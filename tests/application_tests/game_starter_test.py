from app.infra.settings import EnvVarsHandler
from app.application.use_cases import GameStarter
from app.infra.db.repositories import GameRepository


def test_game_starter():
    EnvVarsHandler.read_env_vars('C:/Users/vinio/Projects/tictactoe_api/.env')
    game_repository = GameRepository()
    game = GameStarter(game_repository=game_repository)
    new_game = game.start(player_id=1)
    print('New Game: ', new_game.id, new_game.board)

