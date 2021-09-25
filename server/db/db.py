# Third-party libraries
import decouple
import sqlalchemy as sql
import sqlalchemy.orm as orm
from sqlalchemy.ext.declarative import declarative_base


engine = sql.create_engine(
    url=decouple.config("SQLALCHEMY_DATABASE_URL"),
    connect_args={"check_same_thread": False}
)

SessionLocal = orm.sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

Base = declarative_base()


def start_new_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
