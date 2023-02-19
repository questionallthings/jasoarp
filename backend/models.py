#!/usr/bin/env python3
from sqlalchemy import Boolean, Column, Integer, String, DateTime, Text
import database

db_instance = database.Database()
Base = db_instance.db_base


class BaseModel:
    id = Column(Integer, primary_key=True)
    description = Column(Text)
    notes = Column(Text)
    sync_tags = Column(Text)


class Users(Base, BaseModel):
    __tablename__ = "users"

    email = Column(String(255), nullable=False)
    password = Column(Text, nullable=False)
    username = Column(String(255), nullable=False)
    address = Column(Text)
    phone = Column(String(32))
    status = Column(String(16), nullable=False)
    last_login = Column(DateTime)
    active = Column(Boolean, nullable=False)
    verified = Column(Boolean, nullable=False)
    access_groups = Column(Text, nullable=False)