import requests


class Weather:

    KEY = ""

    def __init__(self, key):
        self.KEY = key

    def __callAPI(self, link):
        req = requests.get(link)
        data = req.json()
        return data

    def __convertKtoC(self, temp):
        return round(temp-273.15, 1)

    """
    getWeather takes a location and returns a dictionary
    the dictionary contains whether the API call was successful, if it is successful then it also 
    contains weather description, current temperature, current feels like temperature, and humidity. 
    """

    def getWeather(self, location: str):
        try:
            geo_data = self.__callAPI(
                "http://api.openweathermap.org/geo/1.0/direct?q="+location+"&limit=2&appid="+self.KEY)
            lat = str(geo_data[0]['lat'])
            lon = str(geo_data[0]['lon'])
            api_data = self.__callAPI(
                "https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid="+self.KEY)
            weather = api_data['weather'][0]['description']
            temperature = str(self.__convertKtoC(
                api_data['main']['temp']))+"°C"
            feels_like = str(self.__convertKtoC(
                api_data['main']['feels_like']))+"°C"
            humidity = str(api_data['main']['humidity'])+"%"
            return {'success': True, 'weather': weather, 'temperature': temperature, 'feels like': feels_like, 'humidity': humidity}
        except Exception:
            return {'success': False}

    # DECIDED TO USE DATETIME INSTEAD
    # def getTimeFromLocation(self, location):

    #     #from location to lat lon
    #     geo_data = self.__callAPI("http://api.openweathermap.org/geo/1.0/direct?q="+location+"&limit=2&appid="+self.KEY)
    #     lat = str(geo_data[0]['lat'])
    #     lon = str(geo_data[0]['lon'])

        #from lat lon to timezone

