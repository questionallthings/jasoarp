#!/usr/bin/env python3
from sqlalchemy.orm import Session
import models


def get_user(db: Session, email: str):
    return db.query(models.Users).filter(models.Users.email == email).first()


def get_users(db: Session, limit, **kwargs):
    unfiltered_kwargs = locals()
    kwargs = {}
    for each in unfiltered_kwargs['kwargs']:
        if unfiltered_kwargs['kwargs'][each] is not None:
            kwargs[each] = unfiltered_kwargs['kwargs'][each]
    return db.query(models.Users).filter_by(**kwargs).limit(limit).all()


def create_user(db: Session, **kwargs):
    unfiltered_kwargs = locals()
    kwargs = {}
    for each in unfiltered_kwargs['kwargs']:
        if unfiltered_kwargs['kwargs'][each] is not None:
            kwargs[each] = unfiltered_kwargs['kwargs'][each]
    user = models.Users(**kwargs)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update_user(db: Session, email: str, **kwargs):
    unfiltered_kwargs = locals()
    kwargs = {}
    for each in unfiltered_kwargs['kwargs']:
        if unfiltered_kwargs['kwargs'][each] is not None:
            kwargs[each] = unfiltered_kwargs['kwargs'][each]
    user_data = get_user(db, email)
    print(kwargs)
    for key, value in kwargs.items():
        setattr(user_data, key, value)
    db.add(user_data)
    db.commit()
    db.refresh(user_data)
    return user_data


def delete_user(db: Session, email: str):
    user_data = get_user(db, email)
    db.delete(user_data)
    db.commit()
    return {"ok": True}
