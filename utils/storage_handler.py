import json
import os
from models.movie import Movie
from models.screening import Screening
from models.booking import Booking

DATA_FILE = "data/theater_storage.json"

def save_theater_data():
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    payload = {
        "movies": [m.to_dict() for m in Movie.all_movies],
        "screenings": [s.to_dict() for s in Screening.all_screenings],
        "bookings": [b.to_dict() for b in Booking.all_bookings]
    }
    with open(DATA_FILE, "w") as f:
        json.dump(payload, f, indent=4)

