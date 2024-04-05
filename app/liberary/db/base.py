from app import app
from sqlmodel import Session, create_engine, SQLModel

engine = create_engine(app.config.get('SQLALCHEMY_DATABASE_URI'))
session_ai = Session(engine)


# engine = create_engine(
#     app.config.get('SQLALCHEMY_DATABASE_URI'),
#     json_serializer=lambda obj: json.dumps(obj, ensure_ascii=False),
# )
#
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# Base: DeclarativeMeta = declarative_base()
#
#
def create_tables():
    SQLModel.metadata.create_all(bind=engine)
