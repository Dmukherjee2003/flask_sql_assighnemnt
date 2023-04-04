class MovieRepository:

    def get_all_movies(self):
        all_movies = Movie.query.all()
        return all_movies

    def get_movie_by_id(self, movie_id):
        single_movie = Movie.query.filter_by(movie_id=movie_id).first()
        return single_movie

    def create_movie(self, title, director, rating):
        new_movie = Movie(title=title, director=director, rating=rating)
        db.session.add(new_movie)
        db.session.commit()
        return new_movie


    def search_movies(self, title):
        title = f"%{title}%"
        found_movies = Movie.query.filter(Movie.title.like(title)).all()
        return found_movies

# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
