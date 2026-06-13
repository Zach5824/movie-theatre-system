import unittest
import os
import json
from models.movie import Movie
from utils.storage_handler import save_theater_data, load_theater_data, DATA_FILE

class TestPersistenceEngine(unittest.TestCase):
    def setUp(self):
        Movie.all_movies.clear()
        # Keep a reference to the original file path if it exists to restore it later
        self.backup_existed = os.path.exists(DATA_FILE)
        if self.backup_existed:
            os.rename(DATA_FILE, DATA_FILE + ".bak")

    def tearDown(self):
        """Clean up test storage footprints and restore the user's original data."""
        if os.path.exists(DATA_FILE):
            os.remove(DATA_FILE)
        if self.backup_existed:
            os.rename(DATA_FILE + ".bak", DATA_FILE)

    def test_save_and_load_cycle(self):
        """Verify written model collections can survive database re-hydration cycles."""
        m = Movie("Tenet", "Sci-Fi", 150)
        save_theater_data()
        
        # Verify physical file creation on disk
        self.assertTrue(os.path.exists(DATA_FILE))
        
        # Clear local working lists completely
        Movie.all_movies.clear()
        self.assertEqual(len(Movie.all_movies), 0)
        
        # Run database file re-hydration load
        load_theater_data()
        
        # Verify object structure returned safely
        self.assertEqual(len(Movie.all_movies), 1)
        self.assertEqual(Movie.all_movies[0].title, "Tenet")

if __name__ == "__main__":
    unittest.main()