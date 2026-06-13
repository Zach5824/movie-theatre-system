import unittest
from models.movie import Movie
from models.screening import Screening

class TestMovieModel(unittest.TestCase):
    def setUp(self):
        """Clear memory collections before every single test run."""
        Movie.all_movies.clear()
        Screening.all_screenings.clear()
        Movie._id_counter = 1

    def test_movie_creation_and_auto_id(self):
        """Verify that movies append to tracking lists and auto-increment unique IDs."""
        m1 = Movie("Inception", "Sci-Fi", 148)
        m2 = Movie("Interstellar", "Sci-Fi", 169)
        
        self.assertEqual(m1.id, 1)
        self.assertEqual(m2.id, 2)
        self.assertEqual(len(Movie.all_movies), 2)

    def test_invalid_title_throws_error(self):
        """Properties must prevent blank or empty string assignments."""
        with self.assertRaises(ValueError):
            Movie("   ", "Drama", 120)

    def test_invalid_duration_throws_error(self):
        """Properties must block negative values or non-integers."""
        with self.assertRaises(ValueError):
            Movie("Gladiator", "Action", -50)
        with self.assertRaises(ValueError):
            Movie("Gladiator", "Action", "one hour")

    def test_cascading_deletion(self):
        """Deleting a movie must automatically clean out dependent screenings."""
        movie = Movie("Avatar", "Sci-Fi", 162)
        screening = Screening(movie.id, 3, "2026-06-20 14:00")
        
        # Confirm setup state
        self.assertIn(screening, Screening.all_screenings)
        
        # Execute deletion
        Movie.delete_movie(movie.id)
        
        # Verify cascade cleared children arrays
        self.assertNotIn(movie, Movie.all_movies)
        self.assertNotIn(screening, Screening.all_screenings)

if __name__ == "__main__":
    unittest.main()