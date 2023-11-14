from flask import Flask, request, make_response
import sqlalchemy
import pymysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

app = Flask(__name__)

engine = sqlalchemy.create_engine('mysql+pymysql://amy:password@34.142.93.241/mapDB')                                              

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uname = Column(String(64),nullable=True)
    email = Column(String(64),nullable=True,unique=True)
    pwd = Column(String(64))


class Location(Base):
    __tablename__ = 'location'

    pid = Column(Integer, primary_key=True, autoincrement=True)
    loc = Column(String(64),unique=True)
    uid = Column(String(64), ForeignKey('users.id'))

DBSession = sessionmaker(bind=engine)

session = DBSession()

new_user = User(uname="test",email="test@gmail.com",pwd="password")
#session.add(new_user)
#session.commit()
#session.close()


