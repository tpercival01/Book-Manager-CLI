import json
import os

def load_file():
    if not os.path.isfile("save_file.json"):
        print("\nNo save file found, continuing as new user.\n")
        return {}
    
    try: 
        with open("save_file.json", "r") as infile:
            json_object = json.load(infile)
            print("\nFile loaded successfully.\n")
        return json_object
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
            print("\n File has been saved.")
    except Exception as e:
        print("Error occured: {e}")

def create_save_data(bookcase):
    json_data = []
    try:
        for id in bookcase.books:
            temp = bookcase.books[id].get_book()
            json_data.append(temp)
    except:
        return json.dumps(json_data, indent=4)
    
    return json.dumps(json_data, indent=4)