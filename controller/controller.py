import requests
import time


class Controller:
    @staticmethod
    def get_weather(city):
        weather_api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=4c95d8ca369ab06cd32c7963ed0b3983"  # from here we get our data about weather
        json_data = requests.get(weather_api).json()  # get weather data in json form

        weather_condition = json_data['weather'][0]['main']
        temperature = int(json_data['main']['temp'] - 273.15)  # transform from Kelvin to Celsius
        temp_min = int(json_data['main']['temp_min'] - 273.15)
        temp_max = int(json_data['main']['temp_max'] - 273.15)
        wind_speed = json_data['wind']['speed']
        sunrise = time.strftime('%H:%M:%S', time.gmtime(
            json_data['sys']['sunrise'] + 10800))  # Romania is in GMT+3, so we add 3600*3 seconds
        sunset = time.strftime('%H:%M:%S', time.gmtime(json_data['sys']['sunset'] + 10800))  # convert to our timezone

        important_info = 'Condition: ' + weather_condition + '\n' + 'Temperature: ' + str(temperature) + ' °C' + '\n'
        less_important_info = 'Max temperature: ' + str(temp_max) + ' °C' + '\n' + 'Min temperature: ' + str(temp_min) + ' °C' + '\n' + \
                              'Wind speed: ' + str(wind_speed) + '\n' + 'Sunrise: ' + sunrise + '\n' + 'Sunset: ' + \
                              sunset

        return important_info, less_important_info
