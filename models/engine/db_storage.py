from sqlalchemy import create_engine
import sqlalchemy.orm


class DBStorage:
    __engine = None