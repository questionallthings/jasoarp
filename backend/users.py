#!/usr/bin/env python3
from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import database


router = APIRouter(
    prefix="/api/v1/users",
    tags=["Users"]
)
db_initial = database.Database()
db_initial.create_engine()


@router.get("/")
def get_users(db: Session = Depends(db_initial.get_db),
              limit: int = 5,
              email: Optional[str] = None,
              last_login: Optional[datetime] = None,
              active: Optional[bool] = None,
              status: Optional[str] = None,
              verified: Optional[bool] = None,
              phone: Optional[str] = None,
              address: Optional[str] = None,
              name: Optional[str] = None,
              username: Optional[str] = None,
              description: Optional[str] = None,
              notes: Optional[str] = None,
              password: Optional[str] = None
              ):
    kwargs = locals()
    del kwargs['db']
    del kwargs['limit']
    users = backend.crud_users.get_users(db, limit=limit, **kwargs)
    return users


@router.get("/{email}")
def get_user(email: str, db: Session = Depends(db_initial.get_db)):
    user = backend.crud_users.get_user(db, email=email)
    return user


@router.post("/")
def create_user(db: Session = Depends(db_initial.get_db),
                email: Optional[str] = None,
                last_login: Optional[datetime] = None,
                active: Optional[bool] = None,
                status: Optional[str] = None,
                verified: Optional[bool] = None,
                phone: Optional[str] = None,
                address: Optional[str] = None,
                name: Optional[str] = None,
                username: Optional[str] = None,
                description: Optional[str] = None,
                notes: Optional[str] = None,
                password: Optional[str] = None
                ):
    kwargs = locals()
    del kwargs['db']
    user = backend.crud_users.create_user(db, **kwargs)
    return user


@router.patch("/{email}")
def update_user(db: Session = Depends(db_initial.get_db),
                limit: int = 5,
                email: Optional[str] = None,
                last_login: Optional[datetime] = None,
                active: Optional[bool] = None,
                status: Optional[str] = None,
                verified: Optional[bool] = None,
                phone: Optional[str] = None,
                address: Optional[str] = None,
                name: Optional[str] = None,
                username: Optional[str] = None,
                description: Optional[str] = None,
                notes: Optional[str] = None,
                password: Optional[str] = None
                ):
    kwargs = locals()
    del kwargs['db']
    del kwargs['email']
    user = backend.crud_users.update_user(db, email, **kwargs)
    return user


@router.delete("/{email}")
def delete_user(email: str, db: Session = Depends(db_initial.get_db)):
    user = backend.crud_users.delete_user(db, email=email)
    return user
