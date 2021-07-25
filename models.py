import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import json

database_path = os.environ['DATABASE_URL']
db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    db.create_all()


'''
Person
Have title and release year
'''


class Person(db.Model):
    __tablename__ = 'People'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    catchphrase = Column(String)

    def __init__(self, name, catchphrase=""):
        self.name = name
        self.catchphrase = catchphrase

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'catchphrase': self.catchphrase}


class Actor(db.Model):
    __tablename__ = 'actors'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    gender = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=True, default='')

    def __init__(self, name, age, gender, description=""):
        self.name = name
        self.age = age
        self.gender = gender
        self.description = description

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def get_as_json(self):
        return({
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "description": self.description,
        })


class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    released_date = db.Column(db.Date(), nullable=False)
    genre = db.Column(db.String(), nullable=True, default='')
    description = db.Column(db.String(), nullable=True, default='')

    def __init__(self, title, released_date, genre, description=""):
        self.title = title
        self.released_date = released_date
        self.genre = genre
        self.description = description

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def get_as_json(self):
        return({
            "id": self.id,
            "title": self.title,
            "released_date": self.released_date,
            "genre": self.genre,
            "description": self.description,
        })
