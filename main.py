from datetime import datetime
from id_generator import id_generator
from printer_functions import print_error, print_success, input_colored
from classes import NoteUser

from colorama import init

init(autoreset=True)

note_list = [] 
note_file = "notes.txt"
note_id_generator = id_generator()
users_list = []


welcome_banner = '''
▗▖ ▗▖▗▞▀▚▖█ ▄▄▄▄  ▗▞▀▚▖ ▄▄▄     ▗▄▄▖  ▄▄▄     ■  
▐▌ ▐▌▐▛▀▀▘█ █   █ ▐▛▀▀▘█        ▐▌ ▐▌█   █ ▗▄▟▙▄▖
▐▛▀▜▌▝▚▄▄▖█ █▄▄▄▀ ▝▚▄▄▖█        ▐▛▀▚▖▀▄▄▄▀   ▐▌  
▐▌ ▐▌     █ █                   ▐▙▄▞▘        ▐▌  
            ▀                                ▐▌                                                                                              
'''

commands = '''
1) exit - to exit the application
2) add_note - to add a new note
3) print_note [i] - to print note number i
4) print_all - to print all notes 
5) help - to print this menu
'''

def add_new_note(note_text, current_user: NoteUser) -> bool:
    note_creation_date = datetime.today()
    next_id = note_id_generator()
    note_list.append({"text": note_text, "creation_date": note_creation_date, "id": next_id})
    current_user.notes_ids.append(next_id)
    return True

def print_note(index: int, current_user: NoteUser):
    note = note_list[index]
    if note['id'] not in current_user.notes_ids:
        print_error("User can not access this note")
        return
    formatted_creation_date = note["creation_date"].strftime("%d.%m.%Y %H:%M")
    print(f'{note["id"]}: "{note["text"]}"\n- Created on {formatted_creation_date}\n')

def print_all_notes(current_user: NoteUser):
    for note_index in range(len(note_list)):
        print_note(note_index, current_user)

def find_top_note_id(notes: list[dict]) -> int:
    max_id = 0
    for note in notes:
        note_id = note['id']
        if note_id > max_id:
            max_id = note_id
    return max_id

def find_top_note_id_functional(notes: list[dict]) -> int:
    return max([note['id'] for note in notes] + [0])

def save_notes():
    with open(note_file, 'w') as file:
        for note in note_list:
            file.write(f'{note['id']};{note["text"]};{note["creation_date"]}\n')

def read_notes() -> list[dict]:
    note_list = []
    with open(note_file) as file:
        for line in file:
            id, text, date = line.strip().split(';')
            creation_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
            note_list.append({"id": int(id), "text": text, "creation_date": creation_date})
    return note_list

def init_note_app():
    global note_list
    note_list = read_notes()

    max_note_id = find_top_note_id_functional(note_list)

    global note_id_generator
    note_id_generator = id_generator(max_note_id)

    print(welcome_banner)
    print("\nHello and welcome to our app!\n")
    print(commands)
    print()

def find_user_by_login(login: str) -> NoteUser | None:
    note_user = None
    for user in users_list:
        if user.login == login:
            note_user = user
    return note_user

def get_user() -> NoteUser:
    user_login = input_colored("Please enter your username:")
    found_user = find_user_by_login(user_login)
    if not found_user:
        print_error("User not found")
        found_user = NoteUser(user_login)
        users_list.append(found_user)
        print_success("User created")
    return found_user


def main():
    current_user = get_user()
    while True:
        command, *args = input_colored("Please enter command (enter exit to stop): ").strip().split(' ') 
        if command == 'exit':
            print('Goodbye!')
            save_notes()
            break
        elif command == 'add_note':
            text = input_colored("Please enter note text: ")
            if add_new_note(text, current_user):
                print_success("\nNote added successfully!\n")
            else:
                print_error("\nError while adding a note!\n")
        elif command == 'help':
            print(commands)
        elif command == 'print_note':
            if len(args) < 1:
                print_error("Please enter a note number")
                continue
            index = int(args[0]) - 1
            if index < 0 or index >= len(note_list):
                print_error("Please enter a valid note number")
                continue
            print_note(index, current_user)
        elif command == 'print_all':
            print_all_notes(current_user)

init_note_app()
main()
