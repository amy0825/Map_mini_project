from flask import Flask, request, make_response 
import sqlalchemy
import pymysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, create_engine, ForeignKey, DateTime, desc
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, scoped_session
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user
#from app import login_manager

app = Flask(__name__)


engine = sqlalchemy.create_engine('mysql+pymysql://amy:password@34.142.93.241/mapDB')    
Session = sessionmaker(bind=engine)
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class User(Base,UserMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uname = Column(String(64),nullable=True)
    email = Column(String(64),nullable=True,unique=True)
    pwd = Column(String(512),nullable=True)


class Location(Base, UserMixin):
    __tablename__ = 'location'

    pid = Column(Integer, primary_key=True, autoincrement=True)
    loc = Column(String(64),unique=True)
    time = Column(DateTime, default=datetime.utcnow)
    uid = Column(Integer, ForeignKey('users.id'))

    # Relationship with User
    user = relationship("User", backref="locations")


#def create_session():
   # engine = sqlalchemy.create_engine('mysql+pymysql://amy:password@34.142.93.241/mapDB')    
   # Session = sessionmaker(bind=engine)
   # db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
  #  Base.query = db_session.query_property()
 #   Base.metadata.create_all(engine)
#    return Session()



# add register users into the database
def add_user(username,email,password):
    # user = User.query.filter_by(email=email).first()
    # if user is None: 
    session = Session()
    new_user = User(uname=username,email=email,pwd=password)
    session.add(new_user)
    session.commit()

# add locations detail into the database, the max values will be five locations
def add_loc(location,uid,pid):
    session = Session()
    new_loc = Location(loc=location, uid= uid)
    session.add(add_loc)
    session.commit()

    # delete location attribute if there is more than five attributes
    att = session.query(Location).order_by(desc(Location.timestamp)).all()
    if len(all)>5:
        for i in att[5:]:
            session.delete(i)
        session.commit()

# logout function, after user logout, clear all the cache
def logout(session):
    session.expunge_all()
    session.close()

Base.metadata.create_all(engine)
