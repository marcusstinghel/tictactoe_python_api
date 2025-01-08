from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    __connection_string: str
    __engine: Engine
    __session: any

    def __init__(self, connection_string: str):
        self.__connection_string = connection_string
        self.__engine = self.__create_engine()

    def get_engine(self):
        return self.__engine

    def get_session(self):
        return self.__session

    def __create_engine(self):
        return create_engine(self.__connection_string, echo=True)

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.__session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__session.close()
