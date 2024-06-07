# Weather Forecast Application

This is a simple weather forecast application built using Python and Tkinter for the GUI. The application fetches weather data for a given city using the OpenWeatherMap API and displays the temperature, humidity, wind speed, pressure, and precipitation.

## Features

- Fetch and display current weather information for a specified city.
- Display temperature, humidity, wind speed, pressure, and precipitation.
- User-friendly interface built with Tkinter.

## Requirements

- Python 3.x
- `tkinter` (usually included with Python)
- `requests` library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/weather-forecast-app.git
    cd weather-forecast-app
    ```

2. Install the required Python packages:

    ```bash
    pip install requests
    ```

3. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api) by signing up and creating an API key.

4. Create a file named `API_KEY.py` in the project directory and define your API key:

    ```python
    # API_KEY.py
    api_key = 'your_actual_api_key_here'
    ```

5. Run the application:

    ```bash
    python main.py
    ```

## Usage

1. Enter the name of the city for which you want to fetch the weather information in the input field.
2. Click the "Search" button.
3. The application will display the current temperature, humidity, wind speed, pressure, and precipitation for the specified city.

## Project Structure

- `main.py`: The main script containing the Tkinter GUI and logic to fetch and display weather data.
- `API_KEY.py`: A separate file to store the OpenWeatherMap API key (this file should be added to `.gitignore` to prevent exposing your API key).

## Example

![Weather Forecast Application Screenshot](screenshot.png)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
