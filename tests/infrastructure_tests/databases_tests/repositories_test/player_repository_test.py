from app.infra.db.repositories import PlayerRepository
from app.infra.settings import EnvVarsHandler


def test_create_player():
    EnvVarsHandler.read_env_vars(dot_env_file='C:/Users/vinio/Projects/tictactoe_api/.env')
    PlayerRepository.create_player(
        first_name='Marcus',
        last_name='Smith',
        nickname='Mr. Smith',
    )
