from app.infra.db.settings import DBMigrationsHandler, DBConnectionHandler
from app.infra.db.entities import Base
from app.infra.settings import EnvVarsHandler


def test_create_tables():
    EnvVarsHandler.read_env_vars(dot_env_file='C:/Users/vinio/Projects/tictactoe_api/.env')
    database = DBConnectionHandler(EnvVarsHandler.get_db_connection_string())
    DBMigrationsHandler.migrate_all_tables(engine=database.get_engine(), base=Base)
