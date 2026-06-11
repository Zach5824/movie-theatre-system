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

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Movie title cannot be empty.")
        self._title = value.strip()

    @property
    def duration_mins(self):
        return self._duration_mins

    @duration_mins.setter
    def duration_mins(self, value):
        try:
            val = int(value)
        except (ValueError, TypeError):
            raise ValueError("Duration must be a valid integer.")
        if val <= 0:
            raise ValueError("Duration must be greater than 0.")
        self._duration_mins = val

    