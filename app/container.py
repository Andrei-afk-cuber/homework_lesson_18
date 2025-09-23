# Контейнер для создания объектов
from app.views.directors.model import Director, DirectorSchema
from app.views.movies.model import Movie, MovieSchema
from app.views.genres.model import Genre, GenreSchema

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)