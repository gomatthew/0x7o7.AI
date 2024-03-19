from functools import wraps
from contextlib import contextmanager
from app.liberary.db.base import SessionLocal
from sqlalchemy.orm import Session


@contextmanager
def give_me_a_session() -> Session:
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
    finally:
        session.close()


def with_session(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        with give_me_a_session() as session:
            try:
                result = f(session, *args, **kwargs)
                session.commit()
                return result
            except:
                session.rollback()
                raise

    return wrapper
