import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

database_name = "wmd"
database_path = 'postgres://postgres@localhost:5432/wmd'

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
  app.config["SQLALCHEMY_DATABASE_URI"] = database_path
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  db.app = app
  db.init_app(app)
  
  migrate = Migrate(app, db)

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Record(db.Model):
    __tablename__ = 'Record'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    isbn = db.Column(db.String, unique=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable=True)
    image_link = db.Column(db.String(500))

    def __repr__(self):
        return f'<Record {self.id} {self.name} {self.isbn} {self.artist_id} {self.image_link}>'
    
    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'isbn': self.isbn,
            'artist_id': self.artist_id,
            'image_link': self.image_link,
        }
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()


class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    image_link = db.Column(db.String(500))

    records = db.relationship('Record', backref='artist', lazy=True)

    def __repr__(self):
      return f'<Artist {self.id} {self.name} {self.image_link}>'

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'image_link': self.image_link,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()


