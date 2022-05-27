import requests

class weather:

    KEY = "3fb551e63f9e07cb81cc64ff1bf4fb61" #find a way to hide key
    
    def getWeather(location: str):
        geo_encode_link= "http://api.openweathermap.org/geo/1.0/direct?q="+location+"&limit=2&appid="+KEY_BEG
        geo_link = requests.get(geo_encode_link)
        geo_data = geo_link.json()
        lat = str(geo_data[0]['lat'])
        lon = str(geo_data[0]['lon'])
        complete_api_link = "https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid="+KEY
        api_link = requests.get(complete_api_link)
        api_data = api_link.json()
        weather = api_data["weather"][0]['description']
        temperature = str(round(api_data["main"]['temp']-273.15,1))
        feels_like = str(round(api_data["main"]["feels_like"]-273.15,1))
        humidity = str(api_data["main"]['humidity'])
        results = {'weather':weather,'temperature':temperature,'feels like': feels_like,'humidity':humidity}
        return results

    











