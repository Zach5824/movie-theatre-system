import unittest
from models.movie import Movie
from models.screening import Screening
from models.booking import Booking

class TestScreeningAndBooking(unittest.TestCase):
    def setUp(self):
        Movie.all_movies.clear()
        Screening.all_screenings.clear()
        Booking.all_bookings.clear()
        Screening._id_counter = 1
        Booking._id_counter = 1

    def test_booking_seat_validation(self):
        """Ensure ticket requests require at least 1 seat and check data types."""
        movie = Movie("The Matrix", "Sci-Fi", 136)
        scr = Screening(movie.id, 2, "18:00")
        
        with self.assertRaises(ValueError):
            Booking(scr.id, "Zach", 0)  # Invalid seat count
            
        with self.assertRaises(ValueError):
            Booking(scr.id, "   ", 2)   # Empty client name

    def test_screening_deletion_cascades_to_bookings(self):
        """Canceling a showtime must clear all booking transactions registered to it."""
        movie = Movie("The Matrix", "Sci-Fi", 136)
        scr = Screening(movie.id, 2, "18:00")
        bk = Booking(scr.id, "Zach", 2)
        
        self.assertIn(bk, Booking.all_bookings)
        
        # Cancel the specific showtime
        Screening.delete_screening(scr.id)
        
        # Ticket booking record should be purged
        self.assertNotIn(bk, Booking.all_bookings)

if __name__ == "__main__":
    unittest.main()