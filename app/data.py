from app.views.movies.model import Movie
from app.views.genres.model import Genre
from app.views.directors.model import Director

genre_1 = Genre(
    name = "action"
)
genre_2 = Genre(
    name = "comedy"
)
genre_3 = Genre(
    name = "travel"
)

director_1 = Director(
    name = "Justin Timberlake"
)
director_2 = Director(
    name = "Alexey Balabanov"
)
director_3 = Director(
    name = "Sergey Bodrov"
)

movie_1 = Movie(
    title = "first movie",
    description = "test movie 1",
    trailer = None,
    year = 2014,
    rating = 4,
    genre = genre_1,
    director = director_1
)
movie_2 = Movie(
    title="second test movie",
    description="test movie 2",
    trailer=None,
    year=2018,
    rating=3,
    genre=genre_2,
    director=director_2
)
movie_3 = Movie(
    title="thirst movie",
    description="test movie 3",
    trailer=None,
    year=2024,
    rating=4,
    genre=genre_1,
    director=director_1
)