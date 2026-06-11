# Movie Theater Management System (CLI Tool)

A pure Python Command-Line Interface (CLI) application built to streamline theater administration workflows. This system allows users to handle a complete multi-entity matrix tracking **Movies**, **Screenings (Showtimes)**, and **Customer Ticket Bookings** directly from the terminal with full local data persistence.

---

## 🚀 Key Architectural Features

* **Object-Oriented Domain Layer:** Implements strong encapsulation principles using Python `@property` decorators and setters to guarantee strict runtime validation (e.g., rejecting blank text entries, zero values, or negative movie durations).
* **Relational Integrity Constraints:** Enforces relational integrity through automated cascade updates. Deleting a parent `Movie` automatically cleanses the system by purging all scheduled `Screenings` and stripping out corresponding `Booking` transactions.
* **Robust Persistence Engine:** Re-hydrates state information across application cycles using local JSON data serializations, complete with defensive error handling (`try-except`) against structural file corruption.
* **Modular Code Structure:** Decoupled data architecture separating runtime entries, physical File I/O handlers, tracking models, and terminal input flags.

---

## 📂 Project Structure

```text
movie_theater_cli/
│
├── data/
│   └── theater_storage.json      # Persistent local database state
│
├── models/
│   ├── __init__.py               # Packages structural initialization (empty file)
│   ├── movie.py                  # Movie domain class (Validations & Counters)
│   ├── screening.py              # Screening relationship mappings
│   └── booking.py                # Transaction ticket tracking attributes
│
├── utils/
│   ├── __init__.py               # Packages structural initialization (empty file)
│   └── storage_handler.py        # File I/O loading & saving engine
│
├── main.py                       # Application entrance & argparse subcommands
├── requirements.txt              # Project third-party dependencies (tabulate)
└── README.md                     # Technical project documentation
⚙️ Installation and Setup
Follow these operational steps to configure your environment and run the workspace application:

1. Clone & Navigate to Project Directory
Bash
cd movie_theater_cli
2. Configure System Dependencies (Ubuntu / WSL Fix)
Ensure your Ubuntu Linux or WSL subsystem has the necessary core Python development utilities installed:

Bash
sudo apt update
sudo apt install python3-pip python3-venv -y
3. Create and Activate the Isolated Virtual Environment
Bash
# Build the virtual environment folder
python3 -m venv .venv

# Activate the sandbox environment
source .venv/bin/activate
Note: Your terminal prompt will now display (.venv) at the beginning of the line.

4. Install Project Requirements
Bash
pip install -r requirements.txt
🛠️ Usage & Command Guide
Once your environment is active, manage the database state cleanly from your terminal layout using the main.py entry point:

Movie Management
Create/Add a Movie:

Bash
python main.py add-movie --title "Interstellar" --genre "Sci-Fi" --duration 169
List All Movies:

Bash
python main.py list-movies
Delete a Movie (Triggers Cascading Cleanup):

Bash
python main.py delete-movie --id 1
Screening Schedule Management
Schedule a Showtime (Pass the parent Movie ID):

Bash
python main.py add-screening --movie-id 1 --hall 5 --time "2026-06-15 20:00"
List Current Theater Schedule:

Bash
python main.py list-screenings
Ticket Booking Management
Book Customer Seating Tickets:

Bash
python main.py book-ticket --screening-id 1 --name "Zach" --seats 3
List All Transaction Records:

Bash
python main.py list-bookings
📋 User Stories Satisfied
As an Admin, I can add a movie profile with details like title, genre, and duration so it becomes available within our theater configurations for active scheduling.

As an Admin, I can view structured listings of movies, screenings, and bookings to track hall asset allocations and current showtime occupancy.

As an Admin, I can cancel or drop entire core movie listings safely, knowing the underlying architecture will sweep through the storage files and wipe out dependent screenings and client tickets cleanly.