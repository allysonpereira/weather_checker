# Import the 'requests' module to make HTTP requests.
import requests

# Define the OpenWeatherMap API key, which is used to authenticate and access the weather data.
API_KEY = "94ea14b8d7e44478a518869035995b0f"

# Define the base URL for the OpenWeatherMap API to retrieve weather information.
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Prompt the user to enter a city name for which they want to get weather information.
city = input("Enter a city name: ")

# Construct the URL for the API request, including the API key and the user-specified city.
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

# Send an HTTP GET request to the OpenWeatherMap API using the constructed URL.
response = requests.get(request_url)

# Check if the API request was successful (HTTP status code 200).
if response.status_code == 200:
    # Parse the JSON data received in the response into a Python dictionary.
    data = response.json()

    # Extract the weather description from the response data.
    weather = data['weather'][0]['description']

    # Extract the temperature in Kelvin from the response data and convert it to Celsius.
    temperature = round(data["main"]["temp"] - 273.15, 2)

    # Print the retrieved weather description and temperature in Celsius.
    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
else:
    # Print an error message if the API request was not successful.
    print("An error occurred.")
