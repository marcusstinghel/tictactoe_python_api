from app.infra.ai.use_cases import AIMovement
from app.infra.db.repositories import GameRepository
from app.application.use_cases import MLMoveMaker
from app.infra.settings import EnvVarsHandler

def test_make_move():
    EnvVarsHandler.read_env_vars('C:/Users/vinio/Projects/tictactoe_api/.env')
    game_repository = GameRepository()
    ai_movement = AIMovement()
    ml_move_maker = MLMoveMaker(game_repository=game_repository, ml_movement=ai_movement)
    movement = ml_move_maker.make_move(player_id=1)
    print('Movement: ', movement)
