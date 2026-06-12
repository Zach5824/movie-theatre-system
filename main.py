import argparse
from utils.storage_handler import load_theater_data, save_theater_data
from models.movie import Movie
from models.screening import Screening
from models.booking import Booking

def main():
    load_theater_data()
    
    parser = argparse.ArgumentParser(description="Movie Theater Management Suite")
    subparsers = parser.add_add_subparsers(dest="command", required=True)

    # --- Movie Management Subcommands ---
    p_add_movie = subparsers.add_parser("add-movie", help="Register a new movie profile")
    p_add_movie.add_argument("--title", required=True, help="Movie Title")
    p_add_movie.add_argument("--genre", required=True, help="Genre category")
    p_add_movie.add_argument("--duration", required=True, type=int, help="Runtime duration in minutes")

    subparsers.add_parser("list-movies", help="Show all cataloged films")

    p_del_movie = subparsers.add_parser("delete-movie", help="Remove a movie and drop dependencies")
    p_del_movie.add_argument("--id", required=True, type=int, help="Target Movie unique ID")

    # --- Screening Management Subcommands ---
    p_add_scr = subparsers.add_parser("add-screening", help="Schedule a unique screening event")
    p_add_scr.add_argument("--movie-id", required=True, type=int, help="Parent Movie ID link")
    p_add_scr.add_argument("--hall", required=True, type=int, help="Theater hall assignment number")
    p_add_scr.add_argument("--time", required=True, help="Showtime timestamp string (e.g. '18:30')")

    subparsers.add_parser("list-screenings", help="Show current theater schedule")

    # --- Ticket Booking Subcommands ---
    p_add_book = subparsers.add_parser("book-ticket", help="Execute a customer seat transaction ticket")
    p_add_book.add_argument("--screening-id", required=True, type=int, help="Target Screening ID")
    p_add_book.add_argument("--name", required=True, help="Customer registration name")
    p_add_book.add_argument("--seats", required=True, type=int, help="Total seats needed")

    subparsers.add_parser("list-bookings", help="Display all transactional records")

    args = parser.parse_args()

    