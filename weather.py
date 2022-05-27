from logging import exception
from warnings import catch_warnings
import requests

class weather:

    KEY = "3fb551e63f9e07cb81cc64ff1bf4fb61" #find a way to hide key
    """
    getWeather takes a location and returns a dictionary
    the dictionary contains whether the API call was successful, if it is successful then it also 
    contains weather description, current temperature, current feels like temperature, and humidity. 
    """
    def getWeather(self, location: str):
        try:
            geo_encode_link= "http://api.openweathermap.org/geo/1.0/direct?q="+location+"&limit=2&appid="+self.KEY
            geo_link = requests.get(geo_encode_link)
            geo_data = geo_link.json()
            lat = str(geo_data[0]['lat'])
            lon = str(geo_data[0]['lon'])
            complete_api_link = "https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid="+self.KEY
            api_link = requests.get(complete_api_link)
            api_data = api_link.json()
            weather = api_data["weather"][0]['description']
            temperature = str(round(api_data["main"]['temp']-273.15,1))
            feels_like = str(round(api_data["main"]["feels_like"]-273.15,1))
            humidity = str(api_data["main"]['humidity'])
            results = {'success':True ,'weather':weather,'temperature':temperature,'feels like': feels_like,'humidity':humidity}
            return results
        except exception:
            return {'success':False}

    











