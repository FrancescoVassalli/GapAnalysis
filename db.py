import os
import logging
from dotenv import find_dotenv, load_dotenv
from sqlmodel import Session, create_engine, SQLModel

logger = logging.getLogger("Database")

class Database:
    def __init__(self, db_url: str | None = None):
        load_dotenv(find_dotenv())
        if not db_url:
            db_url = os.getenv("ALEMBIC_DATABASE_URL")
            logger.info(f'Connected to db at {db_url}')
        self.engine = create_engine(db_url)

    # Example use:
    # with db.get_session() as session:
    #     session.exec(select(User)).all()
    def get_session(self, **kwargs):
        return Session(self.engine, **kwargs)
    
    # Example use:
    # with db.get_sql_session() as con:
    #     rs = con.execute('SELECT * FROM users')
    def get_sql_session(self):
        return self.engine.connect()