from marshmallow import Schema, fields

from app.setup_db import db

class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))

class GenreSchema(Schema):
    id = fields.Integer()
    name = fields.String()