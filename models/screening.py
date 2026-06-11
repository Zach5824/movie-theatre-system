class Screening:
    _id_counter = 1
    all_screenings = []

    def __init__(self, movie_id, hall_number, time, screening_id=None):
        self.movie_id = int(movie_id)
        self.hall_number = hall_number
        self.time = time

        if screening_id:
            self.id = screening_id
            if screening_id >= Screening._id_counter:
                Screening._id_counter = screening_id + 1
        else:
            self.id = Screening._id_counter
            Screening._id_counter += 1

        Screening.all_screenings.append(self)

    