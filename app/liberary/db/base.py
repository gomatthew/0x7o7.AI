import json

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker

# TODO fix env param
from app import app

engine = create_engine(
    app.config.get('SQLALCHEMY_DATABASE_URI'),
    json_serializer=lambda obj: json.dumps(obj, ensure_ascii=False),
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base: DeclarativeMeta = declarative_base()


def create_tables():
    Base.metadata.create_all(bind=engine)
