from app.interface.api import create_app
from app.infra.settings import EnvVarsHandler
from app.infra.db.settings import DBMigrationsHandler, DBConnectionHandler
from app.infra.db.entities import Base

EnvVarsHandler.read_env_vars('.env')
database = DBConnectionHandler(EnvVarsHandler.get_db_connection_string())
DBMigrationsHandler.migrate_all_tables(engine=database.get_engine(), base=Base)
app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
