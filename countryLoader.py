import requests

class CountryLoader():

    def get_countrys(self):

        data = requests.get("https://restcountries.com/v3.1/all")
        data = data.json()
        return data
