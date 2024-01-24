# OpenWeatherMap Weather Information

This Python script allows users to retrieve current weather information for a specified city using the OpenWeatherMap API. The script prompts the user to enter a city name, sends an HTTP GET request to the OpenWeatherMap API, and then displays the weather description and temperature in Celsius.

## Getting Started

### Prerequisites

To use this script, you need to obtain an OpenWeatherMap API key. You can sign up for a free API key on the [OpenWeatherMap website](https://openweathermap.org/).

### Installation

Install the required 'requests' module by running the following command:

```bash
pip install requests
````

## Usage
1. Open the script in a Python environment (e.g., Jupyter Notebook, VSCode).
2. Enter a city name when prompted.
3. The script will send an API request to OpenWeatherMap and display the current weather description and temperature in Celsius.
  
## Code Structure
The script is organized into the following sections:

1. Import Module: Import the 'requests' module for making HTTP requests.

2. API Key and URL Definition:

  - Define the OpenWeatherMap API key for authentication (API_KEY).
  - Define the base URL for the OpenWeatherMap API to retrieve weather information (BASE_URL).
    
3. User Input:

  - Prompt the user to enter a city name for which they want to get weather information.
    
4. API Request:

  - Construct the URL for the API request using the user-specified city and API key.
  - Send an HTTP GET request to the OpenWeatherMap API.
    
5. API Response Handling:

  - Check if the API request was successful (HTTP status code 200).
  - Parse the JSON data received in the response into a Python dictionary.
  - 
6. Display Results:

  - Extract the weather description and temperature from the response data.
  - Print the retrieved weather description and temperature in Celsius.
    
7. Error Handling:

  - Print an error message if the API request was not successful.
    
## Contributing
Feel free to contribute to the development of this script by opening issues or submitting pull requests.

## License
This script is provided under the MIT License - see the LICENSE.md file for details.


## Screenshots

![image1](https://github.com/allysonpereira/weather_checker/assets/113621581/99c5aa39-3869-43e9-9f5a-8c2c3a2b20fc)

![image2](https://github.com/allysonpereira/weather_checker/assets/113621581/8aea14c7-2f4a-4f45-aaae-56a747fca023)
