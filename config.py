import os
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

def get_api_key():
    return os.getenv("API_KEY")

def get_units():
    # Change to 'metric' for Celsius
    return "imperial"
