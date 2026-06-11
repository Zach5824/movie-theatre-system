class Movie:
    _id_counter = 1
    all_movies = []

    def __init__(self, title, genre, duration_mins, movie_id=None):
        self.title = title
        self.genre = genre
        self.duration_mins = duration_mins

        if movie_id:
            self.id = movie_id
            if movie_id >= Movie._id_counter:
                Movie._id_counter = movie_id + 1
        else:
            self.id = Movie._id_counter
            Movie._id_counter += 1

        Movie.all_movies.append(self)

   