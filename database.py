# -*- coding: utf-8 -*-
import re, ast
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

db_name = 'master.db'
engine = create_engine('sqlite:///module/{}?check_same_thread=False'.format(db_name))
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class uid_manager(Base):
    __tablename__ = 'uid_facebook'

    id = Column(Integer, primary_key=True)
    uid = Column(String(50))

    def add_uid(self, uid):
        session.add(uid_manager(uid=uid))
        session.commit()

    def query_uid(self):
        data = session.query(uid_manager).all()
        return data

    def del_uid(self, uid):
    	data = session.query(uid_manager).filter(uid_manager.uid == uid).first()
        session.delete(data)
        session.commit()

if __name__ == '__main__':
    # pass
    uid_manager().add_uid('123')