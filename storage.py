import json

def save_last_location(location_type, location_value):
    with open("last_location.txt", "w") as file:
        file.write(f"{location_type}:{location_value}")

def load_last_location():
    try:
        with open("last_location.txt", "r") as file:
            line = file.read().strip()
            location_type, location_value = line.split(":", 1)
            return location_type, location_value
    except FileNotFoundError:
        return None, None
    except ValueError:
        return None, None

def add_favorite(location_type, location_value):
    try:
        with open('favorites.json', 'r') as file:
            favorites = json.load(file)
    except FileNotFoundError:
        favorites = []

    new_favorite = {'type': location_type, 'value' : location_value}

    if {'type' : location_type, 'value' : location_value} not in favorites:
        favorites.append(new_favorite)
        with open('favorites.json', 'w') as file:
            json.dump(favorites, file, indent=2)
    else:
        print(f"{location_type}:{location_value} already exists")
        return

def delete_favorites():
    try:
        with open('favorites.json', 'r') as file:
            data = json.load(file)
            if not data:
                print('\nNo favorite locations found yet.')
                return
            print('\nFavorite locations:')
            for i, item in enumerate(data, 1):
                print(f'{i}. {item["type"].title()}: {item["value"]}')
            user_choice = input('\nChoose a favorite location to delete: (enter number value or type "back" to leave)\n').lower()
            if user_choice == 'back':
                return
            else:
                delete_index = int(user_choice) - 1
                if 0<= delete_index < len(data):
                    deleted = data.pop(delete_index)
                    with open('favorites.json', 'w') as file:
                        json.dump(data, file, indent=2)
                    print('\nFavorite location deleted.')
                else:
                    print('\nInvalid selection. Please choose a number on the list.')
    except FileNotFoundError:
        print('\nNo favorite locations found yet.')