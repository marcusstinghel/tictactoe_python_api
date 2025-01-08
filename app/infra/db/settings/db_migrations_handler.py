from sqlalchemy import Engine
from typing import Type

from sqlalchemy.ext.declarative import declarative_base


class DBMigrationsHandler:
    @classmethod
    def migrate_table(cls, engine: Engine, entity: Type[declarative_base()]):
        entity.metadata.create_all(bind=engine)

    @classmethod
    def migrate_all_tables(cls, engine: Engine, base: declarative_base()):
        base.metadata.create_all(bind=engine)
