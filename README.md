<table>
  <tr>
    <td><img src="https://github.com/harshjuly12/OpenWeatherAPI-Python/assets/112745312/9a6eafe1-e1a8-4a86-9d95-77e2ea008bf4" width="80" style="margin-right: 10;"></td>
    <td><h1 style="margin: 0;">WeatherApp-Python</h1></td>
  </tr>
</table>

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Example](#example)
7. [Error Handling](#error-handling)
8. [Contributing](#contributing)
9. [License](#license)
10. [Author](#author)

## Introduction
WeatherApp-Python is a simple Python application that fetches & displays weather info for a given city using the OpenWeatherMap API.

## Features
- Fetches current weather conditions
- Displays temperature in Fahrenheit
- Handles city not found errors gracefully

## Prerequisites
- Python 3.x
- `requests` library

## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/WeatherApp-Python.git
    cd WeatherApp-Python
    ```

2. **Install the required Python package:**
    ```bash
    pip install requests
    ```

## Usage
1. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api).

2. Replace the `api_key` variable in the script with your OpenWeatherMap API key:
    ```python
    api_key = 'your_api_key_here'
    ```

3. Run the script:
    ```bash
    python weather_app.py
    ```

4. Enter the name of the city when prompted.

## Example
Enter city: New York
The weather in New York is: Clear
The temperature in New York is: 75ºF

## Error Handling
If the city is not found, the program will output:
No City Found


## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
For any questions or suggestions, please contact:
- Harsh Singh: [harshjuly12@gmail.com](harshjuly12@gmail.com)
- GitHub: [harshjuly12](https://github.com/harshjuly12)
