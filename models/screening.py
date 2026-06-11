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

    @property
    def hall_number(self):
        return self._hall_number

    @hall_number.setter
    def hall_number(self, value):
        try:
            val = int(value)
        except (ValueError, TypeError):
            raise ValueError("Hall number must be an integer.")
        if val <= 0:
            raise ValueError("Hall number must be a positive number.")
        self._hall_number = val

    def to_dict(self):
        return {"id": self.id, "movie_id": self.movie_id, "hall_number": self.hall_number, "time": self.time}

    def __repr__(self):
        return f"<Screening {self.id}: Movie {self.movie_id} | Hall {self.hall_number} at {self.time}>"

    @classmethod
    def find_by_id(cls, screening_id):
        return next((s for s in cls.all_screenings if s.id == screening_id), None)

    @classmethod
    def delete_screening(cls, screening_id):
        screening = cls.find_by_id(screening_id)
        if not screening:
            return False
        cls.all_screenings.remove(screening)
        
        from models.booking import Booking
        bookings_to_remove = [b for b in Booking.all_bookings if b.screening_id == screening_id]
        for booking in bookings_to_remove:
            Booking.all_bookings.remove(booking)
        return True