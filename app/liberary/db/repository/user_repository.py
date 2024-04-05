# -*- coding: utf-8 -*-
from typing import Union
from sqlmodel import select
from app.liberary.db.session import with_session
from app.liberary.db.models.user_model import UserModel


@with_session
def add_user_to_db(session, **kwargs):
    new_user = UserModel(**kwargs)
    session.add(new_user)
    return new_user.id


@with_session
def update_user_token(session, user_id, user_token):
    statement = select(UserModel).where(UserModel.id == user_id)
    user = session.exec(statement).first()
    user.token = user_token
    session.add(user)
    return user.id


@with_session
def user_checkin(session, account) -> tuple:
    if '@' in account:
        statement = select(UserModel).where(UserModel.email == account)
    else:
        statement = select(UserModel).where(UserModel.phone == account)
    user = session.exec(statement).first()
    if user:
        return user.id, user.password
    else:
        return None, None
