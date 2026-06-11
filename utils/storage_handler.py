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

def load_theater_data():
    if not os.path.exists(DATA_FILE):
        return
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        
        Movie.all_movies.clear()
        Screening.all_screenings.clear()
        Booking.all_bookings.clear()

        for m in data.get("movies", []): Movie(m["title"], m["genre"], m["duration_mins"], m["id"])
        for s in data.get("screenings", []): Screening(s["movie_id"], s["hall_number"], s["time"], s["id"])
        for b in data.get("bookings", []): Booking(b["screening_id"], b["customer_name"], b["seats_booked"], b["id"])
    except (json.JSONDecodeError, KeyError, TypeError):
        print("Warning: Data file corrupted. Starting clean database environment.")