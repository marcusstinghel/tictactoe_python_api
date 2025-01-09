from app.application.use_cases import PlayerCreator
from app.infra.db.repositories import PlayerRepository
from app.infra.settings import EnvVarsHandler

def test_player_creator():
    EnvVarsHandler.read_env_vars('C:/Users/vinio/Projects/tictactoe_api/.env')
    player_repository = PlayerRepository()
    player = PlayerCreator(player_repository=player_repository)
    created_player = player.create(
        first_name="John",
        last_name="Smith",
        nickname="Mr. Smith",
    )
    print('Created player:', created_player.id)
