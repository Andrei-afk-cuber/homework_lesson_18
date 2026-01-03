from flask import Flask
from flask_restx import Api

from app.config import Config
from app.setup_db import db
from app.views.movies.views import movies_ns
from app.views.genres.views import genres_ns
from app.views.directors.views import directors_ns
from app.data import *

def create_app(config_object: Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app

def register_extensions(app: Flask) -> None:
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movies_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(directors_ns)
    create_data(app, db)

def create_data(app: Flask, db) -> None:
    with app.app_context():
        db.drop_all()
        db.create_all()

        with db.session.begin():
            db.session.add_all([movie_1, movie_2, movie_3, genre_1, genre_2, genre_3, director_1, director_2, director_3])


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host= "0.0.0.0", port= 5000, debug=True)



