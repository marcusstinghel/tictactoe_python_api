from app.interface.api import create_app
from app.infra.settings import EnvVarsHandler

EnvVarsHandler.read_env_vars('.env')
app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
