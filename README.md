---

# Function Calculator

This is a Python application with a graphical user interface (Tkinter) that allows users to:
- Input and analyze different types of functions,
- Calculate important function properties (such as vertex and intersection points),
- Save functions into a database,
- Draw function graphs,
- View a history of entered functions.

---

## Features

✅ **Linear Functions** (`y = kx + m`):
- Calculates the intersection with the x-axis.
- Draws the function graph.

✅ **Quadratic Functions** (`y = ax² + bx + c`):
- Calculates the vertex (highest/lowest point).
- Calculates intersection points with the x-axis.
- Draws the function graph.

✅ **Inverse Functions** (`y = a/x`):
- Recognizes the inverse function and saves it into the database.

✅ **History**:
- Stores and displays all functions entered by the user from the database.

---

## Installation

1. **Clone or download** this repository.
2. **Install required libraries** (if not already installed):
   ```bash
   pip install tkinter
   pip install sqlite3
   ```
   *(Note: `tkinter` is usually included with standard Python installations.)*

3. **Run the program**:
   ```bash
   python <your_file_name>.py
   ```

---

## Project Structure

- `Users_Database.db` — SQLite database for storing user credentials and functions.
- The program automatically creates the necessary database tables if they do not exist.
- Functions are saved under the username in the database.

---

## Technologies Used

- Python 3
- Tkinter — for GUI
- SQLite3 — for local database

---

## Author
- Developer: German Veideman

---
