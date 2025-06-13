from config import get_api_key, get_units
from weather import get_weather_by_city, get_weather_by_zip
from storage import save_last_location, load_last_location, add_favorite, delete_favorites
import json

def weather_check(weather):
    if weather:
        print_weather(weather)
    else:
        print('\nCouldn\'t retrieve weather data.')

def print_weather(weather):
    print("\n🌦️ Weather Summary:")
    print(f"City: {weather['city']}")
    print(f"Temperature: {weather['temp']}°F")
    print(f"Feels like: {weather['feels_like']}°F")
    print(f'Humidity: {weather['humidity']}%')
    print(f"Condition: {weather['description'].title()}")
    
def city_name():
    city = input("\nEnter a city name: ").title()
    weather = get_weather_by_city(city)
    if weather:
        print_weather(weather)
        save_last_location('city', city)
        save = input('\nDo you want to save the last location? (yes/no):\n').lower()
        if save == 'yes':
            add_favorite('city', city)
            print('New favorite saved.')
    else:
        print("\n❌ Couldn't retrieve weather data.")

def city_zip():
    zip_code = input("\nEnter a zip code: ")
    weather = get_weather_by_zip(zip_code)
    if weather:
        print_weather(weather)
        save_last_location('zip', zip_code)
        save = input('\nDo you want to save the last location? (yes/no):\n').lower()
        if save == 'yes':
            add_favorite('zip', zip_code)
            print('New favorite saved.')
    else:
        print("\n❌ Couldn't retrieve weather data.")

def favorite_locations():
    try:
        with open('favorites.json', 'r') as file:
            data = json.load(file)
            if not data:
                print('\nNo favorite locations found yet.')
                return
            print('\nFavorite locations:')
            for i, item in enumerate(data, 1):
                print(f'{i}. {item["type"].title()}: {item["value"]}')
            user_input = input('\nChose a favorite to view: (enter a number value or type "back" to leave)\n').lower()
            if user_input == 'back':
                return
            else:
                fav_index = int(user_input) - 1
                if 0 <= fav_index < len(data):
                    favorite = data[fav_index]
                    if favorite['type'] == 'city':
                        weather = get_weather_by_city(favorite['value'])
                        weather_check(weather)
                    elif favorite['type'] == 'zip':
                        weather = get_weather_by_zip(favorite['value'])
                        weather_check(weather)
                else:
                    print('Invalid selection. Please choose a number on the list.')

    except FileNotFoundError:
        with open('favorites.json', 'w') as file:
            json.dump([], file)
            print('\nNo favorite locations found yet.')

while True:
    print("---Welcome to the Weather CLI App!---\n")
    user_input = input('What would you like to do?\n'
                       '1. Search by City Name\n'
                       '2. Search by Zip Code\n'
                       '3. Load last Location\n'
                       '4. Search from Favorite Locations\n'
                       '5. Delete Favorite Locations\n'
                       '6. Exit\n')
    
    if user_input == "1":
        city_name()

    elif user_input == "2":
        city_zip()

    elif user_input == "3":
        location_type, location_value = load_last_location()
        if location_type == "city":
            weather = get_weather_by_city(location_value)
        elif location_type == "zip":
            weather = get_weather_by_zip(location_value)
        else:
            print('\nNo saved search found\n')
            continue
        if weather:
            print_weather(weather)

    elif user_input == "4":
        favorite_locations()

    elif user_input == "5":
        delete_favorites()

    elif user_input == "6":
        print("\n---Thank you for using Weather CLI App!---\n")
        break

    else:
        print('\nInvalid input. Please select a valid option.\n')
    
    



