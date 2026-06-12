import argparse
import sys
from utils.storage_handler import load_theater_data, save_theater_data
from models.movie import Movie
from models.screening import Screening
from models.booking import Booking

def print_welcome_dashboard():
    """Prints a clean visual command guide when the app boots up without flags."""
    print("=" * 60)
    print("        MOVIE THEATER MANAGEMENT SYSTEM SYSTEM ACTIVE       ")
    print("=" * 60)
    print("\nAvailable Terminal Commands Guide:\n")
    
    print("  [ MOVIE MANAGEMENT ]")
    print("  • Add a Movie:     python main.py add-movie --title \"<name>\" --genre \"<genre>\" --duration <mins>")
    print("  • View Catalog:    python main.py list-movies")
    print("  • Delete a Movie:  python main.py delete-movie --id <movie_id>")
    print("\n  [ SCREENING SCHEDULE ]")
    print("  • Add Showtime:    python main.py add-screening --movie-id <id> --hall <number> --time \"<HH:MM>\"")
    print("  • View Timetable:  python main.py list-screenings")
    print("\n  [ CLIENT BOOKINGS ]")
    print("  • Book Tickets:    python main.py book-ticket --screening-id <id> --name \"<client>\" --seats <count>")
    print("  • View Receipts:   python main.py list-bookings")
    print("\n" + "=" * 60)
    print(" Provide a command sequence above to execute a management task.")
    print("=" * 60 + "\n")

def main():
    load_theater_data()
    
    # If the user runs the app without arguments, show the guide and exit cleanly
    if len(sys.argv) == 1:
        print_welcome_dashboard()
        return

    parser = argparse.ArgumentParser(description="Movie Theater Management Suite")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- Commands Registrations ---
    p_add_movie = subparsers.add_parser("add-movie", help="Register a new movie profile")
    p_add_movie.add_argument("--title", required=True)
    p_add_movie.add_argument("--genre", required=True)
    p_add_movie.add_argument("--duration", required=True, type=int)

    subparsers.add_parser("list-movies", help="Show all cataloged films")

    p_del_movie = subparsers.add_parser("delete-movie", help="Remove a movie and drop dependencies")
    p_del_movie.add_argument("--id", required=True, type=int)

    p_add_scr = subparsers.add_parser("add-screening", help="Schedule a unique screening event")
    p_add_scr.add_argument("--movie-id", required=True, type=int)
    p_add_scr.add_argument("--hall", required=True, type=int)
    p_add_scr.add_argument("--time", required=True)

    subparsers.add_parser("list-screenings", help="Show current theater schedule")

    p_add_book = subparsers.add_parser("book-ticket", help="Execute a customer seat transaction ticket")
    p_add_book.add_argument("--screening-id", required=True, type=int)
    p_add_book.add_argument("--name", required=True)
    p_add_book.add_argument("--seats", required=True, type=int)

    subparsers.add_parser("list-bookings", help="Display all transactional records")

    args = parser.parse_args()

    try:
        if args.command == "add-movie":
            m = Movie(args.title, args.genre, args.duration)
            print(f"Success: Registered {m}")
        
        elif args.command == "list-movies":
            if not Movie.all_movies: print("No movies cataloged yet.")
            for movie in Movie.all_movies: 
                print(f"ID {movie.id}: {movie.title} | Genre: {movie.genre} | {movie.duration_mins} Mins")

        elif args.command == "delete-movie":
            if Movie.delete_movie(args.id): print(f"Success: Dropped Movie ID {args.id} and matching dependencies.")
            else: print(f"Error: Movie ID {args.id} does not exist.")

        elif args.command == "add-screening":
            if not Movie.find_by_id(args.movie_id):
                print(f"Error: Movie reference key ID {args.movie_id} does not exist.")
                return
            s = Screening(args.movie_id, args.hall, args.time)
            print(f"Success: Scheduled showtime: {s}")

        elif args.command == "list-screenings":
            if not Screening.all_screenings: print("Schedule clear.")
            for scr in Screening.all_screenings:
                mv = Movie.find_by_id(scr.movie_id)
                m_title = mv.title if mv else "Unknown Movie"
                print(f"Showtime ID {scr.id}: '{m_title}' | Hall {scr.hall_number} at {scr.time}")

        elif args.command == "book-ticket":
            if not Screening.find_by_id(args.screening_id):
                print(f"Error: Screening event ID {args.screening_id} not found.")
                return
            b = Booking(args.screening_id, args.name, args.seats)
            print(f"Success: Finalized booking transaction: ID {b.id} for {b.customer_name}")

        elif args.command == "list-bookings":
            if not Booking.all_bookings: print("No transactions recorded.")
            for bk in Booking.all_bookings: 
                print(f"Ticket ID {bk.id}: {bk.customer_name} booked {bk.seats_booked} seats (Screening ID: {bk.screening_id})")

        save_theater_data()

    except ValueError as e:
        print(f"Validation Failure: {e}")

if __name__ == "__main__":
    main()