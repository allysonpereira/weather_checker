
Weather Information Retrieval

This Python script allows you to retrieve weather information for a specific city using the OpenWeatherMap API. It is a simple command-line tool that prompts the user to enter a city name and then fetches and displays the current weather conditions for that city. The code follows these steps:

## Usage

1. Imports the 'requests' module for making HTTP requests.
2. Defines the OpenWeatherMap API key, which is used for authentication.
3. Prompts the user to enter a city name for which they want to fetch weather data.
4. Constructs the URL for the API request using the entered city and API key.
5. Sends an HTTP GET request to the OpenWeatherMap API.
6. If the API request is successful (HTTP status code 200):
- Parses the received JSON data into a Python dictionary. 
- Extracts and displays the weather description and temperature in Celsius.
7. If there's an error with the API request, it prints an error message.

This script is a useful tool for quickly checking the weather conditions in a specific city by interacting with a weather API. It can be extended or integrated into other applications that require weather data retrieval.


## Screenshots

![image1](https://github.com/allysonpereira/weather_checker/assets/113621581/99c5aa39-3869-43e9-9f5a-8c2c3a2b20fc)

![image2](https://github.com/allysonpereira/weather_checker/assets/113621581/8aea14c7-2f4a-4f45-aaae-56a747fca023)
