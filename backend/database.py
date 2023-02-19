#!/usr/bin/env python3
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class Database:
    def __init__(self,
                 db_user=os.environ['DB_USER'],
                 db_password=os.environ['DB_PASSWORD'],
                 db_host=os.environ['DB_HOST'],
                 db_port=os.environ['DB_PORT'],
                 db_name=os.environ['DB_DATABASE']):
        self.db_host = db_host
        self.db_port = db_port
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.db_engine_url = f'mysql+pymysql://{self.db_user}:{self.db_password}' \
                             f'@{self.db_host}:{self.db_port}/{db_name}'
        self.db_engine = create_engine(self.db_engine_url)
        self.db_base = declarative_base()

    def create_engine(self):
        self.db_engine = create_engine(self.db_engine_url)

    def set_admin_credentials(self, db_user, db_password):
        self.db_user = db_user
        self.db_password = db_password

        os.environ['db_user'] = self.db_user
        os.environ['db_password'] = self.db_password

    def create_session(self):
        db_session = sessionmaker(autocommit=False,
                                  autoflush=False,
                                  bind=self.db_engine)
        return db_session()

    def get_db(self):
        db_session = self.create_session()
        try:
            yield db_session
        finally:
            db_session.close()