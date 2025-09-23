from marshmallow import Schema, fields

from app.setup_db import db

class Director(db.Model):
    __tablename__ = 'directors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))

class DirectorSchema(Schema):
    id = fields.Integer()
    name = fields.String()