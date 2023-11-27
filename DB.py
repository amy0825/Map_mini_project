from flask import Flask, render_template , make_response, request
import sqlalchemy
import pymysql
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, desc
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# app = Flask(__name__)

# # Configure the SQLAlchemy database URI
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@/cloudsql/braided-carport-400818:map/mapDB'

# # Create the SQLAlchemy database object
# db = SQLAlchemy(app)
# mysql+pymysql://amy:password@34.142.93.241/mapDB
# app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql + pymysql://amy:password@34.142.93.241/mapDB?unix_socket =/cloudsql/braided-carport-400818:map"
# mysql+mysqldb://amy:password@/mapDB?unix_socket=/cloudsql/braided-carport-400818:map
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://amy:password@/mapDB?unix_socket=/cloudsql/braided-carport-400818:europe-west2:map'

# configuration
app.config["SECRET_KEY"] = "yoursecretkey"
app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql + mysqldb://amy:password@34.142.93.241/mapDB?unix_socket =/cloudsql/braided-carport-400818:map"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True


db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://amy:password@/cloudsql/braided-carport-400818:map/mapDB'
    db.init_app(app)
    return app

app = create_app()

class User(db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uname = Column(String(64),nullable=True)
    email = Column(String(64),nullable=True,unique=True)
    pwd = Column(String(64),nullable=True)

class Location(db.Model):
    __tablename__ = 'location'

    pid = Column(Integer, primary_key=True, autoincrement=True)
    loc = Column(String(64),unique=True)
    time = Column(DateTime, default=datetime.utcnow)
    uid = Column(Integer, ForeignKey('users.id'))

    # Relationship with User
    user = relationship("User", backref="locations")

# add register users into the database
def add_user(username,email,password):
    new_user = User(uname=username,email=email,pwd=password)
    db.session.add(new_user)
    db.session.commit()

# add locations detail into the database, the max values will be five locations
def add_loc(location,uid,pid):
    new_loc = Location(loc=location, uid= uid)
    db.session.add(add_loc)
    db.session.commit()

    # delete location attribute if there is more than five attributes
    att = db.session.query(Location).order_by(desc(Location.timestamp)).all()
    if len(all)>5:
        for i in att[5:]:
            db.session.delete(i)
        db.session.commit()

# logout function, after user logout, clear all the cache
def logout(session):
    session.expunge_all()
    session.close()