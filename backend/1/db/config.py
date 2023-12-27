import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

load_dotenv()


engine = create_engine(os.environ["DATABASE_URL"])
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import models.todo

    Base.metadata.create_all(bind=engine)
