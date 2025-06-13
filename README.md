# Weather CLI App ☀️🌧️

A simple Python command-line application that fetches and displays real-time weather data using the OpenWeatherMap API. Users can search weather by city name or zip code, save and view favorite locations, reload their last search, and manage their saved locations.

---

## 🔧 Features

- 🌆 Search weather by **City Name** or **Zip Code**
- 📊 View **Temperature**, **Feels Like**, **Humidity**, and **Conditions**
- ⭐ Save locations as **Favorites**
- 📂 Reload the **Last Searched Location**
- ❌ **Delete** favorite locations
- 🧠 Smart error handling and data persistence using JSON and text files

---

## ▶️ How to Run

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/weather-cli-app.git
   cd weather-cli-app
   ```

2. **Set up your API key**  
   - Open `config.py`
   - Replace `None` with your OpenWeatherMap API key:  
     ```python
     def get_api_key():
         return "your_api_key_here"
     ```

3. **(Optional) Set units**  
   - Set `"imperial"` (°F) or `"metric"` (°C) in `get_units()`.

4. **Run the application**  
   ```bash
   python main.py
   ```

---

## 💾 Data Storage

- **Favorites**: Stored in `favorites.json`  
- **Last searched location**: Stored in `last_location.txt`

---

## 📦 Requirements

- Python 3.7+
- Internet connection
- A valid [OpenWeatherMap](https://openweathermap.org/api) API key

---

## 📁 Project Structure

```
weather-cli-app/
│
├── main.py              # Main CLI loop
├── weather.py           # API request logic
├── config.py            # API key & units
├── storage.py           # File I/O for saved locations
├── favorites.json       # Favorite locations (auto-created)
├── last_location.txt    # Last searched location (auto-created)
└── README.md            # You're here!
```

---

## 🧠 Future Improvements (Ideas)

- Display additional weather metrics (wind, pressure)
- Auto-refresh weather at intervals
- Optional config file for customization
- Cross-platform packaging as an executable

---

## 🧑‍💻 Author

Created by [Daniel Jarvis](https://github.com/gandalf-ddj)

---

## 🪪 License

This project is open-source and free to use.
