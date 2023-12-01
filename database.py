from flask import Flask, request, make_response 
import sqlalchemy
import pymysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, create_engine, ForeignKey, DateTime, desc, UniqueConstraint
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, scoped_session
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user


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
    UniqueConstraint('loc', 'uid', name='uq_loc_uid')


# add register users into the database
def add_user(username,email,password):
    # user = User.query.filter_by(email=email).first()
    # if user is None: 
    session = Session()
    new_user = User(uname=username,email=email,pwd=password)
    session.add(new_user)
    session.commit()

# add location into the database
def add_loc(location, uid):
    session = Session()

    try:
        existing_location = session.query(Location).filter_by(loc=location, uid=uid).first()

        if existing_location:
            # Location already exists for the user, handle accordingly
            print("Location already exists for the user:", existing_location)
        else:
            new_loc = Location(loc=location, uid=uid)
            session.add(new_loc)
            session.commit()

        # Delete excess locations if there are more than five for the user
        user_locations = session.query(Location).filter_by(uid=uid).order_by(desc(Location.time)).all()

        if len(user_locations) > 5:
            excess_locations = user_locations[5:]
            for excess_location in excess_locations:
                session.delete(excess_location)

            session.commit()

    finally:
        session.close()


Base.metadata.create_all(engine)
