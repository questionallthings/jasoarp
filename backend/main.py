#!/usr/bin/env python3

import os

from fastapi import FastAPI
import database
import models
import users

db_instance = database.Database(db_user=os.environ['DB_USER'],
                                db_password=os.environ['DB_PASSWORD'],
                                db_host=os.environ['DB_HOST'],
                                db_port=os.environ['DB_PORT'],
                                db_name=os.environ['DB_DATABASE'])
db_instance.create_engine()
db_engine = db_instance.db_engine

# TODO: Implement Alembic for database intialization.
models.Base.metadata.create_all(bind=db_engine)

app = FastAPI()

app.include_router(users.router)
