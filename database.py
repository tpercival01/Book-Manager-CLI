import json
import os
import shutil
from book import Bookcase, Book
from graphics import display_messages

def load_file():
    if not os.path.isfile("save_file.json"):
        print("\nNo save file found, continuing as new user.\n")
        return Bookcase()
    try: 
        with open("save_file.json", "r") as infile:
            json_object = json.load(infile)

        json_temp = {}
        for id in json_object:
            temp_book = Book(json_object[id]["title"],
                         json_object[id]["author"],
                         json_object[id]["rating"],
                         json_object[id]["comments"],
                         json_object[id]["finished"],
                         json_object[id]["total_pages"],
                         json_object[id]["total_chapters"],
                         json_object[id]["progress"],
                         json_object[id]["status"] 
                         )
            json_temp[id] = temp_book

        bookcase = Bookcase()
        bookcase.bulk_add_books(json_temp)

        display_messages("File loaded successfully.")
        return bookcase
    except json.JSONDecodeError:
        print("Error: Could not decode json.")
        return {}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {}
    
def save_file(json_object):
    try:
        with open("save_file.json", "w") as outfile:
            json.dump(json_object, outfile)
    except Exception as e:
        print(f"Error occured: {e}")

def create_save_data(bookcase):
    json_data = {}
    for id in bookcase.books:
        temp = {
                "title": bookcase.books[id].title,
                "author": bookcase.books[id].author,
                "progress": bookcase.books[id].progress,
                "status": bookcase.books[id].status,
                "total_chapters": bookcase.books[id].total_chapters,
                "total_pages": bookcase.books[id].total_pages,
                "rating": bookcase.books[id].rating,
                "comments": bookcase.books[id].comments,
                "finished": bookcase.books[id].finished
        }
        json_data[id] = temp

    return json_data

def create_backup():
    try:
        os.mkdir("backups")
    except FileExistsError:
        pass

    if os.path.isfile("save_file.json"):
        destination = os.path.join("backups", "save_file.json")
        shutil.copy2("save_file.json", destination)