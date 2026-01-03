from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields

from app.setup_db import db
from app.dao.models.genres_model import GenreSchema
from app.dao.models.directors_model import DirectorSchema

# model for movie
class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(100))
    trailer = db.Column(db.String(100))
    year = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    genre_id = db.Column(db.Integer, ForeignKey("genres.id"))
    genre = relationship("Genre")
    director_id = db.Column(db.Integer, ForeignKey("directors.id"))
    director = relationship("Director")

# schema for movie
class MovieSchema(Schema):
    id = fields.Integer()
    title = fields.String()
    description = fields.String()
    trailer = fields.String()
    year = fields.Integer()
    rating = fields.Integer()
    genre_id = fields.Integer()
    genre = fields.Nested(GenreSchema)
    director_id = fields.Integer()
    director = fields.Nested(DirectorSchema)
