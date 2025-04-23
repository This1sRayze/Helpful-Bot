# Terminal Notes App
A simple terminal-based note-taking application written in Python. It supports multiple users, note creation, viewing, and persistent storage to a local file.

## Features
- Create and store notes with timestamps
- Multi-user support with user-specific access to notes
- View individual notes or all your notes
- Notes are saved in a text file and reloaded on startup
- User-friendly colored CLI output

## Requirements
- Python 3.10+
- requirements.txt
Install requirements.txt with pip if needed:
```bash
pip install requirements.txt
```

## Getting Started

1. Clone the repository or copy the source code.
2. Make sure the following modules are available in your project:
   - `id_generator.py`
   - `printer_functions.py`
   - `classes.py`
3. Run the application:
```bash
python main.py
```

### Available Commands

```
1) exit - to exit the application
2) add_note - to add a new note
3) print_note [i] - to print note number i (1-based index)
4) print_all - to print all your notes
5) help - to print this command menu
```

### Example

```
Please enter your username: alice
Please enter command (enter exit to stop): add_note
Please enter note text: Buy milk

✅ Note added successfully!

Please enter command (enter exit to stop): print_all

1: "Buy milk"
- Created on 23.04.2025 10:32
```

## Data Storage

Notes are saved in `notes.txt` in the following format:

```
<note_id>;<note_text>;<creation_datetime>
```

## To Do

- Add note deletion/editing
- Password protection for users
- Search and filter notes


