"""Main Weather CLI Application"""

import json
from config import get_api_key, get_units
from weather import get_weather_by_city, get_weather_by_zip
from storage import save_last_location, load_last_location, add_favorite, delete_favorites


def weather_check(data):
    """Print weather or an error message if data is None"""
    if data:
        print_weather(data)
    else:
        print("\nCouldn't retrieve weather data.")


def print_weather(data):
    """Display weather details"""
    print("\n🌦️ Weather Summary:")
    print(f"City: {data['city']}")
    print(f"Temperature: {data['temp']}°F")
    print(f"Feels like: {data['feels_like']}°F")
    print(f"Humidity: {data['humidity']}%")
    print(f"Condition: {data['description'].title()}")


def city_name():
    """Handle search by city name"""
    city = input("\nEnter a city name: ").title()
    data = get_weather_by_city(city)
    if data:
        print_weather(data)
        save_last_location("city", city)
        save = input('\nDo you want to save the last location? (yes/no):\n').lower()
        if save == "yes":
            add_favorite("city", city)
            print("New favorite saved.")
    else:
        print("\n❌ Couldn't retrieve weather data.")


def city_zip():
    """Handle search by zip code"""
    zip_code = input("\nEnter a zip code: ")
    data = get_weather_by_zip(zip_code)
    if data:
        print_weather(data)
        save_last_location("zip", zip_code)
        save = input('\nDo you want to save the last location? (yes/no):\n').lower()
        if save == "yes":
            add_favorite("zip", zip_code)
            print("New favorite saved.")
    else:
        print("\n❌ Couldn't retrieve weather data.")


def favorite_locations():
    """Display and handle favorite location selection"""
    try:
        with open("favorites.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            if not data:
                print("\nNo favorite locations found yet.")
                return

            print("\nFavorite locations:")
            for i, item in enumerate(data, 1):
                print(f"{i}. {item['type'].title()}: {item['value']}")

            user_input = input(
                '\nChoose a favorite to view: (enter a number or type "back")\n'
            ).lower()
            if user_input == "back":
                return

            fav_index = int(user_input) - 1
            if 0 <= fav_index < len(data):
                favorite = data[fav_index]
                if favorite["type"] == "city":
                    weather_check(get_weather_by_city(favorite["value"]))
                elif favorite["type"] == "zip":
                    weather_check(get_weather_by_zip(favorite["value"]))
            else:
                print("Invalid selection. Please choose a number on the list.")

    except FileNotFoundError:
        with open("favorites.json", "w", encoding="utf-8") as file:
            json.dump([], file)
            print("\nNo favorite locations found yet.")


def main():
    """Main menu loop"""
    while True:
        print("--- Welcome to the Weather CLI App! ---\n")
        user_input = input(
            "What would you like to do?\n"
            "1. Search by City Name\n"
            "2. Search by Zip Code\n"
            "3. Load Last Location\n"
            "4. Search from Favorite Locations\n"
            "5. Delete Favorite Locations\n"
            "6. Exit\n"
        )

        if user_input == "1":
            city_name()
        elif user_input == "2":
            city_zip()
        elif user_input == "3":
            location_type, location_value = load_last_location()
            if location_type == "city":
                weather_check(get_weather_by_city(location_value))
            elif location_type == "zip":
                weather_check(get_weather_by_zip(location_value))
            else:
                print("\nNo saved search found.\n")
        elif user_input == "4":
            favorite_locations()
        elif user_input == "5":
            delete_favorites()
        elif user_input == "6":
            print("\n--- Thank you for using Weather CLI App! ---\n")
            break
        else:
            print("\nInvalid input. Please select a valid option.\n")


if __name__ == "__main__":
    main()
