from os import getenv
from dotenv import load_dotenv


class EnvVarsHandler:

    @classmethod
    def read_env_vars(cls, dot_env_file: str):
        load_dotenv(dotenv_path=dot_env_file)

    @staticmethod
    def verify_env(func):
        def wrapper(*args, **kwargs):
            try:
                action = func(*args, **kwargs)
                return action
            except EnvironmentError as e:
                return f"Error: {str(e)}"

        return wrapper

    @staticmethod
    @verify_env
    def get_db_connection_string():
        return getenv('DB_CONNECTION_STRING')

    @staticmethod
    @verify_env
    def get_ml_pth_file_path():
        return getenv('ML_PATH_FILE_PATH')
