from functools import wraps
from app import app
from app.liberary.db.base import session_ai


def with_session(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            with session_ai as session:
                result = f(session, *args, **kwargs)
                session.commit()
                return result

        except BaseException as e:
            app.logger.error(f'failed to add object :{e}')
            session.rollback()

    return wrapper
