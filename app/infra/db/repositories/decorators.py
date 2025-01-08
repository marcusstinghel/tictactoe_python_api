from app.infra.db.settings import DBConnectionHandler
from app.infra.settings import EnvVarsHandler


def use_db_session(func):
    def wrapper(cls, *args, **kwargs):
        with DBConnectionHandler(EnvVarsHandler.get_db_connection_string()) as db:
            session = db.get_session()
            engine = db.get_engine()
            setattr(cls, 'session', session)
            setattr(cls, 'engine', engine)
            try:
                action = func(cls, *args, **kwargs)
                if session.dirty or session.new:
                    session.commit()
            except Exception as e:
                session.rollback()
                raise e
        delattr(cls, 'session')
        delattr(cls, 'engine')
        return action

    return wrapper
